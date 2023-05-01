-------------------------
- R-Services are a suite of services hosted to enable remote access/issue commands between Unitx hosts over TCP/IP
- Span across the ports 512, 513 and 514
- The suite can be accessed via r-commands
- R-commands include:
	- rcp (remote copy) (#514)
	- rexec (remote execution) (#512)
	- rlogin (remote login) (#513)
	- rsh (remote shell) (#514)
	- rstat
	- ruptime
	- rwho (remote who)
--------------------------------------------------

- Scanning for R-Services
```bash
sudo nmap -sV -p 512,513,514 $IP
```

- Loggin in Using rlogin
```bash
rlogin $IP -l htb-student
```

- Listing Authenticated Users Using rwho
```bash
rwho
```

- Listing Authenticated Users using rusers
```bash
rusers -al $IP
```