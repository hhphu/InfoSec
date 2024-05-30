Introduction
This is my personal projects in which I use Microsoft Azure and Ansible to deploy multiple DVWA web servers. The purpose of this project is to get familiar with Microsoft Azure and its services while building a secure system on the Cloud platform. Here’s the architecture of the project:

Ansible
Ansible is an open-source automation tool designed for configuration management, application deployment, and task automation, known for its simplicity and agentless architecture. Using plain YAML syntax, it allows users to define instructions in playbooks that can be executed across multiple machines via SSH, ensuring idempotency and consistency. Ansible’s modular design supports custom modules and plugins, with a vast library of pre-built options. It manages inventory through straightforward text files and scales easily from small to large infrastructures. Its ease of use, scalability, and strong community support make it a popular choice for automating complex IT tasks.
Projects Walkthrough
Create Resource Group
First we need to create the Resource Group, which groups all the resources required for this project.
As seen in the architecture, this Resource Group contains a virtual network, a virtual subnet with 1 Load Balancer and 4 virtual machines.
Steps to create a Resource Group
Search in Azure for “Resource Group”

2. Create a new Resource Group by naming it “DVWA-Servers”. Of course, you can name it whatever you want. For the region, select the region where you’re residing. in my case, it is West US 2.


3. Confirm the “DVWA-Servers” Resource Group is created.


Create Virtual Network
Virtual network contains a collection of virtual machines that can communicate with each other. On top of that is the load balancer, which is used to distribute the traffic amongst the DVWA servers.
Steps to create the Virtual Network
Search in Azure for “Virtual Network”

2. Create a virtual network with the name “DVWA-Servers-Network”. Also, make sure that in the security tab, we don’t have any of these options selected as they may cost you money: Azure Bastion, Azure Firewall or Azure DDoS Network Protection


3. For the IP address tab, we leave everything as default.


4. Review and Create the network. Confirm the network once it’s created.


Configure Network Security Group
The next step is to create Security Group for the network, which acts as a firewall that allows/blocks traffics based on the rules set.
Steps to create Network Security Group
Search for Network Security Group. Remember NOT to select the classic one.

2. Create a new Network Security Group (NSG) with the name “DVWA-Servers-NSG”. Make sure that the Resource Group is DVWA-Servers.


3. Confirm the NSG is created.


Reviewing the NSG, we see there are some default rules

The first rule allows all traffic to flow inside the vNet with destination and source both set to “Internal Network.”, i.e all the virtual machines within the network will be able to communicate with each other.
The second rule allows all traffic coming from a load balancer, meaning if there were a load balancer assigned to this security group, it could send traffic to all the resources on the internal network.
The final rule blocks all inbound & outbound traffics.
For now, we leave the NSG as is. Once we create virtual machine, we can configure these rules.
Create Virtual Machine
Next we create a virtual machine that installs Ansible.

Create a new Virtual machine with the following information:

Resource Group: DVWA-Servers
Virtual Machine Name: azureuser
Region: US West 2
Image: Ubuntu Server 22.04 LTS -x64 Gen2
Size: choose the machine that has 1 vCPU and 1GB of memory. The reason is because free tier users only have 4 vCPUs per region. From the diagram, we have 4 VMs, meaning each of them can only have 1 vCPU.
Note: sometimes, the sizes are not available. We have to switch around the regions to find the size.

SSH Setup
Now we have to set up SSH key to access the Ansible-VM. First, in our machine, run ssh-keygen -t rsa. For Windows, we should run the command in Git Bash.

Once the key-pair is created, we can copy the public key (cat ~/.ssh/id_rsa.pub)

Paste it into the SSH Public Key Source field. The username can be any name.

. Review and create the machine. We now have successfully created a Virtual Machine for Ansible.

Create 3 Web servers

Similar to the above steps, we need to create 3 more VMs, whose names are web-1, web-2 and web-3 .
Make sure they’re all under the same Resource Group and Network.
Check List
Now, before moving on to the next steps, we need to make sure all required resources are created

1 Ansible VM with 1 vCPU and maximum 1 GB
3 web servers VM with 1 vCPU and maximum 1 GB each.
SSH key with no password for each VM.
All 4 VMs are using the same security group and vNet.
Install Ansible in Ansible-VM
I will be running Ansible via docker containers.
Steps of the walkthrough:

SSH into the Ansible-VM machine ssh azureuser@$Anisble_VM_PUBLIC_IP
2. Once on the machine, update the latest image version sudo apt-get update

3. Install docker sudo apt install docker.io

4. Once docker is installed, pull the following image: sudo docker pull $DOCKER_IMAGE_NAME .

5. Once the image is downloaded, run docker run -it $DOCKER_IMAGE_NAME bashto create a new container from the container image and have it set up to run a terminal for user interactions.


Now that we’re in the Ansible container, we need to set up SSH keys so it can communicate with the web servers.

Create SSH connection for web servers
Create SSH keys so the 3 web servers can communicate with the Ansible-VM machine: ssh-keygen -t rsa

2. In Microsoft Azure portal, go to one of the web server and update their SSH key. Paste the newly created SSH key in Ansible-VM.



3. Test the SSH connection: ssh web-1@$10.0.0.5 Note that in this case I use web-1’s private IP address.


From the above screenshot, we can confirm successful connection between the Ansible-VM and the web-1 server.
Configure Ansible

Go back to the Ansible-VM machine. Run ansible
root@9bd16493749f:~# ansible
usage: ansible [-h] [ - version] [-v] [-b] [ - become-method BECOME_METHOD]
 [ - become-user BECOME_USER] [-K] [-i INVENTORY] [ - list-hosts]
 [-l SUBSET] [-P POLL_INTERVAL] [-B SECONDS] [-o] [-t TREE] [-k]
 [ - private-key PRIVATE_KEY_FILE] [-u REMOTE_USER]
 [-c CONNECTION] [-T TIMEOUT]
 [ - ssh-common-args SSH_COMMON_ARGS]
 [ - sftp-extra-args SFTP_EXTRA_ARGS]
 [ - scp-extra-args SCP_EXTRA_ARGS]
 [ - ssh-extra-args SSH_EXTRA_ARGS] [-C] [ - syntax-check] [-D]
 [-e EXTRA_VARS] [ - vault-id VAULT_IDS]
 [ - ask-vault-pass | - vault-password-file VAULT_PASSWORD_FILES]
 [-f FORKS] [-M MODULE_PATH] [ - playbook-dir BASEDIR]
 [-a MODULE_ARGS] [-m MODULE_NAME]
 pattern
ansible: error: too few arguments
There are two tasks we need to perform: configure the usernames used to log in the web server machines & their IP addresses.
Ansible’s configuration file is located in /etc/ansible/ansible.cfg
Let’s configure the file: nano /etc/ansible/ansible.cfg. The remote_user option tells ansible which username should be used for web-1.
Make sure to set the remote_user to the username set for web-1 server (web-user)

Next we modify the hosts file, which tells Ansible which IP address to go to. We add web-1’s IP address (10.0.0.5) to the hosts file. Also remember to uncomment the [webservers]

Note: In order to make Ansible work, we have to create Python scripts and run them on the target machine. Now, to make sure that all target machines run the same version of Python, we add the following ansible_python_interpreter=/usr/bin/python3 next to the IP address we just add

Now that everything is set up, we can test the connection between the Ansible-VM machine and the target machine, web-1.
ansible all -m ping

-m: specify the module you want Ansible to run
ping: the name of the module we want to run
all: the group of machines you want to run the ping module on.
The output should look like this

We repeat the same steps for web-2 & web3 servers. Check the connections and the output should look like

Ansible Playbook
Now that we have successfully set up SSH connections, enter the Ansible container and create dvwa-servers-playbook.yml
Before getting started with the Ansible playbook, we should get familiar with these actions:
ansible.builtin.apt: The name of the module we are using. It is at the same indentation level as the name specification.

update_cache: yes: Runs the equivalent of sudo apt update to pull the most recent repositories.

state: The state of the package we want to install, which is either present or absent.
  If set to present, Ansible checks to see if the package is there. If it is there, Ansible does nothing. If it is not there, Ansible runs the command sudo apt install apache2 to install Apache2.
  If set to absent, Ansible checks for the package and runs sudo apt remove apache2 if Apache2 is there.
Here’s a break down of what the actions the playbook should be performing:
Declare the Yaml file:
#denote this is a yml file
---   

# name of the playbook
- name: Configure DVWA web server with Docker
  # groups of webservers that we run actions on
  hosts: webservers
  # This line means that all actions will be run as root on the server we are configuring. We must run items with root so we can install software and make system changes.
  become: true
  # lists of actions that will be performed.
  tasks:
2. Since DVWA server runs on port 80, we need to remove apache2 (which also runs on port 80) if it is installed.

  - name: Remove apache2 if it is installed 
    ansible.builtin.apt:
      update_cache: yes
      name: apache2
      state: absent
3. Install docker.io and python3-pip

---
- name: docker.io
  ansible.builtin.apt:
    update_cache: yes
    name: docker.io
    state: present

- name: Install pip3
  ansible.builtin.apt:
    # prevent the borken packages or missing dependencies
    force_apt_get: yes
    name: python3-pip
    state: present
4. Install docker module in Python so Ansible can manage docker containers.

---
- name: Install Python Docker module
  pip:
    name: docker
    state: present
5. Use Ansibledocker-container module to install the dvwa container. Make sure the port is 80

---
- name: Download and launch a docker web container
  docker_container: 
    name: dvwa
    image: vulnerables/web-dvwa
    state: started
    # ensure that the container restarts if you restart your web VM. Without it, you will have to restart your container when you restart the machine.
    restart_policy: always
    publish_ports: 80:80
6. Use systemd module to restart the docker service when the machine reboots

---
- name: Enable docker service
  systemd:
    name: docker
    enabled: yes
The complete playbook should look like
---
- name: Configure DVWA web servers with Docker
  hosts: webservers
  become: true
  tasks:
  
  - name: Remove apache2 if it is installed
    ansible.builtin.apt:
      update_cache: yes
      name: apache2
      state: absent

  - name: Install Docker 
    ansible.builtin.apt:
      update_cache: yes
      name: docker.io
      state: present

  - name: Install Python3-pip
    ansible.builtin.apt:
      force_apt_get:yes
      name: python3-pip
      state: present

  - name: Install Python's Docker module
    pip:
      name: docker
      state: present

  - name: Download and launch Docker web container
    docker_container: 
      name: dvwa
      image: vulnerables/web-dvwa
      stated: started
      restart_policy: always
      published_ports: 80:80

  - name: Enable Docker Service
    systemd:
      name: docker
      enabled: yes
Now we can run the playbook
ansible-playbook dvwa-web-servers-playbook.yml
A successful run will look like this

We now can log into the VMs to test the DVWA servers
SSH to one of the VM machine ssh webserver@10.0.0.5
Send a curl request curl localhost/setup.php
If we get a HTML response, the server is up and running as expected.

Load Balancing
What is a load balancer?
Load balancer not only distributes traffics across different web servers but also protects servers from DDoS attacks.
Load Balancer also has “health probe” function, which checks regularly to make sure all of the machines behind the load balancer are functioning before sending traffic to them. Machines with issues are reported, and the load balancers stop sending traffic to those machines.
Create a Load Balancer in Microsoft Azure
Under one of the web server, select Networking > Load Balancing. Select Add Load Balancing and create a new one.

Move to the Frontend IP configurations tab, create a new Frontend IP configuration
Name: DVWA-LB-Frontend
IP Version: IPv4
IP Type: IP address
Public IP address: Create a new one with the same name
  Name: DVWA-LB-Frontend
  Routing preference: Internet

Move to Backend Pool tab. Add a new one
Name: DVWA-LB-Backend
Virtual Network: $YOUR_VIRTUAL_NETWORK

In the IP Configuration section, add 3 virtual machines (web-1, web-2, web-3)

Skip to Review & Create tab and create the new Load Balancer.
Health Probe Configuration
Once the Load Balancer is created, go to the Health probes option and create a new one

Create a new health probe with the following information
Name: Give a unique name
Protocol: TCP
Port: 80
Interval: 5

Create Inbound Rule for Load Balancer
Go to the Load Balancer overview and select Load Balancing rules. Add a new rule

Create a Load Balancing rule based on the screenshot below

Create Security Group
This is to allow port 80 traffic from the Internet to our vNet

Verify we can access the web servers from our machine by entering the Load Balancer frontend IP address: http://http://20.33.46.77/setup.php

Conclusion
That’s it for the post today. I know this is a long project but hope you enjoyed it.
Please clap if you like this post and follow me for more Cybersecurity.