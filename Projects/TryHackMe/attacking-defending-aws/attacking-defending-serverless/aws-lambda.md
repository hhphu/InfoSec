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

## LAmbda misconfurrations and attack vectors


# ANSWER THE QUESTIONS
- **Go to the AWS Lambda Page in your account named TryHackMeLambdaRoom-sample-function. Generate a "hello-world" test event, and invoke the lambda. See what information is returned. What is the value of the context key "memory_limit_in_mb"?**

![image](https://github.com/user-attachments/assets/1af3b478-c8f0-458f-9608-884eca2c9ee9)

-> `128`

- **Save the value of invoked_function_arn**

-> `arn:aws:lambda:us-east-1:637423357278:function:TryHackMeLambdaRoom-sample-function`

