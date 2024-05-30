## Solution Guide: Virtual Computing

The goal of this activity was to set up your first virtual machine inside your cloud network, which is protected by your network security group. You will use this machine as a jump box to access your cloud network and any other machines inside your VNet.

---

Remember: Allowing a server to use password authentication for SSH is insecure because the password can be brute forced.

- Therefore, we will only use cryptographic SSH keys to access our cloud servers. Password authentication will not be allowed. 

- This is part of the "ground up" security approach that we have been discussing. 

Open your command line and run `ssh-keygen -t rsa` to create a new SSH key pair.

- Your output should be similar to:

    ```bash
    cyber@2Us-MacBook-Pro ~ % ssh-keygen -t rsa
    Generating public/private rsa key pair.
    Enter file in which to save the key (/Users/cyber/.ssh/id_rsa):
    Enter passphrase (empty for no passphrase): 
    Enter same passphrase again: 
    Your identification has been saved in id_rsa.
    Your public key has been saved in id_rsa.pub.
    The key fingerprint is:
    SHA256:r3aBFU50/5iQbbzhqXY+fOIfivRFdMFt37AvLJifC/0 cyber@2Us-MacBook-Pro.local
    The randomart image is:
    +---[RSA 2048]----+
    |         .. . ...|
    |          o. =..+|
    |         o .o *=+|
    |          o  +oB+|
    |        So o .*o.|
    |        ..+...+ .|
    |          o+++.+ |
    |        ..oo=+* o|
    |       ... ..=E=.|
    +----[SHA256]-----+
    ```

Run `cat ~/.ssh/id_rsa.pub` to display your `id_rsa.pub` key:

- Your output should be similar to:

    ```bash
    cyber@2Us-MacBook-Pro ~ % cat ~/.ssh/id_rsa.pub 

    ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDGG6dBJ6ibhgM09U+kn/5NE7cGc4CNHWXein0f+MciKElDalf76nVgFvJQEIImMhAGrtRRJDAd6itlPyBpurSyNOByU6LX7Gl6DfGQKzQns6+n9BheiVLLY9dtodp8oAXdVEGles5EslflPrTrjijVZa9lxGe34DtrjijExWM6hBb0KvwlkU4worPblINx+ghDv+3pdrkUXMsQAht/fLdtP/EBwgSXKYCu/
    ```

- Highlight and copy the SSH key string to your clipboard. 

#### VM 1 – Jump Box

Open your Azure portal and search for "virtual machines."

- Use the **+ Add** button or the **Create virtual machine** button to create a new VM.

    ![](../../../Images/VM/CreateVM-b.png)

Use the following settings for this VM: 

- Resource group: Choose the same resource group that you created for the Red Team.

- VM name: Use the name "JumpBoxProvisioner."

- Region: Use the same region that you used for your other resources.

	- Note that availability of VMs in Azure could cause you to change the region where your VMs are created.

	- The goal is to create three machines in the same resource group attached to the same security group. If you cannot add three machines to the resource group and security group that you have, a new resource group and security group may need to be created in another region.

- Availability options: We will use this setting for other machines. For our jump box, we will leave this on the default setting.

- Image: Choose the Ubuntu Server 20.04 option.

- Choose the VM option that has:

  - Its offering set as **Standard - B1s**

  - 1 CPU

  - 1 GB RAM

For SSH, use the following settings: 

- Authentication type: SSH public key.

- Username: Create any username you like.

- SSH public key: Paste the public key string that you copied earlier.

- Public inbound ports: Ignore this setting. It will be overwritten when you choose your security group.

- Select inbound ports: Ignore this setting. It will be overwritten when you choose your security group.

![](../../../Images/Jump_box-VM.png)

Move to the **Networking** tab and set the following settings:

- Virtual network: Choose the VNet you created for the Red Team.

- Subnet: Choose the subnet that you created earlier.

- Public IP: Choose `Create new` and choose `Static` under Assignment in the side panel. Give the IP Address a unique name.

![](../../../Images/VM/Static-IP.png)

- NIC network security group: Choose the "Advanced" option so we can specify our custom security group.

- Configure network security group: Choose your Red Team network security group.

- **Recommended** Check the box to Delete public IP and NIC when VM is deleted.  If you have to delete the VM later, this will prevent extra IPs from appearing

- Accelerated networking: Keep as the default setting (Off).

- In the Networking settings, take note of the VM URL. You may use it later.

- Load balancing: Keep as the default setting (No).

    ![](../../../Images/JumpBoxNetwork.png)

- Click on **Review + create**.

    ![](../../../Images/VM/FinalizeVM.png)

- Finalize all your settings and create the VM by clicking on the **Create** button.

#### VMs 2 and 3 – Web VMs

Create two more new VMs. Keep the following in mind when configuring these VMs:

- Each VM should be named "Web-1" and "Web-2."

- These VMs need to be in the same resource group you are using for all other resources.

- The VMs should be located in the same region as your resource group and security group.

	- Note that availability of VMs in Azure could cause you to change the region where your VMs are created.

	- The goal is to create three machines in the same resource group attached to the same security group. If you cannot add three machines to the resource group and security group that you have, a new resource group and security group may need to be created in another region.

- The administrative username should make sense for this scenario. You should use the same admin name for all three machines. Make sure to take a note of this name as you will need it to login later.

- You will need to create a new SSH key for remote connections. 

	- **Note:** Windows users should use [GitBash](https://gitforwindows.org/) to create ssh keys and ssh connections.

- Choose the VM option that has:

  - Its offering set as **Standard - B1ms**

  - 1 CPU

  - 2 GB RAM

**Note:** These web machines should have **2 GB** of RAM and the Jump-Box only needs **1 GB**. All 3 machines should only have **1 vCPU** because the free Azure account only allows **4 vCPUs** in total per region.

**Important:** Make sure both of these VMs are in the same availability Set. Under Availability Options, select "Availability Set." Click on "Create New" under the Availability set. Give it an appropriate name. After creating it on the first VM, choose it for the second VM.

![](../../../Images/AvailabilitySet.png)

In the **Networking** tab and set the following settings:

- Virtual network: Choose the VNet you created for the Red Team.

- Subnet: Choose the subnet that you created earlier.

- Public IP: NONE! Make sure these web VM's do not have a public IP address.

![](../../../Images/WebVMNetworking.png)

- NIC network security group: Choose the Advanced option so we can specify our custom security group.

- Configure network security group: Choose your Red Team network security group.

- Accelerated networking: Keep as the default setting (Off).

- Load balancing: Keep as the default setting (No).

**NOTE:** Notice that these machines will not be accessible at this time because our security group is blocking all traffic. We will configure access to these machines in a later activity.

The final WebVMs should resemble the following:

![](../../../Images/Avail_Set/final-VM.png)

--- 

© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
