# HTTP Verb Tampering

## Bypassing Basic Authentication
-----
### Identify
- We need to identify which pages are restricted by authentication. When can send the requests to BurpSuite for investigation.
![front-end](https://academy.hackthebox.com/storage/modules/134/web_attacks_verb_tampering_reset.jpg)

![BurpSuite](https://academy.hackthebox.com/storage/modules/134/web_attacks_verb_tampering_unauthorized_request.jpg)

### Exploit
- Enumerate what `OPTIONS` are accepted by the web application
```bash
curl -i -X OPTIONS $TARGET
```
- After that, try all other possible `OPTIONS` that are allowed by the application.
![allowed_options](https://academy.hackthebox.com/storage/modules/134/web_attacks_verb_tampering_HEAD_request.jpg)

## Bypassing Security Filters
-----
### Identify
- Try payloads with special characters like `test;` -> There shoudld be an error, indicating there's a security filter.

### Exploit
- We can try "Change request method" option in BurpSuite. Once the request is changed, we're most likely to bypass security filters

