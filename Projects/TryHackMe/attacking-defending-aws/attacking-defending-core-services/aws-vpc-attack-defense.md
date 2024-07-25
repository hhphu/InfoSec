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

## VPC Wormholes (Endpoints & PrivateLink)
- For resources in VPC to communicate with those outside the VPC, there are two services: VPC Endpoints & [AWS PrivateLink](https://aws.amazon.com/privatelink/?privatelink-blogs.sort-by=item.additionalFields.createdDate&privatelink-blogs.sort-order=desc).
### VPC Endpoints 
- Works with S3 and DynamoDB
- Is put in place to allow resources in the private subnets to have access to S3 without using NatGateway.
- Requires a route in VPC Route Tables.
- [Managed Prefix List](https://docs.aws.amazon.com/vpc/latest/userguide/managed-prefix-lists.html): The destination route is in abstract representation of the services, which is used to map the CIDR ranges wihtin the VPC. This is what a Managed Prefix List looks like.

![a50703faa70b14794ebd58fedace9acb](https://github.com/user-attachments/assets/de105401-e7de-4b8f-a144-a16186720b1f)

- To see the CIDR ranges for different services, run the command:

```bash
aws ec2 describe-prefix-lists
```
![image](https://github.com/user-attachments/assets/39f00329-d08b-4718-a07f-d17c24f5dbad)

**TIPS:** As an attacker, you can add an VPC endpoint as a way to exfiltrate data from a VPC into an S3 bucket that we have control of.

### VPC PrivateLink
- ENI in the VPC tied to an AWS service/AWS customer.
- Provides AWS/its partners to offer services to AWS customers without allowing traffic out to the Internet. This is what a PrivateLink list looks like

![fc50dacdf4a1dab36649811899c85757](https://github.com/user-attachments/assets/a63ac316-cc0e-4337-a172-80d86a5764f9)

## DNS in a VPC
- By default, instances in VPC use Amazon-provided DNS server, which always base of the VPC IPv4 network ranges.
- Customized DNS can be achived through AWS Route 53.
- You can configure the Route 53 Resolver DNS Firewall and Resolver Query Logging to CloudWatch Logs as a protection measure. 

## VPC Monitoring
### VPC Flow Logs
- Log the packet headers but not their contents.
- The logs can be sent to CloudWatch Logs or S3 bucket.

```
2 123456789012 eni-abcdef 52.46.145.233 10.100.0.118 443 52688 6 21 7010 1637966883 1637966911 ACCEPT OK

2: the Flow Logs version
123456789012: AWS account
eni-abcdef: ENI identifier
52.46.145.233: Source IP
10.100.0.118: Destination IP
443: Source port
52688: Destincation port
6: Protocol number
21: Number of packets
7010: number of bytes
1637966883 & 1637966911: start & end time in Unix Epoch time
ACCEPT: the action
OK: log status
```

## VPC Interconnectivity
### Cloud-to-Ground Connectivity
- For enterprise, AWS provides an interconnection service called DirectConnect
- For companies with racks at specific data centers, AWS will run a fiber-line from their cage to the companie's router, giving them a dedicated link to the VGW in the VPC.
- AWS Site-to-Site VPN is for smaller organizations that don't need the level of bandwitdh/latency that DirectConnect offers.
  1. Configure a [Customer Gateway](https://us-east-1.console.aws.amazon.com/vpcconsole/home?region=us-east-1#CustomerGateways:) which defines the endpoint AWS Site-to-Site VPN will connect to
  2. Createa a VPN connection that links the Customer Gateway with the Virtual Private Gateway (VGW).
    
  ![vpn-basic-diagram](https://github.com/user-attachments/assets/0b52a028-3cd8-4107-aa98-92c9eecd5039)

- Both DirectConnect and AWS Site-to-Site VPN require a route in the Route Table
- For attackers: this is a great place to pivot from cloud to on-premise infrastructure
- For defenders: ensure that all traffics from both services terminate at a firewall and set least-privilege firewall rules.
- For compliance expert: DirectConnect's traffics are not encrypted.

### Cloud-to-Cloud Connectivity
- Companies usually separate development and production environments. When different teams need to communicate with each other, there are several means:
  - **VPC Peering**:
    - Allows VPC to communicate with other VPCs, which works accross accounts and regions.
    - VPCs can reference each other's Security Groups -> allow data replication for disaster recovery setup
    - Require routings in Route Table
    - VPC Peering is not transitive. If VPC-A has peered to VPC-B, and VPC-B has peered to VPC-C, there is no network path for a machine in VPC-A to talk directly to an IP Address in VPC-C. 
      
      ![d76d5d0fa20940b4b477067a1fe42151](https://github.com/user-attachments/assets/0a937f64-fe5b-4691-82dd-927c1b4d4e8d)
  - **AWS Transit Gateway**: allows VPCs to interconnect with each other and supports DirectConnect and Site-to-Site VPN

### Client VPN
- This is a surface attackers can bypass and abuse privilege account to access on-premise infrastructure.

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

- **You have a VPC Endpoint in your VPC. What is the destination in the route table?**

In the **Route Table**, in both _VPCRoom-PublicRouteTable_ & _VPCRoom-PrivateRouteTable_, we see there's a Managed Prefix Lists called **pl-63a5400a**. This is the destination of the VPC Endpoint in the Route table.

![image](https://github.com/user-attachments/assets/2121c5be-acd9-47a5-b2e4-5e73943ac716)

-> `pl-63a5400a`

- **What is the service name for the VPC Endpoint?**

![image](https://github.com/user-attachments/assets/589b637e-fe78-4b02-a768-40447de902bc)

-> `com.amazonaws.us-east-1.s3`

- **What is the IP address of the "task6.vpcroom.tryhackme.com" entry in the Route53 Console?**

![image](https://github.com/user-attachments/assets/977c1054-2c1d-4b04-9223-6c356fdabbfe)

-> `169.254.169.254`

- **Go visit the CloudWatch Logs page. What is the name of the log group with the VPC Flow Logs?**

![image](https://github.com/user-attachments/assets/6ba30a14-6a35-4c17-aae8-4b2f9084e367)

-> `/aws/vpcFlowLogs/VPCRoom`

- **Can you find the IP address of the customer gateway for the VPN defined in your account?**

![image](https://github.com/user-attachments/assets/0367e994-94f6-4b98-9c08-2dab053c4b8c)

-> `198.54.117.215`

- **What is the routing target prefix for the VPC Peering connection?**

Google it and we'll find the answer.

-> `pcx-`
