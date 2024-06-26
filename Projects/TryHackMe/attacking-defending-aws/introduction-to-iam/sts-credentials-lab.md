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
![image](https://github.com/hhphu/InfoSec/assets/45286750/3d94d552-17f1-4a51-a574-632e63337801)

- Assign the user to **padawans** group
```bash
aws iam add-user-to-group --user-name padawan --group-name padawans
```

- Verify the group of the user
```bash
aws iam list-groups-for-user --user-name padawan
```
![image](https://github.com/hhphu/InfoSec/assets/45286750/e21ec6a1-9a1b-4a7d-bbb9-ebe5324c2cac)

### Create Access Key for user "padawan"
- Create access key for the user
```bash
aws iam create-access-key --user-name padawan
```
![image](https://github.com/hhphu/InfoSec/assets/45286750/6a5a1932-e01c-447b-a151-6afaa8e94cbe)

- Setting these environments in local machine, which tells AWS CLI what credentials to use.
```bash
export AWS_SECRET_ACCESS_KEY = $SECRET_ACCESS_KEY_VALUE
export AWS_ACCESS_KEY_ID = $ACCESS_KEY_ID_VALUE
```

### Validate the status on Local machine
```bash
aws sts get-caller-identity
```
![image](https://github.com/hhphu/InfoSec/assets/45286750/c569401d-fdec-42d7-96ae-c15dabd4a249)

- The above aws command is equivalent to `whoami` in Unix.

### Assume the Role of Jedi Master
- Generate a short-term key for IAM Role

![image](https://github.com/hhphu/InfoSec/assets/45286750/52676593-9935-4278-89d2-5dd7a9b052d5)

**REQUIREMENTS**
-----
1. Permission to assume the "jedi" role, which is in the policy attached to the **padawans** group. 
2. The Amazon Resource Name (ARN) of the role to be assumed: `arn:aws:iam::$Account_ID_From_TASK4:role/jedi`
3. A Role Session Name - This will appears in CloudTrail logs to help administrators distinguish who/why a specific role was assumed.

```bash
aws sts assume-role --role-arn arn:aws:iam::$Account_ID_From_TASK4:role/jadi --role-session-name $STRING
```
![image](https://github.com/hhphu/InfoSec/assets/45286750/502d3a1c-1952-4f95-a605-5656a8a55f42)

- Set the environment variables
```bash
export AWS_SECRET_ACCESS_KEY= $SECRET_ACCESS_KEY_VALUE
export AWS_ACCESS_KEY_ID= $ACCESS_KEY_ID_VALUE
export AWS_SESSION_TOKEN= $SESSION_TOKEN_VALUE
```
![image](https://github.com/hhphu/InfoSec/assets/45286750/7fb19524-e40d-4fd8-bedd-39d54b1dfc2a)

### Verify the identity
```bash
aws sts get-caller-identity
```
![image](https://github.com/hhphu/InfoSec/assets/45286750/24a30036-e8c2-4741-9aab-9fb3705c02e7)

# ANSWER THE QUESTIONS
- **What are the first four letters of the GroupId of the padawans group?**

`-> AGPA`

- **What is the character length of the SecretAccessKey?**

`-> 40`

- **How many minutes are your session credentials good for?**

`-> 60`

- **How many AWS CLI environment variables were required to be set?**

`-> 3`

- **What IAM resource does the string that begins with AROA represent?**

`-> Role`
