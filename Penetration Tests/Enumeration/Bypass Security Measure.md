## Firewall and IDS/IPS Evasion
- When a port is filtered, it measn there is firewal within the network preventing the scan. Hence, we need to use ACK scan (-sA) 
```
nmap $IP -sA -Pn -n  -p-
```

## Determine Firewall and their Rules
--------------------------
- We need to look for errors when performing scans
- SYN-Scan
```
sudo nmap $IP -p 21,22,25 -sS -Pn -n --disable-arp-ping --packet-trace

```shell-session
Starting Nmap 7.80 ( https://nmap.org ) at 2020-06-21 14:56 CEST
SENT (0.0278s) TCP 10.10.14.2:57347 > 10.129.2.28:22 S ttl=53 id=22412 iplen=44  seq=4092255222 win=1024 <mss 1460>
SENT (0.0278s) TCP 10.10.14.2:57347 > 10.129.2.28:25 S ttl=50 id=62291 iplen=44  seq=4092255222 win=1024 <mss 1460>
SENT (0.0278s) TCP 10.10.14.2:57347 > 10.129.2.28:21 S ttl=58 id=38696 iplen=44  seq=4092255222 win=1024 <mss 1460>
RCVD (0.0329s) ICMP [10.129.2.28 > 10.10.14.2 Port 21 unreachable (type=3/code=3) ] IP [ttl=64 id=40884 iplen=72 ]
RCVD (0.0341s) TCP 10.129.2.28:22 > 10.10.14.2:57347 SA ttl=64 id=0 iplen=44  seq=1153454414 win=64240 <mss 1460>
RCVD (1.0386s) TCP 10.129.2.28:22 > 10.10.14.2:57347 SA ttl=64 id=0 iplen=44  seq=1153454414 win=64240 <mss 1460>
SENT (1.1366s) TCP 10.10.14.2:57348 > 10.129.2.28:25 S ttl=44 id=6796 iplen=44  seq=4092320759 win=1024 <mss 1460>
Nmap scan report for 10.129.2.28
Host is up (0.0053s latency).

PORT   STATE    SERVICE
21/tcp filtered ftp
22/tcp open     ssh
25/tcp filtered smtp
MAC Address: DE:AD:00:00:BE:EF (Intel Corporate)

Nmap done: 1 IP address (1 host up) scanned in 0.07 seconds
```

- ACK-Scan
```
sudo nmap $IP -p 21,22,25 -sA -Pn -n --disable-arp-ping --packet-trace
```
```shell-session
Starting Nmap 7.80 ( https://nmap.org ) at 2020-06-21 14:57 CEST
SENT (0.0422s) TCP 10.10.14.2:49343 > 10.129.2.28:21 A ttl=49 id=12381 iplen=40  seq=0 win=1024
SENT (0.0423s) TCP 10.10.14.2:49343 > 10.129.2.28:22 A ttl=41 id=5146 iplen=40  seq=0 win=1024
SENT (0.0423s) TCP 10.10.14.2:49343 > 10.129.2.28:25 A ttl=49 id=5800 iplen=40  seq=0 win=1024
RCVD (0.1252s) ICMP [10.129.2.28 > 10.10.14.2 Port 21 unreachable (type=3/code=3) ] IP [ttl=64 id=55628 iplen=68 ]
RCVD (0.1268s) TCP 10.129.2.28:22 > 10.10.14.2:49343 R ttl=64 id=0 iplen=40  seq=1660784500 win=0
SENT (1.3837s) TCP 10.10.14.2:49344 > 10.129.2.28:25 A ttl=59 id=21915 iplen=40  seq=0 win=1024
Nmap scan report for 10.129.2.28
Host is up (0.083s latency).

PORT   STATE      SERVICE
21/tcp filtered   ftp
22/tcp unfiltered ssh
25/tcp filtered   smtp
MAC Address: DE:AD:00:00:BE:EF (Intel Corporate)

Nmap done: 1 IP address (1 host up) scanned in 0.15 seconds
```


## Detect IDS/IPS
- To detect the existence of IDS/IPS, we need first to perform the scan on 1 VPS. If we no longer get access to the network-> we're blocked-> confirmed.
- Use Decoys options in NMAP (-D)
```
nmap $IP -p 80 -sS -Pn -n -D RND:5
	-D RND:5 --- Generate five random IP addresses that indicates the source IP the connection comes from.
```
- Another way is to manullay specify the source IP, using the (-S):
```
	# Test the Firewall Rule
	nmap $IP -Pn -n -p445 -O

	# Scan by Using Different Source IP
	nmap 10.129.2.28 -Pn -n -p 445 -O -S 10.129.2.200 -e tun0
		-S: Scans the target using different source IP Address
		10.129.2.200: the specified source IP address
		-e tun0: Sends all request through the sepcified interface
```

## DNS Proxy
------------------------------------
- We can use TPC port 53 as a source port for  our scan
```
	# Regular SYN-Scan of a filterd port
	sudo nmap 10.129.2.28 -p50000 -sS -Pn -n --disable-arp-ping --packet-trace
	
	Starting Nmap 7.80 ( https://nmap.org ) at 2020-06-21 22:50 CEST
	SENT (0.0417s) TCP 10.10.14.2:33436 > 10.129.2.28:50000 S ttl=41 id=21939 iplen=44  seq=736533153 win=1024 <mss 1460>
	SENT (1.0481s) TCP 10.10.14.2:33437 > 10.129.2.28:50000 S ttl=46 id=6446 iplen=44  seq=736598688 win=1024 <mss 1460>
	Nmap scan report for 10.129.2.28
	Host is up.
	
	PORT      STATE    SERVICE
	50000/tcp filtered ibm-db2
	
	Nmap done: 1 IP address (1 host up) scanned in 2.06 seconds


	# SYN-Scan from DNS Port
	sudo nmap 10.129.2.28 -p50000 -sS -Pn -n --disable-arp-ping --packet-trace --source-port 53

	SENT (0.0482s) TCP 10.10.14.2:53 > 10.129.2.28:50000 S ttl=58 id=27470 iplen=44  seq=4003923435 win=1024 <mss 1460>
	RCVD (0.0608s) TCP 10.129.2.28:50000 > 10.10.14.2:53 SA ttl=64 id=0 iplen=44  seq=540635485 win=64240 <mss 1460>
	Nmap scan report for 10.129.2.28
	Host is up (0.013s latency).
	
	PORT      STATE SERVICE
	50000/tcp open  ibm-db2
	MAC Address: DE:AD:00:00:BE:EF (Intel Corporate)
	
	Nmap done: 1 IP address (1 host up) scanned in 0.08 seconds
```
- Now we learned firewall accepts TCP port 53, it is likely the same case for IDS/IPS. We can check:
```
nc -nv --source-port 53 $IP 50000
```

## DNS Find DNS version
```
sudo nmap -sSU -p 53 --script dns-nsid $IP
```