# AWS API Gateway

## Introduction
### API Components
- Endpoints - this is the URL location of the API where users can make a call to access resources
- Method - specifies the type of request being made to an API endpoint
## AWS API Gateway
- API Gateway is a service provided by AWS to assist users to deploy REST, HTTP/S and WebSocket API using serverless infrastructure.
- WebSocket API stands out for its two characteristics: bi-directional and real-time communications.
- Headers - components of HTTP, used by APIs to contain additional information about the request
- Request body: includes data sent to an API as part of the request. GET requests don't usually have a body while POST, PUT and DELETE do.
- Response - Data that the API responds back to the end users, which includes status code, headers, and response body.

### ANSWER THE QUESTIONS
- **What is the URL location of an API called?**
-> `endpoint`
- **What request type commonly doesn't include a request body?**
-> `GET` 

## AWS Lambda's integration with APT Gateway
- AWS API Gateway oftens integrates with AWS Lambda fuction (which is a default AWS serice proxy for API Gateway endpoints).
- Lambda [authorizer](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html) - determines who can access the endpoints behind an API Gateway and what resources they can request to access.
- When misconfigured, Lambda authorizer may allow unintended & unauthorized access to resources behind the API Gateway.

### ANSWER THE QUESTIONS
- **What does the WebSocket API additionally allow, compared to REST or HTTP/S APIs?**
-> `bi-directional communication`
- **What default function does Lambda perform for API Gateway endpoints?**
-> `aws service proxy`
- **What is a special secondary function of Lambda?**
-> `authorizer` 

## Common services integrations with API Gateway
API Gateway can be integrated with various AWS services for different purposes:
- Serverless Architecture - can be integrated with Lambda to build serverless applications, where Lambda fuction is triggered by API Gateway to process incoming requests and return responses
- Mircorservices - API Gateway can be used to create, deploy and manage APIs for microservices, allowing for easier communication and integration between services
- Data storage & retrieval - API Gateway integrates with Amazon DynomoDB and Amazon S3 to provide seamless access to stored data.
- Real-time communication - API Gateway can be used with WebSockets to provide real-time, bi-directional communication between clients and servers.
- API Management - API Gateway provides tools for monitoring, loggin and managing APIs, making it easer to understand and control API usage.
- Security - API Gateway provides robust security features, including OAth 2.0 and AWS Identity and Access Management (IAM) integration for access control, SSL/TLS encryption for data in transit.

### ANSWER THE QUESTIONS
- **What are the two aspects that WebSockets for API Gateway provides? (Answer format: ANSWER1, ANSWER2)**
-> `real-time, bidirectional communication`

## Using API Gateway for offensive purposes
AIP Gateway can be used as "passthrough" proxy, which rotates IP addresses from a given pool of IPs, which can be valuable for security testers in several ways:
- **Bypassing IP-based restriction** -  Some application can block requests from an IP address if malicious activities are detected. By rotating IP addresses, testers can bypass these restrictions.
- **Evading detection** - Once malicious activities are detected, the IP is blacklisted by the systems. By rotating IP addressses, security testers can evade detection and continue their tests.
- **Simulating real-world scenario** - An application is accessed by from different IP addresses. By rotating IPs, testers can simluate scenarios that are closest to the real worlds, which provides them more accuracy in terms of testing.
- **Fireprox** - a common tool used for rotating IP addresses.

```bash
# Installation
git clone https://github.com/ustayready/fireprox
cd fireprox
pip3 install -r requirements.txt


# Configure AWS account
aws configure

# Run the command to create a proxy
python fire.py --command create --url https://api.bestcloudcompany.org

# the proxy URL will be generated, which can be used for testing
https://bnyqzbg5pc.execute-api.us-east-1.amazonaws.com/fireprox/

# Once done with the test, clean up
python3 fire.py --command delete --api_id bnyqzbg5pc

# To get teh api_id value, run
python fire.py --command list
```

### ANSWER THE QUESTIONS
- **What is the serverless capability that AWS API Gateway represents?**
-> `reverse proxy`
- **What does rotating IP addresses allow you to bypass?**
-> `IP-based restrictions`

## Attacking Lambda Authorizers on API Gateway
- Lambda Authorizers provides authorization for API request. Lambda authorizers function is executed before and API request is processed, and it returns a policy document that specifies whether the request is authorized or not.

### Greedy Expansion
- For convenience, Lambda Authorizer often uses `*``, which is known as greedy operator that matches zero or more characters in a string. When used in matching URL paths, this can lead to unexpected matches if not used carefully. As a result, attackers can get access to resources from certain API endpoints when they're not supposed to.

### Exploiting bestcloudcompany.org API endpoints
- Navigate to https://api.bestcloudcompany.org to read the company's API documentation.

![image](https://github.com/user-attachments/assets/e08e3e9b-460f-4545-b44f-e0fbf3630b74)

- From the document, we see that there are several endpoints to be tested: **`/test/test/`**, **`/test/admin`** (user **`test`** and **`admin`** on **test stage**) & **`/prod/test`**, **`/prod/admin`** ((user **`test`** and **`admin`** on **production stage**).
- On top of that, we need a header to make API call: **`authorizationToken:testing123`**

```bash
curl -H "authorizationToken:testing123" https://api.bestcloudcompany.org/test/test
```

![image](https://github.com/user-attachments/assets/8c878753-f70c-4ab5-8491-e5d32ecdad0b)

- It looks like the value of **`api_key`** is being used as the **authorizationToken header**.
- Let's try to retrieve the admin's **`api_key`** on the **test stage**

```bash
curl -H "authorizationToken:testing123" https://api.bestcloudcompany.org/test/admin
```

![image](https://github.com/user-attachments/assets/e2f8a685-1ff4-468e-bc98-f9b405ae0be2)

- Trying these **api_key's** values as **authorizationToken header**'s values to access **`test`** and **`admin`** user on **prod stage**. As expected, we are not authorized to view such resources.

![image](https://github.com/user-attachments/assets/7f0b621a-28a9-499a-8b11-a6475f0a8bc3)

- Assume we can view the Lambda authorizer policy, we can actually spot the vulnerability

```bash
if event['authorizationToken'] == 'testing123':
        auth = 'Allow'
        authResponse = {"principalId": "testing123", "policyDocument": {"Version": "2012-10-17", "Statement": [
            {"Action": "execute-api:Invoke",
             "Resource": "arn:aws:execute-api:us-east-1:{ACCOUNT_ID}:*/*/test/*",
             "Effect": auth}]}}
        return authResponse
    elif event['authorizationToken'] == ‘{PROD_AUTH_TOKEN}’:
        auth = 'Allow'
        authResponse = {"principalId": "testing123", "policyDocument": {"Version": "2012-10-17", "Statement": [
            {"Action": "execute-api:Invoke",
             "Resource": "arn:aws:execute-api:us-east-1:{ACCOUNT_ID}:*/*/prod/*",
             "Effect": auth}]}}
        return authResponse
```

- Look at the policy for `authorizationToken:testing123`, we see that users can access all resources as specified **`arn:aws:execute-api:us-east-1:{ACCOUNT_ID}:*/*/test/*`**

- The URL **https://api.bestcloudcompany.org/test/test** satisfies the **`*/*/test/*`** regex. The interesting thing is, this URL **https://api.bestcloudcompany.org/prod/test/** also satisfies the regex pattern. This means we can get the **`test`** user's api on **prod stage**. We can actually confirm this:

![image](https://github.com/user-attachments/assets/02b54f82-28e2-4aee-b2c7-e7203c88c6cd)

- We found **`test's api_key`** on **prod stage**: `16c7d47c2d1248dc8504219441e3d23f`
- We can now use this newly acquired api_key to check for the **`admin`** on **prod stage**

```bash
curl -H "authorizationToken:16c7d47c2d1248dc8504219441e3d23f" https://api.bestcloudcompany.org/prod/admin
```

![image](https://github.com/user-attachments/assets/5b83c10f-2d73-4355-a5dd-e67cbd5cd4c0)

- And we get it, without having John provide us the password. In this case, the greedy operator are used in an unexpected way to exploit the API endpoint, hence gaining access to unauthorized resource.

### ANSWER THE QUESTIONS
- **What is the api_key for the /test/test user?**
-> `testing123`
- **What is the api_key value for the /test/admin user?**
-> `2008951f220d4c8d9877bb979d560342`
  - **What is the api_key value for the /prod/admin user?**
-> `af84b63da20b4d04a62aca8abdfc3813`
