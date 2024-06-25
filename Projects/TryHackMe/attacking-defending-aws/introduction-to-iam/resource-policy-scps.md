# Resource Policies & SCPs

## Resource Policies
- Attached to resources and determine the Principals that can act on the resource.
- Consider the following statement:
```bash
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "Make Object Readable",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::tryhackme-public-bucket/*"
    },
    {
      "Sid": "Make Bucket Attributed World Readable",
      "Effect": "Allow",
      "Principal": {
        "AWS": "*"
      },
      "Action": [
        "s3:Get*",
        "s3:ListBucket"
      ],
      "Resource": "arn:aws:s3:::tryhackme-public-bucket"
    }
  ]
}
```
From the above policies, we learn:
- Anyone can perform **GetObject** action on any object of the **tryhackme-public-bucket** bucket (arn:aws:s3:::tryhackme-public-bucket/*)
- Anyone can perform any of the **Get** action on ONLY the **tryhackme-public-bucket** bucket (arn:aws:s3:::tryhackme-public-bucket)

- Get bucket policy status
```bash
aws s3api get-bucket-policy-status --bucket tryhackme-public-bucket
```
- Invoke Lambda function:
```bash
aws lambda invoke --function-name arn:aws:lambda:us-east-1:019181489476:function:TryHackMe-time time && cat time | jq -r
```

## Service Control Policies
- Function of AWS Organizations, allowing confiuring restrictions on which principals can have permissions over a service/resources.
- More customized policies and provide flexibility to tailored the policies to meet specific needs.
- Users in AWS Account cannot view the Service Control Policies applied to the account. However, some AWS error messages will indicate if an SCP denied an action.
```bash
  aws guardduty delete-detector --detector-id `aws guardduty list-detectors --query DetectorIds --output text`
```

-----
# ANSWER THE QUESTIONS
- **Try running the s3api command "get-bucket-ownership-controls" against the tryhackme-public-bucket. What is the ObjectOwnership value set to?**
-----
```bash
aws s3api get-bucket-ownership-controls --bucket tryhackme-public-bucket

```
![image](https://github.com/hhphu/InfoSec/assets/45286750/a7c67e24-153a-481f-ab57-2d4e24562a33)

 `-> BucketOwnerPreferred`
 

- **Try invoking the Lambda function "TryHackMe-quote" in the same 019181489476 Account. What's the quote returned from the function?**

**Prerequisite:** Must configure an AWS profile on your local machine and have its region set to us-east-1
```bash
  aws configure --profile $PROFILE_NAME
```
Run the following command to invoke Lambda function:
```bash
aws lambda invoke --function-name arn:aws:lambda:us-east-1:019181489476:function:TryHackMe-quote --profile $PROFILE_NAME time && cat time | jq -r
```
![image](https://github.com/hhphu/InfoSec/assets/45286750/9c22cf32-c247-46e9-aa4f-cb73aff85da7)

`-> Most heard comment at #reinvent 'dude, lambda is the coolest shit, ever' -- Werner Vogles 2014`

- **What are the last four words of the error message you get when attempting to disable GuardDuty with this command?**
```bash
aws guardduty delete-detector --detector-id 'aws guardduty list-detectors --query DetectorIds --output text'
```

![image](https://github.com/hhphu/InfoSec/assets/45286750/b2fc7202-8412-4dec-8c1a-a441b0e6ead9)

`-> with an explicit deny`
