## HOST DISCOVERY
----------------------------------------------------
- NMAP
```shell-session
  -sS/sT/sA/sW/sM: TCP SYN/Connect()/ACK/Window/Maimon scans
  -sU: UDP Scan
  -sN/sF/sX: TCP Null, FIN, and Xmas scans
  --scanflags <flags>: Customize TCP scan flags
  -sI <zombie host[:probeport]>: Idle scan
  -sY/sZ: SCTP INIT/COOKIE-ECHO scans
  -sO: IP protocol scan
  -b <FTP relay host>: FTP bounce scan
```
- Scanning Network Range
```
nmap 10.10.10.0/24 -sn -oA tnet | grep for | cut -d" " -f5
	-sn: disable port scanning
	-oA: Store the results in all formats starintg with the name 'tnet'
```

- Scan IP list 
```
nmap -sn -oA tnet -iL hosts.list | grep for | cut -d" " -f5
	-iL: Perform defined scans against targets provided in the file
```

- Scann a single IP
```
nmap 10.10.10.10 -sn -oA host -PE --reason
	-sn: disable port scanning
	-oA: Store the results in all formats starting with the name "host"
	-PE: Perform the ping scan by using ICMP echo requests against the target
	--reason: display the reason for sepcific result.
```

## HOST & PORT SCANNING
--------------------------------------------------------
- Discover open TCP Ports
```
nmap 10.10.10.10. --top-ports=10
```
- Trace the packets
```
nmap $IP -p 21 --packet-trace -Pn -n --disable-arp-ping
```

## SAVING THE RESULT
-------------------
- Saving the result in xml 
```
nmap $IP -oX target.xml
```
- Create HTML report to read
```
xsltproc target.xml -o target.html
```

## SERVICE ENUMERATION
------------------------------
- Banner Grabbing
```
nmap -sV -p- $IP
```
- When nmap does not show information of a service, we need to manually connect to the service to obtain information
```
nc -lv $IP <PORT>
```