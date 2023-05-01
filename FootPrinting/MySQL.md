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
mysql -u root -h $IP
```

- 