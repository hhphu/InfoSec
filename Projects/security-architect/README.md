# Security Architect

![HeaderImage](https://media.licdn.com/dms/image/D4E12AQFD_We6L5APAw/article-cover_image-shrink_600_2000/0/1676991484108?e=2147483647&v=beta&t=a5wr0yTmC9i5qKhityROd6TDdKmP6u1jHGsZpaRki6I)

These mini projects equip me skills and strategies to implement elements of security infrastructure design and management at an enterprise level. As a security architect, I will be charged with designing security systems to thwart malware, hacker intrusions and Denial of Service attacks. The addressed security topics is concerned with architectural and implementation skills required by a skilled cybersecurity professional for critical use-cases like identity & access management, infrastructure security, threat detection and incident response.

1. [Security Architecture Planning and Design](./security-architecture-planning-design)
- This project introduces the fundamental security planning, design, and systems thinking concepts that are used throughout security architecture. As networks and applications grow more complex, the need to identify potential sources of weakness that are a product of that complexity becomes crucial. Upon completion, I obtained the skills to identify and evaluate risks in systems, assess whether or not risks are acceptable, and work alongside stakeholders to prioritize remediation efforts.
    - Conducted a security assessment to identify risks and policy violations in an existing Customer Information Management System (CIMS)
    - Provided recommendations for new designs for a more secure and robust architecture that is compliant with PCI DSS and SOX    

2. [Enterprise Identity and Access Control](./enterprise-identity-access-control/)
- This project focuses on identity and access management. As a security architect, implementing an organization-wide strategy for strong Identity and access management can greatly improve the security posture of the organization. IAM can be tricky to architect and implement. Too much access can lead to data exposure, whereas, too little access can lead to business hindrance. A fine balance is required while designing a strong IAM model.
    - Evaluated an access control matrix and restrictions to ensure that each role has the appropriate policies and permissions implemented with the principle of least privilege
    - Create an AWS Config rule that will alert on a policy that does not meet the organizational requirements

3. [Infrastructure and Network Security Architecture Planning and Design](./infrastructure-network-security-architecture/)
- In this project, I learned how to plan and build the architecture to ensure that an organization's security is up to date and well defended.
    - Hardened S3 bucket for a file upload application by creating a bucket policy that only allows the uploading of image files and denies any other filetype 
    - Implemented a Defense-in-Depth model for the file upload service by configuring Lambda functions to scan the bucket and allow matching the uploaded files against a pre-populated list of known bad files

4. [Incident Response and Business Continuity Architecture Planning, Design and Implementations](./incident-response-business-continuity/)
- In this project, I learned how to plan and implement incident response and business continuity in a cloud environment.
    - Developed and executed Incident Response Runbook including Incident Response Planning, Incident Response Actions, and Business Continuity Actions to address a critical data breach incident.
    - Enhanced incident preparedness measures to safeguard AWS cloud infrastructure (configuring and deploying Auto Scaling Groups for the LAMP servers), which guarantees business continuity.
