# AWS LAMBDA

- AWS Lambda is a serverless, event-driven compute service that allows us to run code for virtually any type of application /backend service without provisioning servers

## The Lambda Event model
- AWS instaniates a new [execution environment](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtime-environment.html) when a Lambda function is first invoked. Then the execution environment will be used for subsequent requests for a period of time.
- There are two inputs of the invocations: "Event" (the event that triggers the functions) and "context" (function names, logging information, function timeout, etc.).

## Components of Lambda
### Code
- Stored as zip file in S3
- Every code package must havea file name specified by the handler, and in that file, a function or method sepcified by the handler.

### Test events
- We can configure test events for writing and troubleshooting code in AWS console

### Memory and timeout
- Memory can be allocated to the function (128MB - 10GB) -> CPU capacity allocated by the execution environment based on the allocated memory

### Runtimes
- Every Lambda function has a selected runtime (most popular are Python and JavaScript)

### Role
- The [Execution Role](https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html) is a set of predefined permissions the function has permission to act on resources in AWS account.
- We must explicitly define the ability to write logs to CloudWatch logs in the Lambda Execution Role.

### Environment variables
- AWS Lambda allows configuring environment variables as part of Lambda runtimes -> same zipped file can be used across environments.
- `lambda:GetFunction` API call will also grant you a copy of the environment variables and values.
- Environmental variables are encrypted by AWS Key Management Service (KMS)

### Invocation Policy
- Lambda function can have resource-based policy that defines who/what can call the `lambda:InvokeFunction`.

### Logging
- The Lambda service will log any data written by the functions to STDOUT/STDERR to CloudWatch Logs.
- Each function will write its logs to a log group called `/aws/lambda/$function_name`

### VPC
- AWS Lmabda functions are assigned a public IP address. It is also possible to have a function invoked insde a VPC with a private IP address.

### Lmabda Function URLs
- HTTPS endpoint to Lambda function, allowing it to beinvoked over the Internet.
- Can be invoked with/without IAM Authentication.

## Lambda misconfurrations and attack vectors
- A lot of Lmabda functions execute based on an even tthat is user generated. If the code doest not validate user's input, Lambda function could be compromised.
- When code writes sensitive data to STDOUT, which would appear in the CLoudWatch logs for the function and be visible to those who has read access.
- If least privilege principle is not applied to a Lambda function, attackers can leverage the excessive permisions to discover and exploit more vulnerabilities.
- Roles permissions are available via environmental variables (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_SESSION_TOKEN). If these are leaked to attackers,they would be used for privilege escalation.
- How Lambda function is invoked can be a security misconfiguration if the resource policy is misconfigured. Usually, resource policies are used with `lambda:invokeFunction` IAM action, but if we used `lambda:*`, the principal would have the ability to upload new code. If the resource policy allowed all AWS users (principal:*), then we'd have a big security risk.
- When calling `lambda:GetFunction` API, we'll find part of the response is a pre-signed URL to download the Code zip file from the Lambda service's S3 bucket -> discovery tactice as developers may hardcode things in their applications.

# ANSWER THE QUESTIONS
- **Go to the AWS Lambda Page in your account named TryHackMeLambdaRoom-sample-function. Generate a "hello-world" test event, and invoke the lambda. See what information is returned. What is the value of the context key "memory_limit_in_mb"?**

![image](https://github.com/user-attachments/assets/1af3b478-c8f0-458f-9608-884eca2c9ee9)

-> `128`

- **Save the value of invoked_function_arn**

-> `arn:aws:lambda:us-east-1:637423357278:function:TryHackMeLambdaRoom-sample-function`

### Using the AWS CLI, investigate this lambda function in another account
```bash
aws lambda get-function --function-name arn:aws:lambda:us-east-1:019181489476:function:sample-lambda
```

- **What is the RunTime of the function?**

![image](https://github.com/user-attachments/assets/cd44b874-c056-4c37-91bc-2451a5f2c59b)

-> `Python3.7`

- **What are the first two sentences of the error message you received when the get-function command tried to read the environment variables?**

-> `Lambda was unable to decrypt your environment variables because the KMS access was denied. Please check your KMS permissions.`

- **Using curl, download the zip file referenced by the Code Location. Open the file, and enter the contents of the "question3.txt" file.**

-> `Of all the lambda functions in all the accounts in all the regions, you had to download mine.`

- **The handler function is missing from the zip file. What should the filename be?**

  ![image](https://github.com/user-attachments/assets/435ae003-c1cc-4389-9819-ae6afab43d7c)

-> `function.py`

- **Using the command "aws lambda get-policy --query Policy --output text --function-name <function arn from task 3>" retrieve the invocation policy for this sample function. What is the Action for the most permissive Statement?**

![image](https://github.com/user-attachments/assets/9d071a87-4af2-4d42-8c33-9963a2ae985a)

-> `lambda:UpdateFunctionCode`

- **In your account, there is a function named "TryHackMeLambdaRoom-envars-function" Invoke this function (via the console). What is the value of SECRET_CONNECTION_STRING?**

Run the following command to invoke the function and save it into a json file.
```bash
aws lambda invoke --function-name TryHackMeLambdaRoom-envars-function output.json
```

![image](https://github.com/user-attachments/assets/c7d2cf3a-b606-48e6-83fd-9cce947868c8)

View the content and we'll figure out the SECRET_CONNECTION_STRING

![image](https://github.com/user-attachments/assets/b7ab946b-ee7c-44a2-bae6-704542e4431b)

-> `https://falken:joshua@wopr.norad.mil/globalthermonuclearwar`

- **What file is deployed by the Lambda Layer attached to the "TryHackMeLambdaRoom-envars-function"?**

In the AWS Console, invoke the Lambda function, we'll find the file that is deployed by the Lambda Layer.

![image](https://github.com/user-attachments/assets/69d86414-dfe8-4aeb-a04b-41809a474b85)

-> `flag.txt`

- **Modify the "TryHackMeLambdaRoom-envars-function" to echo the contents of the flag.txt**

View the Lambda function, we see the command run within the Lambdafcuntion is `ls /opt`

![image](https://github.com/user-attachments/assets/ea7a312e-1106-48d2-9120-58bfb855e28a)

Change the command to `cat /opt/flag.txt` and we'll get the answer.

-> `The only winning move is not to play`
