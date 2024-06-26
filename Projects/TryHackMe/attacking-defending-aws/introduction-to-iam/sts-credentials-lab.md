# STS Credentials Lab

![image](https://github.com/hhphu/InfoSec/assets/45286750/918ba69b-9b59-4bcb-9c0c-165485f0ee32)

Understand how credentials are generated for better attacking and defending a cloud account.

## Objectives:
In this lab, I learned:
- how to create an IAM User
- how to create long-term access keys
- how to export long-term access keys as shell environment variables
- how to validate the identity that is currently active
- how to assume a new role using the aws sts assume-role command
- how to export temporary session credentials as shell environment variables

### Create a user "padawan"
- Create a user
```bash
aws iam create-user --user-name padawan
```

- Assign the user to **padawans** group
```bash
aws iam add-user-to-group --user-name padawan --group-name padawans
```

- Verify the group of the user
```bash
aws iam list-groups-for-user --user-name padawan
```

### Create Access Key for user "padawan"
- Create access key for the user
```bash
aws iam create-access-key --user-name padawan
```
- Setting these environments in local machine, which tells AWS CLI what credentials to use.
```bash
export AWS_SECRET_ACCESS_KEY = $SECRET_ACCESS_KEY_VALUE
export AWS_ACCESS_KEY_ID = $ACCESS_KEY_ID_VALUE
```

### Validate the status on Local machine
```bash
aws sts get-caller-identity
```
- The above aws command is equivalent to `whoami` in Unix.

### Assume the Role of Jedi Master
- Generate a short-term key for IAM Role

![image](https://github.com/hhphu/InfoSec/assets/45286750/52676593-9935-4278-89d2-5dd7a9b052d5)

**REQUIREMENTS**
-----
1. Permission to assume the "jedi" role, which is in the policy attached to the **padawans** group. 
2. The Amazon Resource Name (ARN) of the role to be assumed: `arn:aws:iam::Account-ID-From-TASK4:role/jedi`
3. A Role Session Name - This will appears in CloudTrail logs to help administrators distinguish who/why a specific role was assumed.

```bash
aws sts assume-role --role-arn arn:aws:iam::Account-ID-From-TASK4:role/jadi --role-session-name $STRING
```
- Set the environment variables
```bash
export AWS_SECRET_ACCESS_KEY= $SECRET_ACCESS_KEY_VALUE
export AWS_ACCESS_KEY_ID= $ACCESS_KEY_ID_VALUE
export AWS_SESSION_TOKEN= $SESSION_TOKEN_VALUE
```
### Verify the identity
```bash
aws sts get-caller-identity
```
