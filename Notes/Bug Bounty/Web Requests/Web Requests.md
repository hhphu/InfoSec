# HTTP Fundamentals

## HyperText Transfer Protocol (HTTP)
### URL
```bash
    http://admin:password@example.com:80/dashboard.php?login=true#status

    http:// - scheme: identify the protocol being used
    admin:password - user credentials: this is username:password pair used to access the application
    example.com - host: the host application we try to access to
    80 - port: the port number on which the application is hosted
    /dashboard.php - path: Identify the resources being accessed through the application.
    ?login=true - query string: contains parameter:value pair 
    #status - fragment: identified the section to land on
```

### HTTP Flow
1. Users request example.com via browser
2. Browser reaches out to DNS server to ask for IP address.
3. DNS server returns with example.com's IP address: 1.2.3.4
4. The browser sends GET request to 1.2.3.4
5. The example.com server receives the request and responds with the resources requested
6. The browser displays the resources returned from the example.com server

## HyperText Transfer Protocol Secure (HTTPS)
1. Users request example.com using HTTP request
2. The request is redirected to HTTPS on port 443
3. Three-way handshakes occurs: the Client sends Hello 
4. The server responds with Hello and key exchange
5. The client verifies the key/certificates and send its own to the server. An encrypted handshake connection is established to confirm whether the connection works
6. Once confirmed, the HTTPs communication continues.

