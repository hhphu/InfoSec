------------ 
# Windows
------------------------------
### Invoke-AESEncryption.ps1
```PowerShell
Import-Module .\Invoke-AESENcryption.ps1
Invoke-AESEncryption.ps1 -Mode Encrypt -Key "p4ssw0rd" -Path .\scan-results.txt
```

----------------------
# Linux
-----------------
### openssl
```bash
# Encrypt the file
openssl enc -aes256 -iter 100000 -pbkdf2 -in /etc/passwd -out passwd.enc

# Decrypt the file
openssn enc -d -aes256 -iter 100000 -pbkdf2 -in passwd.enc -out passwd
```