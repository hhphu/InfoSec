# Dangerous Settings
| Settings | Description |
| --------- | ------------ |
| PasswordAuthentication yes | Allows password-based authentication. |
| PermitEmptyPasswords yes | Allows the use of empty passwords. |
| PermitRootLogin yes | Allows to log in as the root user. |
| Protocol 1 | Usess an outdated version of encryption. |
| X11Forwarding yes | Allows X11 forwarding for GUI applications. |
| AllowTcpForwarding yes | Allows forwarding of TCP ports. |
| PermitTunnel |  Allow tunneling |
| DebianBanner yes | Displays a specific banner when logging in. |

# Footprinting the Service
--------------------------------------------------
- SSH-Audit
```bash
git clone https://github.com/jtesta/ssh-audit.git && cd ssh-audit
./ssh-audit.py $IP
```

- Change Authentication Method
```bash
ssh -v $user@$IP

# Potential brute-force attacks
ssh -v $user@$IP -o PreferredAuthentication=password
```

# SSH Tunneling
## Local Port forwarding
--------------------------------------------
```bash
ssh -L 1234:localhost:5432 christine@$<TARGET_IP>
	-L: specify we use local port forwarding
	- 1234: the port of the attactker machine
	- localhost: the TARGET's localhost
	- 5432: the port on the TARGET to which we want to forward
```

- Once we establish the local port forwarding, we can interact with services on the remote target.
```
psql -h localhost -U christine -p 1234
```

## Dynamic Port Forwarding
-------------------------------------------------
```bash
ssh -D 1234 christine@<TARGET_IP>
	-D: specify we want to use dynamic port forwarding
	- 1234: The port of attacker's machine

# We can use the -f and -N flags so we don't actually SSH into the box, and can instead continue using that shell locally.
```

- Modify proxychains forward the traffic:
	1. Ensure *strict_chain* is not commented out. *dynamic_chain* & *random_chain* shoudl be commented out.
```bash
[ProxyList] # add proxy here ... # meanwile # defaults set to "tor" #socks4 127.0.0.1 9050 socks5 127.0.0.1 1234
```

- Use proxychain
```bash
proxychains psql -U christine -h localhost -p 5432

	5432: the port of the TARGET machine
	localhost: the localhost of target machine
```
