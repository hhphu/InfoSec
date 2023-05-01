| Default System Database | Description |
| --------------------------- | ------------- |
| master | Tracks all system information for an SQL server instance. |
			| model | template database that acts as a structure for every new database created. Any setting changed in the model database will be reflected in any new database created after changes to the model databases. |
| msdb | The SQL Server Agenet uses this database to schedule jobs & alerts | 
| tempdb | Stores temporary objects |
| resource | Read-only database containg system objects included with SQL server. |

# Footprinting the Service
- NMAP MSSQL Script Scan
```bash 
sudo nmap 
	--script ms-sql-info,ms-sql-empty-password,ms-sql-xp-cmdshell,ms-sql-config,ms-sql-ntlm-info,ms-sql-tables,ms-sql-hasdbaccess,ms-sql-dac,ms-sql-dump-hashes 
	--script-args mssql.instance-port=1433,mssql.username=sa,mssql.password=,mssql.instance-name=MSSQLSERVER 
	-sV -p1433 $IP
```

- MSSQL Ping in Metasploit
```bash
auxiliary/scanner/mssql.mssql_ping
```

- Connecting with Mssqlclient.py
```bash
python3 mssqlclient.py Administrator@$IP -windows-auth
```

