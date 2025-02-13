# Cross Site Request Forgery (CSRF)

**URL:** https://tryhackme.com/room/csrfV2

# TABLE OF INDEX

1. [Learning Objecgives](#learning-objectives)
2. Setup
3. CSRF Overview
4. 


## Learning Objectives
- Understand the working of CSRF
- Type of CSRF attacks
- Advance payloads for exploitation
- Defensive mechanisms

## Setup

![image](https://github.com/user-attachments/assets/59ecfb33-cc5a-440c-8120-104b7d59b6a1)

## CSRF Overview

Cross Site Request Forgery (CSRF) is a vulnerability on web applications where attackers take advantage of the victims' identities to make malicious requests, usually through browsers that has the victims' cookies attached to.

There are three phases of a CSRF attack:

- Attackers have knowledge of the traffics on the applications (hence they can craft malicious payloads for the exploit)
- The victims' identities are confirmed on the websites, usually through the cookies transmitted throughout multiple domains.
- The lack of security implementations on the websites that prevent attackers making unauthorized requests on behalf of the victims.

### CSRF Effect

- A successful CSRF can result in unauthorized access to users' data, leading to information disclosure. Attackers can also manipulate users' information for specific purposes.
- Stealthy exploitation: Attackers can leverage CSRF and use it as a stepping stone for other attacks to further exploit the applications.

## ANSWER THE QUESTIONS

![image](https://github.com/user-attachments/assets/721f4b3e-a8b4-4b84-a551-326abceba9b8)

-> `d`

**Does the attacker usually know the web application requests and response format while launching a CSRF attack (yea/nay)?**

-> `yea`



