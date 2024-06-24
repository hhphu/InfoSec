# IAM Princials
- IAM Principals: people, applications & AWS services that can act on your AWS account
- IAM Policies: the definition of what a principal can do in your account
- IAM Credentials: the numerouse ways a principal can authenticate to the AWS control plane
- Least Privilege: How to create a policy with minmally scoped permissions and how AWS makes that difficult for a developer

## IAM users
- The most basic form of IAM Principal. 
- Has LoginProfile & up to 2 Access Keys
    - LoginProfile: password that can grant access to the AWS Web Console.
    - Access Keys: AWS generated and consiste of a Key ID & Secret
```bash
aws iam list-users
```

## IAM Roles
- AWWS Principal to be assumed by a person/service/resource.
- Has feature AssumeRole Trust Poliy, which determined which principal to be assumed by a role.

```bash
aws iam list-roles`
```
## Root User & AWS Accoount
### Root User 
- A special form of IAM Principal that represents account owner.
- Has full priviledges, subject to any Service Control Policies
### AWS Account
- Usually has no access to the root's email
- If AWS account is a member of AWS Organizations, we may retrieve the root email
```bash
aws organizations describe-organization
```
## IAM Groups
- A collections of IAM Users.
- Policies applied to Groups are also applicable to IAM Users.
```bash
aws iam list-groups
```

# Answer the questions
- There are two IAM Users in your account. The one you're using is the 12-digit account ID. What is the name of the other user?

`-> TryHackMe-IAM-User`

- There are several roles in your account. What is the Trusted Entity for the OrganizationAccountAccessRole role?                                                                
Run the command `aws iam list-roles`, we see the Trusted Entity is `arn:aws:iam::116457965582:root`

![image](https://github.com/hhphu/InfoSec/assets/45286750/26bfcd58-7c3e-4e8e-a3c0-6a26bb6c5984)

`->  arn:aws:iam::637423357278:saml-provider/TryHackMe-IAM-SAMLProvider`      

- What is the MasterAccountEmail for your TryHackMe account?
Run the following command to retrieve the root email `aws organizations describe-organization`

![image](https://github.com/hhphu/InfoSec/assets/45286750/63d74fc1-08f8-45cc-950a-d69b5f1f918c)

`-> aws-security-labs@tryhackme.com`

- What is the name of the IAM Group your IAM User is currently a member of?
Running the command `aws iam list-groups` , we see there are two existing groups.
Run the command `aws iam get-group --group-name $GROUPNAME`, we find the current user is the member of `TryHackMe-IAM-Group`.

![image](https://github.com/hhphu/InfoSec/assets/45286750/28226454-5ef7-48b1-a248-eddf5e7db378)

`-> IAMModule-Group`

- What AWS Service is trusted to assume the Role “AWSServiceRoleForCloudFormationStackSetsOrgMember”?
Run the command `aws iam list-roles`, we get the answer.

![image](https://github.com/hhphu/InfoSec/assets/45286750/80461102-bfb4-4fca-aa35-96c11ccf2879)

`-> member.org.stacksets.cloudformation.amazonaws.com`

- What is the name of the Sample SAML Identity Provider in your account?
Navigate to **IAM Roles** & check the **Trust Relationships**

![image](https://github.com/hhphu/InfoSec/assets/45286750/243f0fa0-7883-4356-b0f2-41c978c65efc)

`-> TryHackMe-IAM-SAMLProvider`

