# Command Injection Overview
-----
Command Injections stand out as one of the most critical vulnerabilities in the realm of cybersecurity. This type of vulnerability provides a gateway for executing system commands directly on the hosting server's back-end, potentially compromising the entire network. When a web application employs user-controlled input to execute system commands, there exists an opportunity to inject a malicious payload, diverting the intended command and executing unauthorized actions.

#### Command Injection Detection
- Whenever there's an input field, we can potentially have a command injection vulnerability.

- We can try variou commands with different operators (`;`, `\n`,`&&`, `|`, etc.)

#### Injecting Commands
- Assume we have an application that ping an IP address, we can add another command after the IP

![](https://academy.hackthebox.com/storage/modules/109/cmdinj_basic_injection.jpg)

- As we can see the application refuses our inout. However, it looks like the input validation is done on the front-end (i.e in the 2 commands execute successfully). 

#### Bypass Front-End Validation
- To bypass front-end validations, we can use BurpSuite to intecept the request. If there's only front-end validation, the Reponse will print the output of the commands

![](https://academy.hackthebox.com/storage/modules/109/cmdinj_basic_repeater_2.jpg)

# TABLE OF CONTENT