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

----------------------------------
# Send an Email
-----
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

---------------------------------------
## ENUMERATION
-----
### Enumerate MX Records
```bash
# Using host
host -t MX hackthebox.eu

# Using host - A Record for MX
host -t A mail1.inlanefrieght.htb

# Using DIG
dig mx inlanefreight.com | grep "MX" | grep -v ";"
```

- The following ports can be explored for mail services:

|**Port**|**Service**|
|---|---|
|`TCP/25`|SMTP Unencrypted|
|`TCP/143`|IMAP4 Unencrypted|
|`TCP/110`|POP3 Unencrypted|
|`TCP/465`|SMTP Encrypted|
|`TCP/993`|IMAP4 Encrypted|
|`TCP/995`|POP3 Encrypted|

### nmap
```bash
# General scan
nmap -Pn -sV -sC -p25,143,110,465,993,995 10.129.14.128

# Using nmap script
sudo nmap $IP -sC -sV -p25 --script smtp-open-relay -v

# Using nmap script with arguments
sudo nmap -p25 $IP --script smtp-enum-users --script-args smtp-enum-users.method={VRFY},userdb=<FILE_NAME>
```

-----
## AUTHENTICATION
-----
- Three commands can be used for username enumeration: VRFY, EXPN, RCPT TO
- First we need to connect to the server
```bash
telnet $IP 25
```
- The actual initialization of the session si done with the command HELO
```
HELO mail1.inlanefreight.htb
```

#### VRFY
- We can use `VRFY` command to verify if a user exists. However, it does not always work. Depending the configuration, the SMTP may issue different status codes, which can be found [here](https://serversmtp.com/smtp-error/).
```bash
VRFY root

252 2.0.0 root


VRFY www-data

252 2.0.0 www-data


VRFY new-user

550 5.1.1 <new-user>: Recipient address rejected: User unknown in local recipient table
```

#### EXPN
- Similar to `VRFY`, except that it provide a list of all users
```bash
EXPN john

250 2.1.0 john@inlanefreight.htb

EXPN support-team

250 2.0.0 carol@inlanefreight.htb
250 2.1.5 elisa@inlanefreight.htb
```

#### RCPT TO
- Identify the recipient of the email message.
```bash
MAIL FROM:test@htb.com
it is
250 2.1.0 test@htb.com... Sender ok


RCPT TO:julio

550 5.1.1 julio... User unknown


RCPT TO:kate

550 5.1.1 kate... User unknown


RCPT TO:john

250 2.1.5 john... Recipient ok
```

#### USER 
- We can use POP3-USER command to enumerate users: `telnet $IP 110`
```bash
USER julio

-ERR

USER john

+OK

```

### [smtp-user-enum](https://github.com/pentestmonkey/smtp-user-enum)
- Automate enumeration process
```bash
smtp-user-enum -M RCPT -U userlist.txt -D inlanefreight.htb -t 10.129.203.7

# Options
-M: the command used (VRFY, EXPN, RCPT)
-U: list of users
-D: domain for the email address
-t: target
```
- Note: This doesn't work all the time. Double check with Metasploit (auxiliary/scanner/smtp/smtp_enum)
-----
# CLOUD ENUMERATION
-----
### [o365spray](https://github.com/0xZDH/o365spray)
- Username enumeration and password spraying tool
- First we validate the domain
```bash
python3 o365spray.py --validate --domain $DOMAIN
```

- Identify usernames
```bash
python3 o365spray.py --enum -U users.txt --domain msplaintext.xyz
```

- Password Spraying
```bash
python3 -365spray.py --spray -U $USER_FILE -p $PASS --count 1 --lockout 1 --domain $DOMAIN
```


----------------------------------
# OPEN RELAY CONFIGURATION
-----
- Open Relay is a SMTP server, improperly configured and allows unauthenticated email relay
- Attackers can send phishing emails as non-existing users or spoof emails to compormise targets.
```bash
mynetworks = 0.0.0.0/0
```
- With this setting, this SMTP server can send fake emails and thus initialize communication between multiple parties/ spoof the email and read it.
- nmap scan
```bash
nmap -p25 -Pn --script smtp-open-relay $IP
```
- Use any mail client to connect to the mail server and send our emails
```bash
swaks --from notification@inlanefreight.com --to employees@inlanefreight.com --header 'Subject: Company Notification' --body 'Hi All, we want to hear from you! Please complete the following survey. http://mycustomphishinglink.com/' --server 10.10.11.213
```