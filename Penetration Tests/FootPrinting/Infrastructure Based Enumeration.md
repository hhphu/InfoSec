## Online Presence
--------------------
### SSL Certificate
- Website certificate (the lock icon)
- https://crt.sh/
	- To output the results in JSON format
		```shell
		curl -s https://crt.sh/\?q\=inlanefreight.com\%output\=json | jq .
		```
	- To filter out unique subdomains
		```shell
		curl -s https://crt.sh/\?q\=inlanefreight.com\%output\=json | jq . | grep name | cut -d":" -f2 | grep -v "CN=" | cut -d'"' -f2 | awk '{gsub(/\\n/,"\n");}1;' | sort -U
		```

- Company hosted server
```shell
Huy Phu-1@htb[/htb]$ for i in $(cat subdomainlist);do host $i | grep "has address" | grep inlanefreight.com | cut -d" " -f1,4;done

blog.inlanefreight.com 10.129.24.93
inlanefreight.com 10.129.27.33
matomo.inlanefreight.com 10.129.127.22
www.inlanefreight.com 10.129.127.33
s3-website-us-west-2.amazonaws.com 10.129.95.250
```

- Once we see which hosts can be investigated further, we can generate a list of IP addresses with a minor adjustment to the `cut` command and run them through [Shodan](https://www.shodan.io/).
```shell
for i in $(cat subdomainlist);do host $i | grep "has address" | grep inlanefreight.com | cut -d" " -f4 >> ip-addresses.txt;done

for i in $(cat ip-addresses.txt);do shodan host $i;done
```

### DNS Records
```shell
dig any inlanefreight.com
```
-   `A` records: We recognize the IP addresses that point to a specific (sub)domain through the A record. Here we only see one that we already know.
    
-   `MX` records: The mail server records show us which mail server is responsible for managing the emails for the company. Since this is handled by google in our case, we should note this and skip it for now.
    
-   `NS` records: These kinds of records show which name servers are used to resolve the FQDN to IP addresses. Most hosting providers use their own name servers, making it easier to identify the hosting provider.
    
-   `TXT` records: this type of record often contains verification keys for different third-party providers and other security aspects of DNS, such as [SPF](https://datatracker.ietf.org/doc/html/rfc7208), [DMARC](https://datatracker.ietf.org/doc/html/rfc7489), and [DKIM](https://datatracker.ietf.org/doc/html/rfc6376), which are responsible for verifying and confirming the origin of the emails sent. Here we can already see some valuable information if we look closer at the results.
