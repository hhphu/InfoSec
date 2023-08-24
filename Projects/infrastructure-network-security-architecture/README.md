# SCENARIO
The Water & Power Organization(WPO) audits and maintains the billing and usage of its customers with an application that allows its field agents to upload the picture of the meters attached in customer's houses.
In the backend, the uploaded images are then analyzed by WPO's Machine Learning system to automatically detect the meter readings and verify the customer's actual water and electricity usage.
At a technical level, as soon as a field agent uploads an image through the application, it gets stored onto an S3 bucket. An SQS queue is used to maintain a FIFO(first in the first queue) queue of images to be processed by the image processing server. Once the queued image is picked up by the server, the following actions are performed in a sequence:
1. The image is scanned against ClamAV antivirus from any accidental infection of images from the agent's devices.
2. Once marked as clean by ClamAV, the image file gets processed by the Machine learning algorithm.
3. The metadata and reading information is then extracted and updated to a DynamoDB database.

# OBJECTIVES
Throughout this project, I need to complete the following tasks:
- Harden S3 bucket
- Plan the defense layer
- Integrate Yara scanning
- Integrate Defense-In-Depth
- Redesign the architecture to achieve a more secure application.

# SET UP
We need to create a stack for this project. Run the following command in the terminal, from the same directory where you've placed your lab.template.yaml file. It will create all resources defined in the lab.template.yaml file. All resources logically combined together is called a stack.
```bash
aws cloudformation create-stack  --stack-name myStack --region us-east-1 --template-body file://lab.template.yaml --capabilities "CAPABILITY_IAM" "CAPABILITY_NAMED_IAM"
```
Describe the stack
```bash
aws cloudformation describe-stacks --stack-name myStack
```

# REPORT
The report of this project can be found [here](./INSA-Planning-Design.pdf).
