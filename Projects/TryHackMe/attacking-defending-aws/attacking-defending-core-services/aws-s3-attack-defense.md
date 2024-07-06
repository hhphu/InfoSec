# AWS S3 - Attak and Defense

# S3 Service Overview
## Directory Structure
- S3 BUcket is a file storage system like UNIX systems.
- There can be multiple folders and files inside a bucket
- Buckets cannot be tested inside other buckets.

## Object "Durability"
- Claimed by AWS: 99.999999999% durability
- Neverthelss, S3 still loses roughly 1000 objects/year

## Access Controln Lists
  - ACLs are original methods for controlling access to S3 buckets.
  - When a bucket is created, full permission is automatically granted to the owner/creator. ACLs allows more customized permissions for other AWS principals and services.
 
```xml
<!--?xml version="1.0" encoding="UTF-8"?-->
<accesscontrolpolicy xmlns="http://s3.amazonaws.com/doc/2006-03-01/">

  <owner>

    <id>79a59df900b949e55d96a1e698fbacedfd6e09d98eacf8f8d5218e7cd47ef2be</id>

    <displayname>wladd@tryhackme.com</displayname>

  </owner>

  <accesscontrollist>

    <grant>

      <grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="Canonical User">

        <id>79a59df900b949e55d96a1e698fbacedfd6e09d98eacf8f8d5218e7cd47ef2be</id>

        <displayname>wladd@tryhackme.com</displayname>

      </grantee>

      <permission>FULL_CONTROL</permission>

    </grant>

  </accesscontrollist>

</accesscontrolpolicy>
```

THe above ACL grant **FULL_CONTROL** permission to the **Canonical User** whose id is `79a59df900b949e55d96a1e698fbacedfd6e09d98eacf8f8d5218e7cd47ef2be` and display name is `wladd@tryhackme.com`

## Bucket Policy
- Bucket Policy are like ACLs, but is more readable for users

```json
{

    "Version": "2012-10-17",

    "Statement": [

        {

            "Sid": "PublicRead",

            "Effect": "Allow",

            "Principal": "*",

            "Action": [

                "s3:GetObject",

                "s3:PutObject"

            ],

            "Resource": [

                "arn:aws:s3:::my-bucket/*"

            ]

        }

    ]

}
```

# CloudFront Overview
- AWS content Distribution Network offering service.
- Provide better user experience by caching customers' content over distributed networks worldwide -> more scalable for static content with lower latency
- Can be used for some security controls: Geo-restricted contents, authenticated contents (meaning users have to authenticate to view the contents), data encryption, etc.
- INtegrated with AWS Web Application Firewall (WAF) & AWS Shield/SHield Advanced Distributed Denial-of-Service protections.
## CloudFront "Origin"
- Resourc to be hosted behind the CloudFront.
- Can be EC2 instance or S3 bucket objects

# Lab - Identify Misconfigured CloudFront Distributions
- CloudFront Origins are connected to EC2, S3 buckets, API Gateway enpoints ore Elastic Load Balancers.
- When properly configured, only CloudFront Distribution should have access to the back-end/internal resources. However, not many customers are aware of this -> misconfiguration
- An Origina Access Identity (OAI) specifies CloudFront to access internal resources by putting the OAI into the resource's policy.

```bash
{ "Sid": "1", "Effect": "Allow", "Principal": { "AWS": "arn:aws:iam::cloudfront:user/CloudFront Origin Access Identity EAF5XXXXXXXXX" }, "Action": "s3:GetObject", "Resource": "arn:aws:s3:::SAMPLE_BUCKET/*" }
```

- The above OAI allows CloudFront to perform `s3:GetObject` requests against the `SAMPLE_BUCKET` and its objects.
- To find out misconfigured CloudFront Origins, we can leverage [DNS reconnaissance](https://tryhackme.com/r/room/passiverecon) techniques.

## Certificate Transparency Logs
- `crt.sh` is one of many public resources to identify certificates for DNS domains that are logged.

## Analyze Hosts of Certificate Transparency Log Results
- `bestcloudcompany.org` will be the example target

```bash
nslookup bestcloudcompany.org
```
- From the output IP address, perform another `nslookup`

```bash
nslookup 44.203.62.152
```

![image](https://github.com/hhphu/InfoSec/assets/45286750/bd9760d6-a428-476c-903b-57bc04b5a818)

- From the about input, it seems the website is hosted on an EC2 instance whose IP address is 44.203.62.152
- Perform similar command on the `assets.bestcloudcompany.org`

```bash
nsloookup assets.bestcloudcompany.org
nslookup $IP 
```

![image](https://github.com/hhphu/InfoSec/assets/45286750/23500025-9623-4a42-8602-fd7b911e6f16)

- From here, we see the `assets.bestcloudcompany.org` is using CloudFront.
- Visitng the `assets.bestcloudcompany.org` on the browser, we learn that the site might be using S3 bucket for the content.

  ![image](https://github.com/hhphu/InfoSec/assets/45286750/2fbf353b-d31a-44c3-a3d7-6c29910705f2)

## Enumerate S3 buckets
### Naming convention
THere are two conventional ways for naming S3 buckets: `assets.$DOMAIN_NAME.com.s3.amazonaws.com` or `$ORG_NAME-prod.s3.amaoznaws.com`

### DNS Recon
- Since we know the `assets.bestcloudcompany.org` might be using S3 bucket, we can try doing DNS reconnaissance based on the two most popular naming conventions

```bash
nslookup assets.bestcloudcompany.org.s3.amazonaws.com
```

OR 

```bash
nslookup bestcloudcompany-prod.s3.amazonaws.com
```

![image](https://github.com/hhphu/InfoSec/assets/45286750/765085e1-ebb2-44a7-9a18-a6b0ba74cc16)

- Now we can confirm `assets.bestcloudcompany.org.s3.amazonaws.com` exists. Run the following command to dump the entire bucket:

```bash
aws s3 sync s3://$BUCKET_NAME . --no-sign-request

--no-sign-request: you're not using AWS credentials to perform the above command, meaning the bucket is publicly accessible.
```

![image](https://github.com/hhphu/InfoSec/assets/45286750/85a0cc2f-5a2d-4cda-9a7f-40e14e8efa1f)

### AWS Service Substrate
- S3 buckets not only host contents for static websites but also store files for other AWS services like AWS CloudFormation Template or Lambda fucntions.Becasue of this, if we see a bucket containg any other resrouces, we can try to modify those files to leverage an attack.
- 

# ANSWER THE QUESTIONS
- **What is the name of the file storage container where you keep your data in S3?**

-> `bucket`

- **What characteristic makes Bucket Polcies preferable to ACLs in S3?**

-> `human-readable syntax`

- **What are CloudFront Origins?**

-> `the resource to be hosted behind CloudFront`

- **What are the two primary methods of identifying public S3 buckets?**

-> `Search Engine INdexing and DNS Recon`

- **What subdomain did we identify by seraching certificates at crt.sh?**

-> `assets.bestcloudcompany.org`

- **What AWS CLI command can you run to dump an S3 bucket in its entirety?**

-> `aws s3 sync`

