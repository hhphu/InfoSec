---------------
# Enumerate Windows 
-----------------------
- Ping host
- OS Detect scan
```bash
sudo nmap -v -O $IP
```
- Banner Grab to enumerate ports
```bash
sudo nmap -v $IP --script banner.nse
```

--------------------------
# Payloads Types
------------------------------
- DLLs - Dynamic Linking Library: Used to provide shared code and data for applications and processes.
- Batch: DOS scripts utilized by sys admin to complete multiple tasks through command lines.
- VBS: lightweight scripting language based on Microsoft's Visual Basic, client side language which has been outdated
- MSI: serv as an installation database for Windows Installer. 
- Powershell

## Payload Generation
- MSFVenom & Metasploit Framework
- Payloads All The Things
- Mythic C2 Framework
- Nishang
- Darkarmour

## Payload Transfer & Execution
- Impacket
- Payloads All The Things
- SMB
- Remote execution via MSF
- Other protocols: FTP, TFTP, HTTP