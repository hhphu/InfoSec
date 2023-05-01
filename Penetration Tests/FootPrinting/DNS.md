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
dig CH TXT version.bind $IP
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

- Subdomain BruteForce
```shell
for sub in $(cat /opt/useful/SecLists/Discovery/DNS/subdomains-top1million-110000.txt);do dig $sub.inlanefreight.htb @10.129.245.203 | grep -v ';\|SOA' | sed -r '/^\s*$/d' | grep $sub | tee -a subdomains.txt;done
```

## [DNSenum](https://github.com/fwaeytens/dnsenum)
```shell
dnsenum --dnsserver $IP --enum -p 0 -s 0 -o subdomians.txt -f /opt/useful/SecLists/Discovery/DNS/subdomains-top1million-110000.txt inlanefreight.htb
```

