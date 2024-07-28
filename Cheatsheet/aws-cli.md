# Cheatsheet for AWS CLI

## IAM Users
- List IAM users
```bash
aws iam list-users
```
- Retrieve a user's key
```bash
aws iam list-access-keys --user-name admin
```

## IAM Roles
- List IAM roles
```bash
aws iam list-roles
```

## Root user
- If an AWS Account is a member of AWS Organization, we can run the command to retrieve root's email
```bash
aws organizations describe-organization
```
## IAM Groups
- List IAM groups
```bash
aws iam list-groups
```
- Retrieve an IAM group
```bash
aws iam get-group --group-game $GROUP_NAME
```
## IAM Credentials
### API Access Keys
- Set Acccess Key active/inactive
```bash
# Set inactive
aws iam update-access-key --access-key-id $ACCESS_KEY_VALUE --status Inactive

# Set active
aws iam update-access-key --access-key-id $ACCESS_KEY_VALUE --status Active
```
- Delete an Access Key
```bash
aws iam delete-access-key --access-key-id $ACCESS_KEY_VALUE 
```
- Create a long-term Access Key
```bash
aws iam create-access-key --user-name $USERNAME
```
- To generate a Session Key
```bash
aws sts get-session-token
```

### MFA
- Check if user has MFA enabled
```bash
aws iam list-mfa-devices --user-name $USERNAME
```
## IAM Permissions
### IAM Policy
- List policy
```bash
aws iam list-policy
```
- Retrieve a policy
```bash
aws iam get-policy --policy-arn $POLICY_ARN
```
## S3
- List S3 buckets
```bash
aws s3api list-buckets
```
- Retrieve a bucket policy
```bash
aws s3api get-buket-policy --bucket $BUCKET_NAME
```


