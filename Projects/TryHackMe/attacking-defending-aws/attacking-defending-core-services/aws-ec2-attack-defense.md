# Amazon EC2: Attacks & Defense

## Ways to connect to EC2
### EC2 Connect
- Select the instance and click **Connect**

![7d0a5b956d2d038bd638c2e05d73e5f7](https://github.com/user-attachments/assets/70fdb8bc-e291-4932-8ce3-a60425a85d44)

- **EC2 Instance Connect** is the first option. When clicking **Connect** button, we will be logged in as the default username dispalyed in this tab.

![9823afab2ed71b05b9b75c241c01f215](https://github.com/user-attachments/assets/f051ae45-983b-49f7-ac02-c04ce75c4663)

General URL for Instance Connect **`https://console.aws.amazon.com/ec2/v2/connect/$USERNAME/$INSTANCE_ID`**

### AWS SSM
- SSN stands for Simple Systems Manager: allow users to install a package or run a command on Linux/Windows server.
- AWS Systems Manager Session Manager is another capability that allows users to connect to EC2 instance.

![cd3359835859b8e9ba3f758b5634bfdd](https://github.com/user-attachments/assets/e2ef7a42-84a5-4fcf-b8c6-c10d17920739)

### Serial Console
- A new feature of AWS to connect to EC2 intances
- Must be enabled by administrators and the user within the EC2 instance must have passowrd configured in `/etc/passwd`.


### ANSWER THE QUESTIONS
**- Connect to your EC2 Instance via Instance Connect. Run the id command, and answer what user you're logged in as:**

1. In the EC2 dashboad, selet the instance and click **Connect** button.

![image](https://github.com/user-attachments/assets/2ccac66c-4b10-45f2-867e-0eadc90ee650)

2. On the next page, click **Connect** button.

![image](https://github.com/user-attachments/assets/5e79053e-797e-4529-a92a-369b48a9c173)

Run the command `whoami` and we get the id.

-> `ec2-user`

**- Now connect via SSM Session Manager. Run the id command. What user are you connected as?**

Similar to the above steps, however, in step 2, select **Session Manageer** tab and click **Connect** button.

Run the command `whoami` and we get the id.

-> `ssm-user`

**- Using either the Instance Connect or SSM Session Manager session, run "sudo passwd root" and set a password for the root user. Can you now log in with the EC2 Serial Console? (Yea or Nay)**

-> `yea`


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

## EC2 Networking & Storage
- EC2 Networking revolves around **Elastic Network Interface (ENI)**. Each EC2 instance has at least 1 ENI, which has at least 1 Security Group attached to it. We can try the following command

```bash
aws ec2 describe-network-interfaces | jq '.NetworkInterfaces[0]'
```

![image](https://github.com/user-attachments/assets/67e65889-db9d-42e1-82c5-26e083e1f7fb)

- EC2 Storage uses **Amazon Elastic BLock Store (EBS)** as the hard disk storage for EC2 instances.

```bash
aws ec2 describe-snapshots --snapshot-ids $SNAP_ID
```
![image](https://github.com/user-attachments/assets/395c4c22-0d7f-4c02-9e06-c8eadb1c0c9c)

- From the above screenshot, we see there are two important pieces of information: the volume is not encrypted and the Owner's id is `019181489476`.
- To create a volume from this snapshot, we need the AZ to be in the same region as the EC2 machine's.

```bash
TOKEN=`curl -s -X PUT "http://169.254.169.254/latest/api/token" -H  "X-aws-ec2-metadata-token-ttl-seconds:21600"`

curl -s -H "X-aws-ec2-metadata-token:$TOKEN" http://169.254.169.254/latest/meta-data/placement/availability-zone
```

- Once obtaining the AZ, we can preoceed to create the volume from the snapshot

```bash
aws ec2 create-volume --snapshot-id $SNAP_ID --volume-type- gp3 --region $REGION --availability-zone $REGION
```

![image](https://github.com/user-attachments/assets/49d91901-e1ef-4908-a493-89fe81713e22)

-We'll get the Volume ID, which can be used to attach to our instance:

```bash
# Retrieve Instance ID
instance_id=$( curl -H "X-aws-ec2-metadata-token: $TOKEN" -s http://169.254.169.254/latest/meta-data/instance-id)

# Attacht the Volume to the instance
aws ec2 attach-volume --region $REGION --device /dev/sdh --instance-id $instance_id --volume-id $VOLUME_ID 
```

- Run `sudo fdisk -l` to confirm the volume has been attached.\

  ![image](https://github.com/user-attachments/assets/157c8acd-193f-4541-adb3-1ae1118dfd3e)

- Mount the disk:

```bash
sudo mkdir /snapshot-recovery
sudo mount /dev/nvme1n1 /snapshot-recovery
ls /snapshot-recovery
cat /snapshot-recovery/flag.txt
```

![image](https://github.com/user-attachments/assets/49e0eda7-65ff-4c5d-9657-e6aebd2b3ed3)

## EC2 Configuration
- Retrieve AMI information

```bash
aws ec2 describe-images --owners $OWNER_ID
```

![image](https://github.com/user-attachments/assets/8d14c817-f79f-43bf-b763-cd9c984fecc5)


- UserData allows uers to configure EC2 instances at launch (customize environments, settings, etc.)
- If UserData starts with `#!/bin/bash`, it is considered a script and will be executed by [cloud-init](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html)
- To get the user-datam, run:

```bash
curl -s -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/user-data
```

OR

look in `/var/lib/cloud/instance/scripts/part-001`

- SImilar to the above cases, we need to request a token to retrieve any information

```bash
TOKEN=$( curl -s -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds:21600")

instance_id=$(curl -H "X-aws-ec2-metadata-token: $TOKEN" -s http://169.254.169.254/latest/meta-data/instance-id)

aws ec2 describe-instance-attribute --attribute userData --instance-id $instance_id --region us-east-1 --query UserData --output text | base64 -d
```

![image](https://github.com/user-attachments/assets/8b3d23e1-da72-499a-ac30-96d5ce242030)






  
