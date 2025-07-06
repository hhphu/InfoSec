# Information Gathering


# Passive Information Gathering
-----

## WHOIS
```bash
export TARGET="facebook.com"
whois $TARGET
```

## DNS
### nslookup
```bash
nslookup $TARGET

```

### dig
```bash
dig facebook.com @1.1.1.1
```

### Query A records for subdomains
```bash
export TARGET="www.facebook.com"

nslookup -query=A $TARGET 
	OR
dig a $TARGET @1.1.1.1
```

### QUery PTR Records for an IP address
- TARGET=31.13.92.36

```bash
nslookup -query=PTR $TARGET
	OR
dig -x $TARGET @1.1.1.1
```

### Query ANY exisiting records
- TARGET="google.com"

```bash
nslookup -query=ANY $TARGET
	OR
dig any $TARGET @8.8.8.8
```

### Query TXT records
- TARGET="facebook.com"
```bash
nslookup -query=TXT $TARGET
	OR
dig txt $TARGET @1.1.1.1
```

### Query MX records
```bash
nslookup -query=MX $TARGET
	OR
dig mx $TARGET @1.1.1.1
```

## Passive Subdomain Enumeration
- we can extract information of subdomain via the following sites:

#### VirusTotal: https://www.virustotal.com/gui/home/upload
#### Certificates
- There are two sites to enumerate certificates
https://censys.io
	&
https://crt.sh

```bash
curl -s "https://crt.sh/?q=${TARGET}&output=json" | jq -r '.[] | "\(.name_value)\n\(.common_name)"' | sort -u > "${TARGET}_crt.sh.txt"

curl -s: Issue the request with minimal output.
https://crt.sh/?q=<DOMAIN>&output=json: Ask for the json output.
jq -r '.[]' "\(.name_value)\n\(.common_name)"': Process the json output and print certificate's name value and common name one per line.
sort -u: Sort alphabetically the output provided and removes duplicates.
```

### Automate subdomain enumeration
#### [TheHarvester](https://github.com/laramies/theHarvester)
- It uses various sources to enumerates emails, names, domains, subdomains of the targets.
- To automate the process:
1. Create a list of sources that will be used by TheHarvester `sources.txt`
```bash
baidu
bufferoverun
crtsh
hackertarget
otx
projectdiscovery
rapiddns
sublist3r
threatcrowd
trello
urlscan
vhost
virustotal
zoomeye
```
2. Run the Harvester command using the sources
```bash
cat sources.txt | while read source; do theHarvester -d "${TARGET}" -b $source -f "${source}_${TARGET}";done
```

3. Extract all the subdomains found and sort them:
```bash
cat *.json | jq -r '.hosts[]' 2>/dev/null | cut -d':' -f 1 | sort -u > "${TARGET}_theHarvester.txt"
```

4. Merge all the passive reconnaissance files
```bash
cat facebook.com_*.txt | sort -u > facebook.com_subdomains_passive.txt
cat facebook.com_subdomains_passive.txt | wc -l
```


# Active Information Gathering
-----

## Active Infrastructure Identification

- HTTP Headers
```bash
curl -I "http://${TARGET}"
```

- WhatWeb
```bash
whatweb -a3 https://www.facebook.com -v
```

- WafW00f
```bash
sudo apt install wafw00f -y
wafw00f -v https://wwww.tesla.com
```

- Aquatone
```bash
sudo apt install golang chromium-driver
go get github.com/michenriksen/aquatone
export PATH="$PATH":"$HOME/go/bin"

# Use Aquatone with the list of subdomains
cat facebook_aquatone.txt | aquatone -out ./aquatone -screenshot-timeout 1000

There will be aquatone_report.html file generated once the process finishes.
```
