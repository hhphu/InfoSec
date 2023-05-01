## Internet Message Access Protocol: 
	- Manages emails on a remote server. 
	- client-server-based
	- allow synchronization of a local email elint with the mailbox on the server -> network file ystems for emails.

## POP3
	- Only provide listings, retrieving and deleting emails as funcitons at the email server.

## Footprintint the Service
- nmap
```bash
sudo nmap $IP -sV -sC -p110,143,993,995
```

- curl
```bash
# IMAP
curl -k 'imaps://$IP' --user user:password
# POP3
curl -k 'pop3s://$IP' --user user:password
```

- netcat
```bash
# POP3
nc -nv $IP 110
# IMAP
nc nv $IP 143
```

- openSSL - TLS Encrypted interaciton POP3
```bash
openssl s_client -connect $IP:pop3s
```

- openSSL - TLS Encrypted Interaction IMAP
```bash
openssl s_client -connect $IP:imaps
```

-----------------------------------------------------
## IMAP Commands

| Command | Description |
| ----------- | ------------- |
| 1 LOGIN username password | Login with username and passowrd |
| 1 LIST "" *  | List all directoried |
| 1 SELECT INBOX | Select a mailbox so that messages in the mailbox can be accessed |

For more information and use cases, refer to this [post](https://www.atmail.com/blog/imap-commands/)
