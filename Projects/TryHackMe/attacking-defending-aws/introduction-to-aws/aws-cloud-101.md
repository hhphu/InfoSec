# AWS: Cloud 101

## Introduction
This room is intended to provide users who are not familiar with cloud technologies insight into some of the cloud's unique characteristics. Students in the room will learn about:
- How current cloud capabilities evolved from humble beginnings at AWS and other early internet companies.
- Why cloud technologies have changed how individuals and corporations interact with IT infrastructure.
- How business (non-tech) benefits have helped drive cloud adoption.
- Free resources and documentation that AWS has created for the public.
This information will help you become familiar with AWS even if you have never used a single cloud technology. These tasks will help you understand the broader story arc of where the cloud has been, is, and, therefore...where the cloud may be going.

## Notes
- Region: physical locations of AWS' clusters of data centers
- Availability Zone: multiple AWS data centers within a region, which can not be more than 60 miles apart.

### Data Severieignty
Diffrent countries have different laws and regulations regarding how Amazon store data. Data are also categorized based on their confidentiality level.

### Operational Expenses vs Capital Expenses
- Capital Expenses: major monetary spent on goods & services for the company to operate in a long period of times
- Operational Expenses: incurred as part of day-to-day operations, which vary.

### API mandate
- All teams within Amazon must communicate through APIs. These APIs must be usable for both Amazon employees and external users.
- The Two Pizza Team: Jeff try to enforce collaborations within teams, which requires smaller team size.
  
```bash
"We try not to create teams larger than can be fed by two pizzas"
```

### Serverless Services
- Low-code/No-code solutions: allow users to perform certain tasks with minimum configurations.
- Cost less compared to traditional resources.

## Answers the questions

**What decade did companies start having widespread reliance on internet-connected services?**

-> `1990s`

**Was EC2 Autoscaling the first autoscaling service in AWS? (yea/nay)**

-> `nay`

**How close together (in miles) should an Availability Zone's data centers be?**

-> `60`

**What continent has no AWS Region??**

-> `Antartica`                                                        

**What country has its own AWS partition?**

-> `China`

**Is a major purchase intended to be used by a business over a long period of time a capital expense or operating expense?**

-> `capital expense

**Who announced the "API Mandate" at AWS?**

-> `Jeff Bezos`

**What is AWS native "Infrastructure-as-Code" tool?**

-> `CloudFormation`

**Does serverless cost more or less when running idle than traditional servers?**

-> `less`

## View Site exercise
1. **Software Engineering Room**

![image](https://github.com/hhphu/TryHackMe/assets/45286750/2a0fb321-64ef-47e5-8c0f-3f46d23ae83e)

-> Answer: `us`

![image](https://github.com/hhphu/TryHackMe/assets/45286750/cabeaf16-6ee9-4132-bc3e-fea0e1c7ff87)

-> `Route 53`

![image](https://github.com/hhphu/TryHackMe/assets/45286750/41c3f8a7-5218-46fe-8087-e1445c78ecaa)

-> `API`

**2. DevOps Room**

![image](https://github.com/hhphu/TryHackMe/assets/45286750/2d39a86c-97b7-4b75-8092-34e2ab625a23)

-> Answer: `cloud`

![image](https://github.com/hhphu/TryHackMe/assets/45286750/a40bede9-7f72-40b5-bd96-7995cff16816)

-> Answer: `Lesser latency rate for website users and easy scalability as the userbase grows.`

**3. Finance Room**

![image](https://github.com/hhphu/TryHackMe/assets/45286750/68cdeb6f-ce73-45d5-b500-41680543bd51)

-> Answer: Optional`

Flags: **THM{AWS_CLOUD__00100}**

