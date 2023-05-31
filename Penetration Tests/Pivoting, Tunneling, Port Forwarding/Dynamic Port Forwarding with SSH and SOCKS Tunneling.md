# SSH Local Port Forwarding
- Execute Local Port Forwarding
```bash
ssh -L 1234:localhost:3306 $USER@$PIVOT_HOST

# For multiple port forwarding
ssh -L 1234:localhost:3306 8080:localhost:80 $USER@PIVOT_HOST
```

- Confirm Port Forwarding with netstat
```bash
netstat -antp | grep 1234
netstat -antp | grep 8080
```

- Confirm Port Forwarding with nmap
```bash
nmap -v -sV -p1234,8080 localhost
```

# Set up to Pivot
- Enabling Dynamic Port Forwarding with SSH
```bash
ssh -D 9050 $USER@PIVOT_HOST
```

- Checking with /etc/proxychains.conf
```bash
tail -4 /etc/proxychains.conf
```

- Using Nmap with Proxychains
```bash
proxychains nmap -v -sn $IP
```

- Enumerate Target Hosts with proxychains
```bash
proxychains nmap -A $IP
```

- Use Metasploit with proxychains
```bash
proxychains msfconsole

# user rdp_scanner
serach rdp_scanner
```

- Use xfreerdp with proxychains
```bash
proxychains xfreerdp /v:$IP /u:$USER /p:$PASS
```



