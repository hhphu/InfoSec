# Automate servers deployment with Ansible
![](https://www.redhat.com/rhdc/managed-files/ansible/Ansible_and_MicrosoftAzure.png)


- This is my personal projects in which I use Microsoft Azure and Ansible to deploy multiple DVWA web servers.
- The purpose of this project is to get familiar with Microsoft Azure and its services while building a secure system on the Cloud platform. Here's the architecture of the project:



#### Setting up the Resource Group

[Resource Group and Virtual Networking](./resource-group-virtual-network.md)

---

#### Setting up a Network Security Group:

[Network Security Group](./network-security-group.md)

---

#### Setting up Virtual Machines

[Virtual Machine Setup](./virtual-machine-setup.md)


#### Setting up your Jump Box Administration

[Jump Box Administration](./jump-box-administration.md)
---

#### Docker Container Setup

[Docker Container Setup](./containers.md)

---

#### Setup your Provisioner

[Provisioner Setup](./provisioners.md)

---

#### Setup your Ansible Playbooks

[Ansible Playbook Setup](./ansible-playbook-setup.md)


---

#### Setting up the Load Balancer

[Setting up Load balancer](./load-balancer-setup.md)

---

#### Setting up the NSG to expose port 80

 [Setting up NSG Rule for DVWA Webservers](./security-configuration.md)
 
**Note:** With the stated configuration, you will not be able to access these machines from another location unless the security Group rule is changed.

---
#### END


