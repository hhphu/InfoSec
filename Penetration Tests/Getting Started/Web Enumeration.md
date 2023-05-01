## Directory/File Enumeration
```
gobuster dir -U $IP -w <WORD_LIST>
```

## DNS Subdomain Enumeration
```
	1. Add domain to /etc/hosts
	2. Run:
		gobuster dns -d htb.com -w <WORDLIST>
```

## Tips & Tricks
- Banner Grabbiung / Web Server Headers
```
curl -IL https://google.com
```
- EyeWitness: used to take screenshots of targets, fingerprint them and identify possible default credentials.
- Whatweb: extract versoin of the servers, supporint frameworks
```
whatweb $IP

# Automate web application enumeration across a network
whatweb --noerrors 10.10.10.0/24
```
