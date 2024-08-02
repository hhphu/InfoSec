# AWS IAM Enumeration

### Learning Objectives
- How IAM resource policies can be abused to identify valid IAM principals
- How to use upen source tools to efficiently enumerate valid principals in a given AWS account
- How to footprint potential services, including security services, enabled for an account

## AWS IAM Enumveration Mechanics
### Scavening for credentials
AWS Boto3 is popular libraries used to work wiht AWS. A few places to look for:
- Environment Variables: users can set credentials using `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` as environment variables.
- Shared credentials File (~/.aws/credentials): The most common place when storeing IAM user access keys or SSO configurations for assuming role.
- AWS Config file (`/.aws/config): Credential sources that referenc helper scripts and other external credentials providers are commonly referenced here.
- Assume Role Provider: when sombody uses AWS SSO/other mechanism to assume a role, it is cached at `~/.aws/cli/cache/$ROLE_SESSION_ID`
- Boto2 config file: predecessor version to Boto3 and may be used in legacy clients
- Instance Metadata Service: EC2 instances that have IAM roles configured.

### Get-Access-Key-Info
- When found an access key, we can use aws cli to extract information
```bash
aws sts get-access-key-info --access-key-id $ACCESS_KEY_ID
```

## Resource-Based Policies
- This is what a resource-based policy looks like, which may enable attackers to identify any valid IAM Principal in a given AWS account. Follow tricks [here](https://hackingthe.cloud/aws/enumeration/enum_iam_user_role/)
```bash
{       
"Statement": 
[{         
"Sid": "grant-1234-publish", 
        "Effect": "Allow", 
        "Principal": {           
               "AWS": {IAM_PRINCIPAL_TO_TEST} 
        }, 
        "Action": ["sns:Publish"], 
        "Resource": {EXAMPLE_SNS_TOPIC} 
      }] 
    }
```

## Enumerate IAM Users and Roles
- Quiet Riot is a tool used for unauthenticated enumeration of AWS/Azure Active Directory/Google Workspace users/principal. [Github](https://github.com/righteousgambit/quiet-riot)
- Install Quiet Riot
```bash
pip3 install quiet-riot
```

- Durin enumeration phase, we found 2 accounts Adam and John. We can generate potential usernames using [common patterns](https://www.interseller.io/blog/2019/02/04/top-email-address-patterns-by-company-size/) employed by companies and [common family names](https://github.com/danielmiessler/SecLists/blob/master/Usernames/Names/familynames-usa-top1000.txt).
```python
#!/usr/bin/env python
malenames = ['adam', 'john']
with open('familynames-usa-top1000.txt', 'r') as f:
    lastnames = f.read().splitlines()
with open('test.txt', 'w') as f:
    for i in malenames:
        for j in lastnames:
            first = i.lower()
            last = j.lower()
            f.write(f"{first}.{last}\n")
            f.write(f"{first[0]}{last}\n")
            f.write(f"{first}\n")
            f.write(f"{first}_{last}\n")
            f.write(f"{first}{last}\n")
            f.write(f"{first}{j[0].lower()}\n")
```

- Set up Quiet Riot to perform enumeration
```bash
quiet_riot --scan 5
```

## Enumerat Root User Email Adadress
```bash
quiet_riot --s 4
```


