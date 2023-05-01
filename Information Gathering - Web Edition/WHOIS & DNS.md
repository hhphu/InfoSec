## WHOIS
```bash
export TARGET="facebook.com"
whois $TARGET
```

- Gather the as much information as possible:
	- Organization
	- Locations
	- Domain Email address
	- Phone Number
	- Language
	- Register
	- New Domain
	- DNSSEC
	- Name servers

## DNS
```bash
export TARGET="facebook.com"
nslookup $TARGET
	OR
dig facebook.com @1.1.1.1
```

- Query  records
```bash
# Query A records
nslookup -query=A $TARGET
dig a www.facebook.com @1.1.1.1

# Query PTR records
nslookup -query=PTR $IP # IP address obtained from the A record
dig -x $IP @1.1.1.1

# Query ANY existing records
nslookup -query=ANY $TARGET
dig any google.com @8.8.8.8

# Query TXT records
nslookup -query=TXT $TARGET
dig txt facebook.com @1.1.1.1

# Query MX records
nslookup -query=MX $TARGET
dig mx facebook.com @1.1.1.1
```

------------------------------
# Process
```bash
# nslookup
export TARGET="facebook.com"
nslookup $TARGET

# whois
whois $IP #IP obtained in nslookup above
```
- Find
	- IANA ID
	- Mail server when querying MX