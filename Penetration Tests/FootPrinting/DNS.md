- FQDN: Fully Qualified Domain Name
| DNS Record | Description |
| ------------- | ------------- |
| A | Return an IPv4 address of the requested domain as a result |
| AAAA | Return an IPv6 of the requested domain |
| MX | Return the responsibl mail servers as a rulst |
| NS | Return the DNS servers of the domain |
| TXT | Contain various information. THe all-rounder can be used, e.g., to valildate SSL certificates, Google Search Console, etc.|
| CNAME | This serves as an alias. If the domain www.hackthebox.eu should point to the same IP, we create an A recod for one and CNAME record point for the other. |
| PTR | PTR records work the other way around ( reverse lookup, convert IP addressed into domain names) |
| SOA | Provides information about the coreesponding DNS zone and email address of the aministrative contact |

## NMAP
----------------
```shell
sudo nmap -sV --script dns-nsid -p53 $IP

nmap -Pn -p 53 --script dns-brute $IP -o $IP-nmap-dns-brute-scan
```
-----------------------------------------------------
## Dangerous Settings

| Option | Description |
| -------- | ------------ |
| allow-query | Defines which hosts are allowed to send requests to the DNS server |
| allow-recursion | Defines which hosts are allowed to send recursive requests to the DNS server |
| allow-transfer | Defnies which hosts are allowed to receive zone transfers from the DNS server |
| zone-statistics | Collect statistical data of zones. |

--------------------------------------
## DIG

- NS Query
```shell
dig ns inlanefreight.htb @$IP
```

- Version Query
```shell
dig CH TXT version.bind @$IP
```

- ANY Query
```
dig any inlane freight.htb @$IP
```

- AXFR Zone Transfer
```shell
dig axfr inlanefreight.htb @$IP
```

- AXFR Zone Transfer - Internal
```
dig axfr internal.inlanefreight.htb @$IP
```

- [Fierce](https://github.com/mschwager/fierce) can be used to enumerate all DNS servers of the root domain and scan for a DNS zone transfer
```bash
fierce --domain zonetransfer.me
```

------
## Domain Takeovers & Subdomain Enumeration
-----
### Sub Domains Enumeration

- #### Subdomain BruteForce
```shell
for sub in $(cat /opt/useful/SecLists/Discovery/DNS/subdomains-top1million-110000.txt);do dig $sub.inlanefreight.htb @10.129.245.203 | grep -v ';\|SOA' | sed -r '/^\s*$/d' | grep $sub | tee -a subdomains.txt;done
```

- #### [DNSenum](https://github.com/fwaeytens/dnsenum)
```shell
dnsenum --dnsserver $IP --enum -p 0 -s 0 -o subdomians.txt -f /opt/useful/SecLists/Discovery/DNS/subdomains-top1million-110000.txt inlanefreight.htb
```

- #### [Subfinder](https://github.com/projectdiscovery/subfinder) or [Sublist3r](https://github.com/aboul3la/Sublist3r)
```shell
subfinder -d inlanefreight.com -v
```

- [Subbrute](https://github.com/TheRook/subbrute)
```bash
echo "ns1.inlanefreight.com"/$IP > ./resolvers.txt
subbrute inlanefreight.com -s ./name.txt -r ./resovlers.txt
```

- After finding subdomains, we can use `nslookup` or `host` to enumerate the CNAME records
```bash
host support.inlanefreight.com
```

![](https://academy.hackthebox.com/storage/modules/116/s3.png)

- Looking at the error, we see there is NoSUchBucket, which indicate the subdomain can be taken over. We can crate AWS s3 bucket with the same subdomain name.
- [can-i-take-over-xyz](https://github.com/EdOverflow/can-i-take-over-xyz) is great for discovering subdomain takeover vulnerability and provides guidelines on assessing the vulnerability.

### DNS Spoofing
#### Local DNS Cache Poisoning
- We can use [Ettercap](https://www.ettercap-project.org/) or [Bettercap](https://www.bettercap.org/) as MITM tools to perform DNS Cache Poisoning
	1. Edit `/etc/ettercap/etter.dns` to map the target domain name (inlanefreight.com) & attacker's IP 
		```bash
		cat /etc/ettercap/etter.dns

		inlanefreight.com A $ATTACKER_IP
		*.inlanefreight.com A $ATTACKER_IP
		```
	2. Start Ettercap tool and scan for live hosts within the network
		- `Hosts > Scan For Hosts`
		- Once completed, add the $TARGET_IP to Target1 & add the default gateway IP to Target2
	3. Activate `dns_spoof` attack by navigating to `Plugins > Manage Plugins` . This sends the target machine with fake DNS responses that will resolve `inlanefreight.com` to $ATTACKER_IP
	4. After successful attacks, Target from $TARGET_IP visits `inlanefreight.com` will be redirected to a fake web page hosted on $ATTACKER_IP