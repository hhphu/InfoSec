--------------
# WinRM
-----------------------
## CrackMapExec
- Installing CrackMapExec
```bash
sudo apt-get -y install crackmapexec
```
- Usage
```bash
crackmapexec <proto> <target-IP> -u <user or userlist> -p <password or passwordlist>

# crackmapexec winrm $IP -u user.list -p password.list
```

## Evil-WinRM
- Installing Evil-WinRM
```bash
sudo gem install evil-winrm
```
- Usage
```bash
evil-winrm -i $TARGET -u $USERNAME -p $PASSWORD

```
