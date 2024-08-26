# The Quest for Least Privilege

## Introduction
- In this room , we will take a broadly scoped rule and whittle down access to allow the policy to do three things:
1. Audit all EC2 settings
2. Launch machines in the Singapore Region
3. Access a specific corporate S3 bucket
- Starting default AdministratorAccess policy

```bash
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "*",
            "Resource": "*"
        }
    ]
}
```

## Limiting by Service
- The requirement is to allow access to EC2 and S3 only. To do that, you’ll need to restrict the actions by service. That would look like this:

```bash
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PermitEC2",
            "Effect": "Allow",
            "Action": ["ec2:*", "XXX:*"],
            "Resource": "*"
        }
    ]
}
```
## Limiting by Read & Modify
- To make this a read-only audit role, We need to limit the policy to only List/Describe/Get actions:
```bash
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PermitEC2",
            "Effect": "Allow",
            "Action": [ "ec2:YYY*", "ec2:Get*" ],
            "Resource": "*"
        },
        {
            "Sid": "Permit S3",
            "Effect": "Allow",
            "Action": [ "s3:Get*", "s3:XXX*" ],
            "Resource": "*"
        }
    ]
}
```

## Enumerating specific resources
- Finally, we’ll limit this policy to a subset of resources using wildcards and prefixes. We start with a new statement to allow all actions on instances in Singapore.
We also need to add two resources to the S3 statement. The first statement refers to all the objects in the bucket and the second to the bucket itself.

```bash
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PermitEC2",
            "Effect": "Allow",
            "Action": [
            	"ec2:Describe*",
            	"ec2:Get*"
            ],
            "Resource": "*"
        },
        {
            "Sid": "Singapore",
            "Effect": "Allow",
            "Action": [
            	"ec2:*"
            ],
            "Resource": "arn:aws:ec2:XXXX:*:instance/*"
        },
        {
            "Sid": "Permit S3",
            "Effect": "Allow",
            "Action": "s3:Get*",
            "Resource": [
            	"arn:aws:s3:::my_corporate_bucket/*",
            	"arn:aws:s3:::my_corporate_bucket"
            ]
        }
    ]
}
```

-----

# ANSWER THE QUESTION 
- **If you are denied access while you have this policy, what type of policy is blocking you?**
`-> Sevice Control Polocy`

**What action is needed in place of XXX?**
`-> s3`

-**What is the redacted EC2 Action required in place of YYY?**
`-> Describe`

-**What is the redacted S3 Action required in place of XXX?**
`-> List`

- **What is the element needed in place of XXXX to represent the AWS Region (Singapore)?**
`-> ap-southeast-1`
