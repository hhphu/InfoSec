# ZoneTransfer
- Zone transfer is how a secondary DNS server receives infromation from the primary DNS server and updates it.
- We will use [hakertarget](https://hackertarget.com/zone-transfer/)
- Identify name servers
```bash
nslookup -type=NS zonetransfer.me
```

- Test ANY and AXFR Zone Transfer
```bash
nslookup -type=any -query=AXFR zonetransfer.ne nsztm1.digi.ninja

# If we manage to perform a successful zone transfer for a domain, there is no need to continue enumerating this particular domain as this will extract all the available information.
```

- Gobuster
```bash
export TARGET=facebook.com
export NS=d.ns.facebook.com
export WORDLIST=numbers.txt
gobuster dns -q -r "${NS}" -d "${TARGET}" -w "${WORDLIST}" -p ./patterns.txt -o "gobuster_${TARGET}.txt"

	# options
	# dns: launch the DSN module
	# -q: Don't print the banner and other noise
	# -r: Use custom DNS server
	# -d: A target domain name
	# -p: Path to the patterns file
	# -w: Path to the wordlist
	# -o: Output file
```