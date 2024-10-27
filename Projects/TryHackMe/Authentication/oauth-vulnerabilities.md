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

	- **`client_id`**: the unique identifier for the client application **`CoffeeShopApp`**
   	- **`return_type=code`**: indicates the **`CoffeeShopApp`** is expecting the returned authorization code.
	- **`state`**: the CSRF token for the request and the response
   	- **`redirect_uri`**: The URL where the authorization server will send users after he grants permission. This must match one of the pre-registered redirect URIs for the client application.
   	- **`scope`**: Specifies the level of access requested, such as viewing coffee orders.
- 




-----

# ANSWER THE QUESTION
**- Which optional parameter can be used to prevent CSRF attack?**

`-> state`

**- What credentials can the client use to access protected resources on behalf of the resource owner**

`-> access token`

**- What is the grant type often used for server-server interaction?**

`-> client credentials`
