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
- **What default function does Lambda perform for API Gateway endpoints?**
-> `aws service proxy`

