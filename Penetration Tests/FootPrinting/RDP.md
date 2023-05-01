- Footprinting the Service
```bash
sudo nmap -sV -sC $IP -p3389 --script rdp*
```

- To track individual packages
```bash
sudo nmap -sV -sC $IP -p3390 --script rdp* --packet-trace --disable-arp-ping
```

### RDP Security Check
```bash
# Installation
sudo cpan
git clone https://github.com/CiscoCXSecurity/rdp-sec-check.git && cd rdp-sec-check
./rdp-sec-check.pl $IP

# Initiate an RDP Session
xfreedp /u:$user /p:$pass /b:$IP
```
