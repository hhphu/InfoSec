# Project Overview
In this project, I implement and enforce identity access management within AWS. I will:
- Implement a role structure with policies that will be evaluated and enforced.
- Evaluate an access control matrix and restrictions to ensure that each role has the appropriate policies and permissions implemented with the principle of least privilege.
- Create an AWS Config rule that will alert on a policy that does not meet the organizational requirements.
- Finish this project with a visualization of organizational roles and policies.

# Main Steps
Here are the main steps:
1. Using the [access control matrix document](./Access_Control_Matrix.xlsx) , evaluate the IAM permissions that were associated with the policies created as part of the "iam-policies" CloudFormation stack.
2. Within the AWS console, navigate to the "IAM" service and navigate to "Policies." Search for four policies (outlined in later pages), and update each IAM policy to only have statements that can be directly associated with the permissions defined in the access control matrix.
3. Associate the appropriate policies to roles as directed.
4. Test the roles to ensure the appropriate access has been defined.
5. Update the provided Lambda code to reflect restrictions as directed.
6. Appropriately mark an IAM policy as non-compliant.
7. Design a visualization to document the work.

# Set up
As a prerequisite, CloudFormation stacks will need to be created to complete the project. Within the project folder there is a folder called `cloudformation_templates`. Each file inside this folder is a CloudFormation template that will be used to create a CloudFormation stack so that the appropriate resources are created.

Assuming that the AWS credentials have been configured using the AWS CLI, the CloudFormation stacks can be created. Within the `cloudformation_templates` directory, the following commands can be used to create each stack.
```bash
aws --region=us-east-1 cloudformation create-stack --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND --stack-name iam-roles --template-body file://iam_roles.yml
```

```bash
aws --region=us-east-1 cloudformation create-stack --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND --stack-name iam-policies --template-body file://iam_policies.yml
```

```bash
aws --region=us-east-1 cloudformation create-stack --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND --stack-name config-deps --template-body file://config_dependencies.yml
```

```bash
aws --region=us-east-1 cloudformation create-stack --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND --stack-name resources --template-body file://resources.yml
```

Report of the project can be found [here](./enterprise-identity-and-access-control.pdf).