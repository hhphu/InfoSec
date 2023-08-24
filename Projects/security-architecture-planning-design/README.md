# Security Architecture Planning and Design
In this project, I demonstrate my new security architecture skills by conducting a security assessment. I was given an initial design that contains multiple problems. I will identify the risks and policy violations in this design, and then recommend a new, secure design that mitigates the risks and gets any policy violations into compliance – all while still satisfying the underlying needs of the business.

## Scenario
I need to perform a security assessment on a new Customer Information Management System (CIMS). This system has a number of pieces we need to consider, including the database itself, the surrounding architecture, and the users.

There are three categories of users:
- Customers – who need to be able to enter and update their individual information .
- Customer relationship managers – who need to be able to access and update all customer information.
- Data scientists – who need the data for business intelligence.

All of the details are provided in the [scenario document](./scenario-conduct-an-application-security-review.pdf)

A few key things to note:
- The database is optimized for usability—which means it may address the business needs, but there has been no security review (that's your job!).
- The system involves financial data, so it is bound by Sarbanes-Oxley. I need to ensure that any financial data is protected and auditable
- Because the database holds customer credit card information to process payments, I also need to consider PCI DSS.

## Main Steps
1. Identify the needs. These are the requirements of the users that cannot change and that need to be included in the new design.
2. Identify risks and design mitigations. The initial design may have multiple security risks, so you'll need to figure out what they are and how to address them.
3. Check for policy violations and ensure compliance. In particular, you'll need to make sure the final design doesn't violate Sarbanes-Oxley or PCI DSS.
 
Report of the assessment can be found [here](./Conduct%20an%20Application%20Security%20Review.pdf).
