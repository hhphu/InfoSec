# AWS Basic Concepts

## AWS Account
- An AWS acocunt is a container for AWS resources
- Assigned 12-digit unique Account ID.
### AWS Account Root User
- Has all priviledges
- By default does not have MFA -> must implement

## Identity and Access Management (IAM)
- AWS IAM means the capabilities and features of the IAM engine and service of AWS, determining how IAM principas are granted access to specific services, resources and capabilities.
- Use [policy evaluation logic form](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html) to determine whether and what type of access an AWS IAM principal has to a service/resource.

### IAM Roles
- AWS principals that have permission over AWS services/resource.
- Has "assume role" feature ("switch role"): Identities recognized by AWS IAM are allowed to gain priviledges of a particular IAM rol
- "AssumeRole Trust Policy": Determine what services/resources an AWS principal has priviledges over.

### Federated Identities and Identity Providers
AWS IAM support Security Assertion Markup Language (SAML 2.0) and Open ID Connect (OIDC) to federate identities from third-party Identiy Provider ((Azure Active Directory - AAD, Ping Identity, Okta, etc.)

## AWS Regions
### Global Services:
- Support a central control plane and data plane that are not specific to any AWS region.
- Examples: CloudFront, Route 53, Organizations, IAM, and STS (Security Token Service, which has both global and regional endpoints).

### Regional Services:
- Control and data planes are specific to geographic regions where AWS data centers are located.
- Example: US-East-1 corresponds to Northern Virginia data centers.
Important for data sovereignty and redundancy for multi-region workloads.

### Special Cases:
- STS: Tokens from regional endpoints are valid globally, whereas tokens from global endpoints are limited to default-enabled regions.
- S3 Buckets: The namespace is global (unique bucket names across AWS), but storage is regional.

### Default Regions
- Pre-2017: US-EAST-1 was the default for all AWS customers, leading to a concentration of resources in that region.
- Post-2017: New default regions are US-EAST-2 (Ohio) or US-WEST-2 (Oregon) for new accounts.

### Restricted Regions
Some regions are disabled by default and require manual enablement for use:
- Africa: Cape Town
- Asia Pacific: Hong Kong, Hyderabad, Jakarta, Melbourne
- Europe: Milan, Spain, Zurich
- Middle East: Bahrain, UAE
These regions cannot be accessed using global STS API endpoint credentials and require regional endpoint credentials.

### AWS Organizations
**Workload Segmentation**
- AWS Organizatios allows segmentation of workloads by collecting accounts under a single AWS Organization.
- Each account can represent different workloads with serparate security boundaries.

**Organizational Structure**
- Organizational Root: Parent container for all AWS accounts
- Organizational Untis (OUs): sub-containers that contains AWS accounts and services and nested OUs.

### Service Control Policies (SCP)
- Function of AWS Organization that allow customized security and access restrcitions on Organization Root, OUs or individual accounts
- SCP does not apply to Organization Management account -> ineffective for IAM roles and users within it.

## Virtual Private Cloud (VPC)
### VPC Components
- Internet Gateway: allow resources in the VPC to communicate with the Internet 
- Egress-only Gateway: allow 
IPv6 outbound communication from the VPC to the Internet 
- Subnets: segmented the VPC into subnetworks for 
different purposes 
- DNS: Using AWS Route 53 to assign IP address for VPC 
- DHCP: Automatically assign IP 
addresses for EC2 instances within VPC
- NAT Gateway: allow resources to communicate with other services outside the VPC.

-----
# Answer the questions
- How many digits are in an AWS Account ID?

`-> 12`

- Does AWS require customers to enforce MFA by default for root user credentials? (yay/nay)

`-> nay`

- What logic can be used to determine the access of an AWS IAM Principal?

`-> policy evaluation`

- What policy determines if an IAM principal has the ability to gain the privileges of a particular IAM role?

`-> assume-role`

- What AWS service has both global and regional API endpoints?

`->STS`

- If your AWS account was created prior to 2017, what is your account's default region?

`-> US-EAST-1`

- What year was AWS Organizations made generally available for AWS customers?

`-> 2017`

- What is the sub-container for accounts in AWS Organizations?

`Organizational Unit`

- What AWS Organizations account does Service Control Policies not apply to?

`-> Organization Management`

- What AWS service hosts the AWS DNS resolver?

`-> Route 53`

- What VPC feature was used for privilege escalation during the 2019 CapitalOne Breach?

`-> IMDS`

- What type of VPC endpoint will allow for network traffic inspection?

`-> Gateway Load Balancer`
