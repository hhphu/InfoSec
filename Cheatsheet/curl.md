# curl
------

- cURL help menu 
```bash
curl -h
```

- Basic GET request
```bash
curl www.example.com
```

- Download file
```bash
curl -s -O example.tcom/index.html
```

- Skip HTTPS (SSL) certificate validation
```bash
curl -k https://example.com
```

- Print full HTTP requesst/reponse details
```bash
curl example.com -v
```

- Send HEAD request (only prints response header)
```bash
curl -I https://example.com
```

- Print response headers and body
```bash
curl -i https://example.com
```

- Set User-Agent header
```bash
curl https://example.com -A "Mozilla/5.0"
```

- Pass HTTP basic authorization credentials in the URL
```bash
curl https://username:password@example.com:1234
```

- Set request header
```bash
curl -H "Authorization: Basic URNADkd=" https://example.com
```

- Pass GET parameters
```bash
curl "https://example.com/search.php?search=ls"
```

- Send POST request with POST data
```bash
curl -X POST -d "username=admin&password=pass" https://example.com
```

- Set request cookies
```bash
curl -b "PHPSESSID=ckljgdnfakdlssa1" https://example.com
```

- Send POST request with JSON data
```bash
curl -X POST -d "{'search':'htb'}" -H "Content-Type: application/json" https://example.com/search.php
```

## curl with APIs

- Read entry
```bash
curl https://example.com/api.php/city/newyork
```

- Read all entries
```bash
curl -s https://example.com/api,php/city | jq
```

- Create (add) an entry
```bash
curl -X PUT https://example.com/api.php/city -d "{'city':'LA','country':'USA'}" -H "Content-Type: application/json"
```

- Delete an entry
```bash
curl -X DELETE https://example.com/api.php/city/LA
```

