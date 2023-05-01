- Download all files from FTP
```shell
wget -m --no-passive ftp://anonymoous:anonymous@$IP
```

- To use nmap ftp script, we first need to update the db:
```shell
sudo nmap --script-udpatedb
```

- Perform the scan:
```
sudo nmap -sV -sC -A -p21 $IP
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