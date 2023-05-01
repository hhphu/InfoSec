- Footprinting the service
```shell
sudo nmap $IP -sV -sC -p139,445
```

----------------------------------
### RPCclient
- Sometimes, nmap does not provide lots of information., use [RPC](https://www.geeksforgeeks.org/remote-procedure-call-rpc-in-operating-system/)
- Should be performed on top off nmap scan
```shell
rpcclient -U "" $IP

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

- RPCclient - Group Information
```
querygroup $GROUP_RID
```

- Imacket samrdump.py
```
samrdump.py $IP
```

---------
[SMBMap](https://github.com/ShawnDEvans/smbmap) & [CrackMapExec](https://github.com/Porchetta-Industries/CrackMapExec)
```shell
# log in
smbmap -H $IP
```

```shell
crackmapexec smb $Ip --shares -U '' -p ''
smbclient -U $USER \\\\$IP\\$share
```

---------------------------
[Enum4Linux-ng](https://github.com/cddmp/enum4linux-ng)
- Installation
```shell
git clone https://github.com/cddmp/enum4linux-ng.git
cd enum4linux-ng
pip3 install -r requirements.txt
```

- Enumeration
```
enum4linux-ng.py $IP -A
```