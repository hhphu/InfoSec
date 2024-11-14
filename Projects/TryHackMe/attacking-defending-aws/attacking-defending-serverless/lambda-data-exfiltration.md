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


