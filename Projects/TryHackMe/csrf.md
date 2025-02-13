# Cross Site Request Forgery (CSRF)

**URL:** https://tryhackme.com/room/csrfV2

# TABLE OF INDEX

**1. [Learning Objectives](#learning-objectives)**

**2. [Setup](#setup)**

**3. [CSRF Overview](#csrf-overview)**

**4. [Types of CSRF attacks](#types-of-csrf-attacks)**

**5. [Basic CSRF Exploitation](#basic-csrf-exploitation)**

**[Answer the questions](#answer-the-questions)**


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

## Types of CSRF attacks

### Traditional CSRF
- Traditional CSRF focuses on the state-changing of the application by submiting forms.
  
![image](https://github.com/user-attachments/assets/30bd5ff1-fed3-4244-a306-34d2bb04b5aa)

1. A user authenticates to the banking application
2. The attacker crafts a malicious link and send it to the user. This malicious link contains the actions the attacker wants to perform on the application under the user's identity.
3. The user open the email on the same browser and clicks the link.
4. The unauthorized action is performeed (transfering money to the attacker's account) using the victim's cookies.

### XMLHttpRequest CSRF
An asynchronous CSRF (Cross-Site Request Forgery) attack occurs when an attacker forces a victim’s browser to make an unauthorized request without requiring a full page reload. Instead of using a traditional HTML form submission, these attacks leverage JavaScript's XMLHttpRequest (XHR) or the Fetch API to send requests in the background—just like modern web applications do for smoother user experiences.

Example: assume a user is using an email service `mailbox.thm`, which allows him/her to update email forwarding settings without refreshing the page. The service uses an API endpoint:

```bash
POST mailbox.thm/api/updateEmail
```

A legitimate request from a logged-in user might look like this:

```javascript
fetch("https://mailbox.thm/api/updateEmail", {
  method: "POST",
  credentials: "include",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ forwardTo: "mynewemail@example.com" })
});
```

If the email service does not have CSRF protection, an attacker can exploit this behavior.

1. The user logs into `mailbox.thm`, which results in the browser's storing an authenticated session cookie for `mailbox.thm`
2. The attacker tricks the victim into clicking a malicious links, which executes JavaScript codes. The script may look like this:

```javascript
fetch("https://mailbox.thm/api/updateEmail", {
  method: "POST",
  credentials: "include",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ forwardTo: "attacker@example.com" })
});
```
3. Since the web malcious web page is open in the same browser that stores the user's authenticated session cookie for `mailbox.thm`, the request is processed as if it's coming from a legitimate user.
4. The attacker now has access to the victim's emails.

## Basic CSRF Exploitation
A covert technique known as hidden link/image exploitation in CSRF involves an attacker inserting a 0x0 pixel image or a link into a webpage that is nearly undetectable to the user.

```html
<!-- Website --> 
<a href="https://mybank.thm/transfer.php" target="_blank">Click Here</a>  
<!-- User visits attacker's website while authenticated -->
```

![image](https://github.com/user-attachments/assets/4bcd0b2e-b76c-4836-97f5-25364e1c3dcf)

The insecure code from the application may look like this

```php
<?php 
<form action="transfer.php" method="post">

    <label for="to_account">To Account:</label>
    <input type="text" id="to_account" name="to_account" required>

    <label for="amount">Amount:</label>
    <input type="number" id="amount" name="amount" required>

    <button type="submit">Transfer</button>
</form>
```

As we can see, there is no check for the CSRF token for every request made to the application.

Hence, by using the hidden image technique, attackers are able to make unauthorized request on behalf of users.


## ANSWER THE QUESTIONS

![image](https://github.com/user-attachments/assets/721f4b3e-a8b4-4b84-a551-326abceba9b8)

-> `d`

**Does the attacker usually know the web application requests and response format while launching a CSRF attack (yea/nay)?**

-> `yea`

**What is usually the extension of a malicious flash file used during a CSRF attack?**

-> `.swf`

**Which type of CSRF exploitation is carried out when operations are initiated without a complete page request-response cycle?**

-> `asynchronous`

