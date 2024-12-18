# STS Credentials Lab
Understanding how credentials are generated is critical for attacking & defending a cloud account.

## Objectives
What will be learned:
- how to create an IAM User
- how to create long-term access keys
- how to export long-term access keys as shell environment variables
- how to validate the identity that is currently active
- how to assume a new role using the `aws sts assume-role` command
- how to export temporary session credentials as shell environment variables

## Createa a user
First we create a user named **padawan**

```bash
aws iam create-user --user-name padawan
```

Grant the user permission by adding it to the padawan group

```bash
aws iam add-user-to-group --user-name padawan --group-name padawans
```

Check for the to which the user belong

```bash
aws iam list-groups-for-user --user-name padawan
```

![image](https://github.com/user-attachments/assets/ac9e86e4-2697-4fc7-9cb4-94c7aee62e92)

**- What are the first four letters of the GroupId of the padawans group?**

-> `AGPA`

## Create an Access Key for the user
Configure the **padawan** account to authenticate to AWS APIs.

```bash
aws iam create-access-key --user-name padawan
```

![image](https://github.com/user-attachments/assets/6df345d7-5c39-4f88-a7f7-b54de1041128)

With the Access key and the SecretAccessKey, we can try to authenticate this user

```bash
export AWS_SECRET_ACCESS_KEY = $SECRET_ACCESS_KEY
export AWS_ACCESS_KEY_ID = $ACCESS_KEY_ID
```

Verify the user **padawan** has been successfully configured and authenticated.

```bash
aws sts get-caller-identity
```

**- What is the character length of the SecretAccessKey?**

-> `40`

## Assume the role of Jedi Master
We are going to generate a short-term key for an IAM Role, which **padawan** will use to temporarily authenticate to.
Three requirements:
1. Permission to assume the role "jedi". This permission has been provided by the policy attached to the **padawans** group.
2. The Amazon Resource Name (ARN) of the role we want to assume: **`arn:aws:iam::Account-ID:role/jedi`**
3. A Role Session Name - This string appears in CloudTrail logs and help administrators distinguish who/why a specific role was assumed.

```bash
aws sts assume-role --role-arn arn:aws:iam::637423357278:role/jedi --role-session-name Ahsoka
```

![image](https://github.com/user-attachments/assets/8d3af14a-b1a3-48ac-b59c-cff445301e42)

With the new AccessKey & the SecretAccessKey, combined with the Session Token generated, we can configure our machine to use the short-term credentials for authenticaion.

```bash
export AWS_SECRET_ACCESS_KEY=$SECRET_ACCESS_KEY
export AWS_ACCESS_KEY_ID=$ACCESS_KEY_ID
export AWS_SESSION_TOKEN=$SESSION_TOKEN
```

![image](https://github.com/user-attachments/assets/74bdcd65-0f1c-45ab-8ce0-0b5016b9f3e0)

**- How many minutes are your session credentials good for?**

-> `60`

**- How many AWS CLI environment variables were required to be set?**

-> `3`

Confirm that we have successfully authenticated with the short-term credentials

```bash
aws sts get-caller-identity
```

![image](https://github.com/user-attachments/assets/26115504-13d1-4bf5-b0d1-043e3cc6df03)

**- What IAM resource does the string that begins with AROA represent?**

-> `Role`
