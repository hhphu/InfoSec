# IAM Credentials

## Root Password
- The most powerful credential in AWS.
- Password allows unrestricted access to the AWS account adn must e secured.
- If the AWS account was created via AWS Organizations using CreateAccount API, the password will be randomly generated and must be reset by the users.

## IAM Login Profile
- AWS's term for a user's console password.
- Not all IAM users have access to the AWS console. This has to be set by the admin/root

![d594618566b781a663bfde4b6af9bc65](https://github.com/hhphu/InfoSec/assets/45286750/7fb6c273-f05c-4004-9fd7-6df1f54e571a)

- To change user's password
```bash
aws iam update-login-profile --user TryHackMe-IAM-User --password 'SolarWinds123!'
```

## AWS API Access Key
- Use to create Access Keys for AWS Accounts.
- Two types: Long Term and Temporary Session keys
### Long Term keys
- Start with **AKIA**, consisting of Access Key ID and Secret Access Key
- Do not expire -> best practices = rotate the keys periodically.
- Can be active or inactive, which can be set using the command
```bash
aws iam update-access-key --access-key-id AKIA<SNIP> --status Inactive
aws iam update-access-key --access-key-id AKIA<SNIP> --status Active
```
- To delete an Access Key
```bash
aws iam delete-access-key --access-key-id AKIA<SNIP>
```
- To create a long term Access Key
```bash
aws iam create-access-key --user-name $USERNAME
```
- Once deleted, a long-term access key cannot be recreated.
### Session Keys
- Consist of: Access Key ID, Secret Access Key & Session token
- Start with **ASIA**
- Cannot be deleted/deactivated
- To generate Session Keys:
```bash
aws sts get-session-token
```

## MFA in AWS and Best Practices around Credentials
MFA is enabled for both Root and IAM users.
Best Practices for Handling AWS Access Keys:
- Minimize Use of IAM Users: Prefer using SAML or OIDC for session credentials for AWS API access.
- Never Commit Access Keys to Repositories: Avoid committing access keys to any source code repositories (public or private). GitHub scans public repositories and will disable exposed keys, but private repositories can also be compromised.
- Rotate Access Keys Frequently: Regularly rotate access keys and manage their storage carefully. Avoid accumulating CSV files with credentials in download folders to prevent unauthorized access if devices are compromised.
- Use MFA for Root and IAM Users: Enforce MFA for all critical accounts to enhance security.
- Guard IAM Identifiers: Although IAM identifiers like AKIA strings are not sensitive themselves, they can be used for reconnaissance to identify AWS accounts.

IAM Identifiers can sometimes be useful for reconnaissance. For example, AKIA strings, while not sensitive, can be used to identify an AWS Account with the following command:
```bash
aws sts get-access-key-info --access-key-id AKIAEXAMPLE
```

## How services get credentials
- To get credentials for a role: use **AWS STS AssumeRole API Call** or **aws sts assume-role** command
- Different services have different ways of requesting credentials to function.
- Use the following command to get temporary credentials. Note that a profile must be configured first
```bash
curl $AWS_CONTAINER_CREDENTIALS_FULL_URI -H "X-aws-ec2-metadata-token: $AWS_CONTAINER_AUTHORIZATION_TOKEN" 
```


-----
# ANSWER THE QUESTIONS
- **How many active IAM Access Keys does the TryHackMe-IAM-User have?**
Run `aws iam list-access-keys --user-name TryHackMe-Iam-User`

![image](https://github.com/hhphu/InfoSec/assets/45286750/294f4319-db31-4f80-bf51-ed31623970ba)

`-> 1`

- **Which user has an MFA attached to it?**
Run `aws iam list-users` to get the list of users

![image](https://github.com/hhphu/InfoSec/assets/45286750/ad6d208a-0123-468b-830a-30f1d8178973)

For each of the found users, run `aws iam list-mfa-devices --user-name $USERNAME`

![image](https://github.com/hhphu/InfoSec/assets/45286750/28f5abde-7b12-489d-9c15-410b19ababed)

`-> TryHackMe-IAM-User`

- **What account ID does "AKIASTZ6PFXLJW3RQWXC" belong to?**
Run `aws sts get-access-key-info --access-key-id AKIASTZ6PFXLJW3RQWXC`

![image](https://github.com/hhphu/InfoSec/assets/45286750/e2349789-8cfd-495d-b90b-5126ad8c8a6b)

`-> 179982773718`

- **Use the CloudShell and the curl command above to download temporary credentials, what is the JSON key that begins with "E"?**
Configure a profile in CloudShell
Run the following command:
```bash
curl $AWS_CONTAINER_CREDENTIALS_FULL_URI -H "X-aws-ec2-metadata-token: $AWS_CONTAINER_AUTHORIZATION_TOKEN" 
```

![image](https://github.com/hhphu/InfoSec/assets/45286750/fe132ae6-ed78-488f-8472-b65459349f4c)

`-> Experiation`

- **When using temporary credentials, what are the first four letters of the AccessKeyId?**
`-> ASIA`


  
