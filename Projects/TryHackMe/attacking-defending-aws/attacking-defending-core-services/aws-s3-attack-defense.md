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

# ANSWER THE QUESTIONS
- **What is the name of the file storage container where you keep your data in S3?**

-> `bucket`

- **What characteristic makes Bucket Polcies preferable to ACLs in S3?**

-> `human-readable syntax`

- **What are CloudFront Origins?**

-> `the resource to be hosted behind CloudFront`

