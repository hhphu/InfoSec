# AWS LAMBDA

- AWS Lambda is a serverless, event-driven compute service that allows us to run code for virtually any type of application /backend service without provisioning servers

## The Lambda Event model
- AWS instaniates a new [execution environment](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtime-environment.html) when a Lambda function is first invoked. Then the execution environment will be used for subsequent requests for a period of time.
- There are two inputs of the invocations: "Event" (the event that triggers the functions) and "context" (function names, logging information, function timeout, etc.).


# ANSWER THE QUESTIONS
- **Go to the AWS Lambda Page in your account named TryHackMeLambdaRoom-sample-function. Generate a "hello-world" test event, and invoke the lambda. See what information is returned. What is the value of the context key "memory_limit_in_mb"?**

