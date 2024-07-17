# Amazon EC2: Attacks & Defense

## Ways to connect to EC2
### EC2 Connect
- Select the instance and click **Connect**

![7d0a5b956d2d038bd638c2e05d73e5f7](https://github.com/user-attachments/assets/70fdb8bc-e291-4932-8ce3-a60425a85d44)

- **EC2 Instance Connect** is the first option. When clicking **Connect** button, we will be logged in as the default username dispalyed in this tab.

![9823afab2ed71b05b9b75c241c01f215](https://github.com/user-attachments/assets/f051ae45-983b-49f7-ac02-c04ce75c4663)

### AWS SSM
- SSN stands for Simple Systems Manager: allow users to install a package or run a command on Linux/Windows server.
- AWS Systems Manager Session Manager is another capability that allows users to connect to EC2 instance.

![cd3359835859b8e9ba3f758b5634bfdd](https://github.com/user-attachments/assets/e2ef7a42-84a5-4fcf-b8c6-c10d17920739)

## Instance Permissions
### Instance Metadata Service (IMDS)
- A way for EC2 instances to retrieve AWS credentials to interact with other AWS services.
- Listens to special IP Address: `169.254.169.254`
- IMDS was vulnerable, which caused the Capital One breach. Hence, IMDSv2 was introduced., which leverages a session-based approach to interactions with the Metadata services and requires both an HTTP PUT and an HTTP GET,.
- To retrieve credentials, we make an API call on `/security-credentials` endpoint, which requires the **role name**.
- To retrieve the role name, we run:

  ```bash
  role_name=$( curl -s http://169.254.169.254/latest/meta-data/iam/security-credentials)
  ```
- Now we can retrieve the session credentials for the role:

```bash
curl -s http://169.254.169.254/latest/meta-data/iam/security-credentials/${role_name}
```

- To enable IMDSv2, we do run the following commands:

```bash
# Get the Instance ID
instace_id=$( curl -s http://169.254.169.254/latest/meta-data/instance-id )

# Echo the Instance ID
echo "My INstance ID is ${instance_id}

# Update the Instace Metadata option to require a Token to make the instance metadata call
aws ec2 modify-instance-metadata-options --instance-id $instance_id --http-tokens required --region us-east-1
```

- To get credentials via the HTTP Token method:

```bash
# Request a token that will last 216000s (6h)
TOKEN= `curl -s -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds:21600"`
echo $TOKEN

# Retrieve the credentials
role_name = $( curl -s -H "X-aws-ec2-metadata-token:$TOKEN" http://169.254.169.254/latest/meta0data/iam/security-credentials/ )
curl -s -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/iam/security-credentials/${role_name}
```





  
