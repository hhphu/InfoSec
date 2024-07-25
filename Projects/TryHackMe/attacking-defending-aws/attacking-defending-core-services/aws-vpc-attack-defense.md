# AWS VPC - Attack and Defense
### AWS VPC - Attack and Defense

## AZs, Subnets, Route Tables
- Every VPC consists of AZs (availability zone), subnets and gateways (Internet Gateway & Virtual Private Gateway).
- Subnets: must use CIDR ranges and can't overlap.
- Internet Gateway & Virtual Private Gateway: IGW connects the VPC to the Internet while VPG connects the VPC to on-premise networks/infrastructure.
- The Route tables define the ingress and egress traffics of the VPC.

## NACLs & Security Groups
### Network Access Control Lists (NACLs) 
- Act as VPC firewalls. They are applied to subnets and stateless, meaning if an inbound connection is allowed, the outbound response must also be allowed.
- By default, NACLs have a "Deny All" rule.
  
![49a22c60a0563f0cc22b5ea72caaef10](https://github.com/user-attachments/assets/c2dca2f5-8089-4aef-bc1b-21adc69ddabf)

- From the above screenshot, the NACL prohibits all SSH traffic, then allows all other traffics. The final Deny rule is the default from AWS.

### Security Groups
- Are attached to resources (EC2 instances, RDS Database)  
- Are stateful, meaing if the inbound connection is allowed, the outbound is automatically allowed.
- Only support **Allow** actions.

   
# ANSWER THE QUESTIONS
- **What is the CIDR Range of the VPC named VPCRoom?**

-> `10.100.0.0/21`

- **For the VPC in your account, the Private Subnets have a route to a fictional on-prem network via a VGW. What is the CIDR Range of the fictional  on-prem network?**

Because the VGW connects VPC to on-premise network, the network is private. We can find all information about this private network from the Route tables.

![image](https://github.com/user-attachments/assets/fe3f71d3-4e0a-4903-b2b3-5b79e8df11d6)

-> `172.18.0.0/16`

- **What CIDR Range in the Security Group "VPCRoom-Instances" is Allowed to SSH?**

![image](https://github.com/user-attachments/assets/6e1d2a03-96c8-45fa-a5d1-6ae6a7e8af95)

-> `18.206.107.24/29`

- **What port range is permitted to the private subnets from the on-prem network range?**

![image](https://github.com/user-attachments/assets/f5194379-047c-4637-9c5d-b729f25063d3)

-> `22-443`

- **List the ENIs in your account. What is the description of the ENI with the IP Address 10.100.2.79?**

1. Run the command `aws ec2 describe-network-interfaces` and save it to a file
2. Open the file using nano or vim
3. From the editor, use the command search to locate where the IP address is. From here we can retrieve the description.

-> `Hardcoded DHCP Assignment`
