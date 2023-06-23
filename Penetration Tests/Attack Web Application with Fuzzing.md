-----
# BASIC FUZZING
----
- Directory Fuzzing
```bash
ffuf -w Seclists/Discovery/Web-Content/directory-list-2.3-small.txt:FUZZ -u $URL/FUZZ -ic -e .php -recursion -recursion-depth $VALUE

-ic: removes all the copyrights/licenses in wordlists
```

- Extension Fuzzing
```bash
ffuf -w Seclists/Discovery/Web-Content/web-extensions.txt:FUZZ -u $URL/blog/indexFUZZ -ic
```

- Page Fuzzing
```bash
ffuf -w Seclists/Discovery/Web-Content/directory-list-2.3-small.txt:FUZZ -u $URL/blog/FUZZ -e .php -ic
```

- Recursive Fuzzing
```bash
ffuf -w Seclists/Discovery/Web-Content/directory-list-2.3-small.txt:FUZZ -u $URL/FUZZ -ic -e .php -recursion -recursion-depth $VALUE

-e: extension

# if $VALUE = 1 => only /blog is returned
# if $VALUE = 2 => /blog/index is returned
```

-----
# DOMAIN FUZZING
-----
- DNS Fuzzing
```bash
# Add IP to host file
echo "$IP example.com" >> /etc/hosts

# Fuzzing subdomains
ffuf -w Seclists/Discovery/DNS/subdomains-top1million-5000.txt:FUZZ -u http://FUZZ.example.com -ic 
```

- VHOST Fuzzing
	- VHOST is like sub-domain servers, where it allows 1 IP address to display different servers
	- Fuzzing VHOST will allow us to fuzz non-public subdomains
	-  A lot of out puts will have the same response size, we can filter them .
```bash
ffuf -w Seclists/Discovery/Web-Content/directory-list-2.3-small.txt:FUZZ -u $URL -H "Host: FUZZ.example.com" -fs 900
```

-----
# PRAMETER FUZZING
-----
- Fuzzing with GET
```bash
ffuf -w Seclists/Discovery/Web-Content/burp-parameter-names.txt:FUZZ -u $URL/admin/admin.php?FUZZ=key -fs xxx

#filter the ones with different sizes in response
```

- Fuzzing with POST
```bash
ffuf -w Seclists/Discovery/Web-Content/burp-parameter-names.txt:FUZZ -u $URL/admin/admin.php -X POST -d "FUZZ=key" -H "Content-Type: application/x-www-form-urlencoded" -fs xxx
```

- Fuzzing values for parameters
```bash
# Create a custom list: Since we find id, numbers are likely to be the values
for i in $(seq 1 1000); do echo $i >> ids.txt; done

ffuf -w customlist:FUZZ -u $URL/admin/admin.php -x POST -d "id=FUZZ" -H "Content-Type: application/x-www-form-urlencoded" -fs xxx
```

- curl the target with POST request
```bash
curl http://admin.academy.htb:$PORT/admin/admin.php -x POST -d "id=$VALUE" -H "Content-Type: application/x-www-form-urlencoded"
```

