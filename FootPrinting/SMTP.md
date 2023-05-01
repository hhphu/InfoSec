- Simple Mail Transfer Protocol (#25 or #587)

| Commnad | Description |
| ------------ | ------------ |
	| AUTH PLAIN | AUTH is a service exentaion used to authenticate the client |
	| HELO | The client logs in with its computer name and thus starts the session |
	| MAIL FROM | The client names the email sender. |
	| RCPT TO | The client names the email recipient. |
	| DATA | The client initiates the transmission of the email. |
	| RSET | The client aborts the initiated transmission but keeps the connection between client and server |
	| VRFY | The client checks if a mailbox is availablel for message transfer. |
|	EXPN | The client also checks if a mailbox is available for messaging with this command |
| NOOP | The client requests a response from the server to prevent disconnection due to time-out |
| QUIT | the client terminates the sessions. |

-------------------------------------------------------
## Telnet - HELO/EHLO
- To interact with SMTP server, we can use telnet
```bash
telnet $IP 25
```
- The actual initialization of the session si done with the command HELO
```
HELO mail1.inlanefreight.htb
```

## Telnet - VRFY
- We can use `VRFY` command to verify if a user exists. However, it does not always work. Depending the configuration, the SMTP may issue different status codes, which can be found [here](https://serversmtp.com/smtp-error/).
```bash
VRFY root
VRFY cryol1t3
```

----------------------------------
## Send an Email

```bash 
telnet $IP 25

Trying 10.129.14.128...
Connected to 10.129.14.128.
Escape character is '^]'.
220 ESMTP Server


EHLO inlanefreight.htb

250-mail1.inlanefreight.htb
250-PIPELINING
250-SIZE 10240000
250-ETRN
250-ENHANCEDSTATUSCODES
250-8BITMIME
250-DSN
250-SMTPUTF8
250 CHUNKING


MAIL FROM: <cry0l1t3@inlanefreight.htb>

250 2.1.0 Ok


RCPT TO: <mrb3n@inlanefreight.htb> NOTIFY=success,failure

250 2.1.5 Ok


DATA

354 End data with <CR><LF>.<CR><LF>

From: <cry0l1t3@inlanefreight.htb>
To: <mrb3n@inlanefreight.htb>
Subject: DB
Date: Tue, 28 Sept 2021 16:32:51 +0200
Hey man, I am trying to access our XY-DB but the creds don't work. 
Did you make any changes there?
.

250 2.0.0 Ok: queued as 6E1CF1681AB


QUIT

221 2.0.0 Bye
Connection closed by foreign host.
```

----------------------------------
## Open Relay Configuration
```bash
mynetworks = 0.0.0.0/0
```
- With this setting, this SMTP server can send fake emails and thus initilaize communication between multiple parties/ spoof the email and read it.

---------------------------------------
## Footprinting
```bash
sudo nmap $IP -sC -sV -p25 --script smtp-open-relay -v
sudo nmap -p25 $IP --script smtp-enum-users --script-args smtp-enum-users.method={VRFY},userdb=<FILE_NAME>
```

--------------------------------------------------------
### Enumerate users
```bash
smtp-user-enum -M VRFY -U usernames.txt -t $IP
```
- Note: This doesn't work all the time. Double check with Metasploit (auxiliary/scanner/smtp/smtp_enum)