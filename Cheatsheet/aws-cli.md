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
