# VirusTotal
- Type the domain name into the search bar and click the Relations tab.

# Certificates
- Use the following two sites for inspections: [censys](https://censys.io/) & [crt.sh](https://crt.sh/)

# Certificate Transparency
- curl
```bash
curl -s "https://crt.sh/?q=${TARGET}&output=json" | jq -r '.[] | "\(.name_value)\n\(.common_name)"' | sort -u > "${TARGET}_crt.sh.txt"
	
	jq: command used to transform JSON data into more readable formats for Linux.
	jq -r : concatinate strings
		# echo '{ "object" : { "name": "banana", "color": "yellow" }}' |\
		# jq -r '.object | "\(.name) is \(.color)"'
		# will print "banana is yellow."
```

- openssl
```bash
openssl s_client -ign_eof 2>/dev/null <<<$'HEAD / HTTP/1.0\r\n\r' -connect "${TARGET}:${PORT}" | openssl x509 -noout -text -in - | grep 'DNS' | sed -e 's|DNS:|\n|g' -e 's|^\*.*||g' | tr -d ',' | sort -U
```

# TheHarvester
- Create `sources.txt` with the most popular modules:
```bash
sudo nano sources.txt

baidu
bufferoverun
crtsh
hackertarget
otx
projecdiscovery
rapiddns
sublist3r
threatcrowd
trello
urlscan
vhost
virustotal
zoomeye
```

- Execute the command
```bash
cat sources.txt | while read source; do theHarvester -d "${TARGET}" -b $source -f "${source}_${TARGET}";done
```

- When the process finishes, extract all the subdomains found and sort them
```bash
cat *.json | jq -r '.hosts[]' 2>/dev/null | cut -d':' -f 1 | sort -u > "${TARGET}_theHarvester.txt"
```

- Merge all the passive reconnaissance files:
```bash
cat facegbook.com_*.txt | sort -U > facebook.com_subdomains.passive.txt
cat facebook.com_subdomains_passive.txt | wc -l
```