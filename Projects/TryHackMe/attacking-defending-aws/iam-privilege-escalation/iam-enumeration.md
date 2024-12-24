# AWS IAM Enumeration

### Learning Objectives
- How IAM resource policies can be abused to identify valid IAM principals
- How to use upen source tools to efficiently enumerate valid principals in a given AWS account
- How to footprint potential services, including security services, enabled for an account

## AWS IAM Enumveration Mechanics
### Scavening for credentials
AWS Boto3 is popular libraries used to work wiht AWS. A few places to look for:
- **Environment Variables:** users can set credentials using `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` as environment variables.
- **Shared credentials File (~/.aws/credentials):** The most common place when storeing IAM user access keys or SSO configurations for assuming role.
- **AWS Config file (`/.aws/config):** Credential sources that referenc helper scripts and other external credentials providers are commonly referenced here.
- **Assume Role Provider:** when sombody uses AWS SSO/other mechanism to assume a role, it is cached at `~/.aws/cli/cache/$ROLE_SESSION_ID`
- **Boto2 config file:** predecessor version to Boto3 and may be used in legacy clients
- **Instance Metadata Service:** EC2 instances that have IAM roles configured.

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
- To enumerate an IAM Principal via resource policy:
	1. Create the resource that supports a resource-based policy
	2. Update it to allow access for the Principal you want to test whether it exists
	3. If !exists -> error message. Else: the update is implemented.

### ANSWER THE QUESTIONS
**- If an IAM Principal does not exist, what does an attempt to update the resource-based policy to include the "Principal" return?**

-> `error message`

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

- A pre-generated wordlist can be downloaded here

```bash
curl https://gist.githubusercontent.com/righteousgambit/72220f9b7296f83133240d06d9653c0a/raw/eea20d3390e01e5570018b222633336c6c13d3fd/Common%2520Adam%2520and%2520John%2520Usernames -o pregenerated-usernames.txt
```

- Set up Quiet Riot to perform enumeration
```bash
quiet_riot --scan 5
```

- To enumertate IAM role, we select option 1. For IAM user, we select option 2.
- Then we provide the AWS Account ID we find when running `aws sts get-caller-identity`
- Specify the pre-generated-usernames.txt file

![image](https://github.com/user-attachments/assets/843830b8-9ed1-4e05-9ded-6089c7b45742)

  
## ANSWER THE QUESTIONS
- **What is John's username? **

-> `john.cervantes` 

- **What is Adam's last name?**

-> `foreman`

## Enumerat Root User Email Adadress
- AWS S3 ACLs policy can be used to place email addresses that correspond to potential root user email addresses.
```bash
quiet_riot --s 4
```
- For this option, we need a `rootuser.txt` to enumerate. This process may take a while. Hence, it's best to perform it once we found a list of usernames.
- Becasue of sensitivity, this is just a theory that no activity is availalble for this action.

## Footprinting services
- We can enumerate services to see which one is running using quiet-riot.

```bash
quiet_riot --s 3
```

- We see that there are 6 principals found.

  ![image](https://github.com/user-attachments/assets/653e48ff-5079-4ba2-9dab-dd6e0a7d4855)

- Amongst them, there are only 5 assumed roles, i.e every principal but this one

```bash
arn:aws:iam::637423357278:role/OrganizationAccountAccessRole
```

## ANSWER THE QUESTIONS
- **How many roles does Quiet Riot identify in your account when you run the Service Footprinting option?**

-> `5`

- **What services appear enabled based on the results?**

  Go to the AWS Console and inspect each of the service, we see that Rout53resolver service has not been configured, meaning that it is not enabled.

->  `guardduty, organizations, support, trustedadvisor`
