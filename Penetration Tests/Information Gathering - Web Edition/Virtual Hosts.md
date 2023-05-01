## Name-based Virtual Hosting
- During enumerations, we might find some domain names using the same IP. Internally, these are separated and distinguished using different folders.
- curl
```bash
curl -s http://$IP -H "Host: randomtarget.com"
```
- We can automate this by using a dictionary file `/opt/useful/SecLists/Discovery/DNS/namelist.txt`
- Create `vhost.txt`
```
app
blog
dev-admin
forum
help
m
my
shop
some
store
support
www
```

- vHost Fuzzing
```shell
cat ./vhosts | while read vhost;do echo "\n********\nFUZZING: ${vhost}\n********";curl -s -I http://192.168.10.10 -H "HOST: ${vhost}.randomtarget.com" | grep "Content-Length: ";done
```

## Automating Virtual Hosts Discovery
```bash
ffuf -w ./vhosts -u http://$IP -H "HOST: FUZZ.randomtarget.com" -fs 612
	# options
	-w: path to the wordlist
	-u: URL
	-fs: Filter HTTP reponses with a size of 612, default response size in this case.
```