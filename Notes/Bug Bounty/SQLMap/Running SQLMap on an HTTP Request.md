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



