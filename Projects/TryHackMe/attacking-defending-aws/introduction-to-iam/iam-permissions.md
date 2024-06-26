# IAM Permissions

## Structure of IAM Policy
A policy consists of:
- Statement ID (SID) - optional
- Action: a list of things the policy allows/denies
- Resources: the ARNs of resources the statement applies to
- Effec: either Allow or Deny
- Condition - optional: conditions that must be satisfied for the policy to grant permissions.

[AWS Managed Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) contains a list of actions that usually map to a specific job function.
```bash
aws iam list-policy
aws iam get-policy --policy-arn arn:aws:iam::aws:policy/AdministratorAccess
```

![image](https://github.com/hhphu/InfoSec/assets/45286750/e2af6f25-18b5-4cb3-9b9c-94cf58583dd4)


### Action
Actions consist of a service and an API call. Examples:
- ec2:StopInstance
- s3:GetObject
- sts:AssumeRole
- iam:ListUsers

### Resources
- Always in ARN format or *
- Essentials to achieving the principle of privilege. 

## Effect
- Can be Allow or Deny.
- There is implicit Deny, ie if there is no action defined, the policy automatically denies all premissions.

## Principal
- Only required for resource policies, not applicable to identities-based IAM Principal.
- If the principal is *, the policy applies to anyone or all AWS customers.

## Conditions
- Optional element in a policy.
- Condition statements have special operators that are used to evaluate the conditions (StringEquals, StringNotEquals, StringNotLike, StringLikeIfExists, etc.)


-----
# Answer the questions
- What is the PolicyId of the ReadOnlyAccess managed policy?
Run the following command to retrieve the Policy **ReadOnlyAccess** policy
```bash
aws iam get-policy --policy-arn arn:aws:iam::aws:policy/ReadOnlyAcces
```

![image](https://github.com/hhphu/InfoSec/assets/45286750/04782b03-2487-4907-af41-23233cf895a9)

`-> ANPAILL3HVNFSB6DCOWYQ`

- What action "Grants permission to create access key and secret access key for the specified IAM user"? You can find a hint in the [Service Authorization docs for IAM](https://docs.aws.amazon.com/service-authorization/latest/reference/reference.html)

`-> iam:createAccessKey`

- In your account, ther eis a bucket that begins with "tryhackme-bucket-" and ends with your unique account ID. What is the ARN of that bucket excluding the last 12 digit account ID?
Run the following command to list the s3 buckets
```bash
aws s3api lists-buckets
```

We now retrieve the whole name of the bucket. Run the following command with the bucket name

```bash
aws s3api get-bucket-policy --bucket $BUCKET_NAME
```

![image](https://github.com/hhphu/InfoSec/assets/45286750/3cfd24df-cb06-4465-a686-3be06b0fe365)

`-> arn:aws:s3:::tryhackme-bucket`

- Given the policy above, can this user get the HR Password (Y/N)?
```bash
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": [
                "ec2:Describe*",
                "secretsmanager:ListSecrets",
                "secretsmanager:GetSecretValue"
            ],
            "Resource": "*",
            "Effect": "Allow"
        },
        {
            "Action": ["*"],
            "Resource": "arn:aws:secretsmanager:us-east-1:123456789012:secret:HR-Passwords*",
            "Effect": "Deny"
        }
    ]
}
```
`-> N`

- Look in your account. What is the Principal that is allowed to assume the OrganizationAccountAccessRole role?
Run the following command to retrieve the **OrganizationAccountAccessRole**
```bash
aws iam get-role --role OrganizationAccountAccessRole
```

![image](https://github.com/hhphu/InfoSec/assets/45286750/ba13549a-4c25-4932-8095-46673e8685f2)

`-> "AWS": "arn:aws:iam::116457965582:root"`

- Given the Statement, the Glue Service, running in vpc-12345, can write an object to the my-logs-bucket? (T/F)
```bash
{
  "Effect": "Deny",
  "Principal": "*",
  "Action": "s3:PutObject",
  "Resource": "arn:aws:s3:::my-logs-bucket/AWSLogs/AccountNumber/*",
  "Condition": {
    "StringNotEquals": {
      "aws:SourceVpc": "vpc-abcdef2",
      "aws:PrincipalServiceName": "glue.amazonaws.com"
    }
  }
}
```
`-> F`

