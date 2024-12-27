# JWT Security

# Token-based Session Management
- **Web applications** use cookie-based session management:
    - After authentication, the server includes the cookies in the request body that's sent back to client
    - The cookie is saved in the browser's LocalStorage
    - Every time the browser makes a new request, there will be a JavaScript code to retrieve the cookies and include it in the header.
    - Browsers have built-in features to implement security for these cookies sessions
    - JWT (JSON Web Token): is one of the most common tokens used nowadays, which can be passed through the header `Authorization: Bearer '$TOKEN`
 
### ANSWER THE QUESTIONS
**- What is the common header used to transport the JWT in a request?**

-> `Authorization: Bearer`

# JSON Web Tokens
- There are three parts in a JWT, each of which is base64 encoded and separated by a dot: **Header**, **Payload**, **Signature**
    - **Header**: indicate the type of token and the signin algorithm.
    - **Payload**: includes claims (a claim = a piece of information about a specific entry). Hence, sometimes these JWT include sensitive information.
    - **Signature**: provide a method for verifying the token's authenticity. This can be None (no algorithm is used, Symmetric (using 1 secret key for both client and server like HS256), Assymetric (using public-private key pairs like RS256)
- JWE =  Encrypted JWT

### ANSWER THE QUESTIONS
- **HS256 is an example of what type of signing algorithm?**

-> `symmetric`

- **RS256 is an example of what type of signing algorithm?**

-> `assymmetric` 

- **What is the name used for encrypted JWTs?**

-> `JWE` 

# Resources
- In the follow example, there will be two useful resources I recommend using as they help us understand the vulnerabilities and how to mitigate them.
- https://jwt.io/ - This helps us quickyly decode the JWT and see their values
- Python's pyjwt - A Python module that is used to create JWT. We will be looking at some vulnerable codes as well as how to fix them

## JWT Vulnerabilities
## Sensitive Information Disclosure
- IN cookied-based sessions, server store the values of the tokens. Hence, these information are not publicly exposed on the client-side.
- JWT, since processed on the client-side, if not carefully implemented, may expose sensitive information like users' credentials, privileges, network configurations,etc.

**Demonstration**

```bash
curl -H 'Content-Type: application/json' -X POST -d '{ "username" : "user", "password" : "password1" }' http://10.10.53.116/api/v1.0/example1
```

![image](https://github.com/user-attachments/assets/aa82e694-6951-4e5e-b036-79e8579bd0f8)

- Copy the token values into [JWT.io](https://jwt.io/), we see its content, which exposes some senitive information:

  ![image](https://github.com/user-attachments/assets/fa8a621f-55f2-47cf-b3be-6638fdbbfa35)

**Vulnerable**
- This is how the vulnerable code looks like

```bash
payload = {
    "username" : username,
    "password" : password,
    "admin" : 0,
    "flag" : "[redacted]"
}

access_token = jwt.encode(payload, self.secret, algorithm="HS256")
```

**The Fix**
- Sensitive information should not be added as claims of the JWT. Instead, they should be securely stored in the server-side. When needed, they can be read and looked up from the server

```bash
payload = jwt.decode(token, self.secret, algorithms="HS256")

username = payload['username']
flag = self.db_lookup(username, "flag")
```
### ANSWER THE QUESTIONS
- **What is the flag for example 1?**

-> `THM{9cc039cc-d85f-45d1-ac3b-818c8383a560}`

## Signature Validation Mistakes

