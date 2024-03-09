FFUF

# Basic Fuzzing
------

## Directory Fuzzing
```bash
ffuf -w /opt/useful/SecLists/Discovery/Web-Content/directory-list-2.3-small.txt:FUZZ -u http://$TARGET/FUZZ
```

## Page Fuzzing
- Extension Fuzzing
```bash
ffuf -w /opt/useful/SecLists/Discovery/Web-Content/web-extensions.txt:FUZZ -u http://$TARGET/indexFUZZ

# The wordlist already contains the dots. So we don't need to include the . in the command
```

- Page Fuzzing
```bash
ffuf -w /opt/useful/SecLists/Discovery/Web-Content/directory-list-2.3-small.txt:FUZZ -u http://$TARGET/FUZZ.php
```

- Recursive Fuzzing
```bash
ffuf -w /opt/useful/SecLists/Discovery/Web-Content/directory-list-2.3-small.txt:FUZZ -u http://$TARGET/FUZZ -recursion -recursion-depth 1 -e .php -v

# -e: specify the extension
# -recursion-depth: specify the depth we want to fuzz
```

# Domain Fuzzing
-----

## Sub-domain Fuzzing
```bash
ffuf -w /opt/useful/SecLists/Discovery/DNS/subdomains-top1milliion-5000.txt:FUZZZ -u http://FUZZ.$TARGET
```

## Vhosts FUzzing
```bash
ffuf -w /opt/useful/SecLists/Discovery/DNS/subdomains-top1million-5000.txt:FUZZ -u http://$TARGET -H 'Host: FUZZ.$TARGET'
```

## Parameter Fuzzing - GET
```bash
ffuf -w /opt/useful/SecLists/Discovery/Web-Content/burp-parameter-names.txt:FUZZ -u http://$TARGET/admin/admin.php?FUZZ=key
```

## Parameter Fuzzing - POST
- Key fuzzing
```bash
ffuf -w /opt/useful/SecLists/Discovery/Web-Content/burp-parameter-names:txt:FUZZ -u http://$TARGET/admin/admin.php -X POST -d 'FUZZ=key' -H 'Content-Type: application/x-www-form-urlencoded'
```
- Value fuzzing
```bash
ffuf -w /opt/useful/SecLists/Discovery/Web-Content/burp-parameter-names:txt:FUZZ -u http://$TARGET/admin/admin.php -X POST -d 'id=FUZZ' -H 'Content-Type: application/x-www-form-urlencoded'
```



