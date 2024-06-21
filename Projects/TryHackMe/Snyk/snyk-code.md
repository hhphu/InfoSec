# Snyk Code
Securing code with Snyk - a junior application security engineer's journey.

## Code Security Risks
- **Complex codebases:** With applications serving business needs, the codebases sometimes can be huge and complex, which can obscure the vulnerabilities, making them harder to detect and remediate.
- **Insufficient security practices:** A lot of developers prioritize functionalities over security in their codes, especially in high-pressure environments. This can result in insufficient coding practices and standards, making the applications vulnerabile to security risks.
= **Limited external scrutiny:** Codebases within a company do not have the "many eyes" principle that supports open-source security, it is easier to have security issues go unoticed for a long period of time, increasing the risk of Zero-day vulnerability.
- **Dependency on third-party components:** It is common that companies use third-party libraries/frameworks, which can introduce vulnerabilites.
- **INternal knowledge gaps:** Team may lack expertise in secure coding practices or unaware of the latest security threats and mitigation strategies.

## Remediating Vulnerabilites
### AI-Generated Code Scrutiny
AI-Generated codes can introduce security risks. Hence it is important to audit these codes:
- Manual review: encourage manual inspection of all AI-generated code, focusing on security-sensitive sections
- Pair programming: implement pair programming for AI-generated code sections, combining AI efficiency with human scrutiniy insight.
- Security testing integration: Integrate automated security testing tool like SnykCOde, ensuring immedate feedback on potential vulnerabilities introduced by AI.

### Strategic Vulnerability Prioritization
- Business logic consideration: Prioritize vulnerabilities directly affecting business operations/exposing business data
- Feature-focus enhancement: Some features of the applications are more important than others. Hence, it is important to prioritize vulnerabilites affecting those features.

## Establish Best Practices
### Refine Security Policies for propriety and AI-Generated code
- With the growing of AI, we should have policy to include AI-generated code segments in security testings. 
- There should also be guideline for secure coding practices when it comes to AI-generated code.

### Enhance Collaborations Across Teams
- Use [OWASP Security Champions Playbook](https://github.com/c0rdis/security-champions-playbook) to establish cross-functional security forumes where developers, security team members and AI specialists can share insights, discuss new security trends and collaborate on secure coding practices.

### Measure the impact of Security Tool implementation
- When it comes to implementing Security Tools, there are a great number of factors to consider. Use the following frameworks as a guideline:
	- Cost reduction: Calculate the costs associated with security before vs after the implementation (remediation, fines, downtime, etc.)
	- Efficiency gains: the time saved by developers and security team in identifying & addressing vulnerabilities through automated scans and integrations. 
	- Preventive savings: Estimate the costs of potential security breaches that were avoided due to proactive vulnerability management. 
	- ROI formula: use the following formula to calculate ROI
  		![](https://tryhackme-images.s3.amazonaws.com/user-uploads/600495397be6737041128e4a/room-content/04231fc8f30425714af6631f4c43d8cd.png)


## ANSWER THE QUESTIONS
- How many vulnerabilities are flagged on the search-feature.js file?

-> 4

- How many high-severity vulnerabilities are flagged on the search-feature.js file?

-> 2

- What are the two medium-severity vulnerabilities flagged on the search-feature.js file? (in alphabetical order)

-> Cross-Site Request Forgery, Information Exposures

- What is the CWE for Cross-Site Scripting?

-> CWE-79

- What is the CWE for SQL Injection?

-> CWE-89

- WHat is the unsnitised user input in the chat-controller.js file?

-> searchTerm

- What is the new vulnerability introduced with the XSS fix?

-> Allocation of resources without limits or throttling

- Which Express method is used to fix the XSS vulnerability in the code snippet?

-> res.render

- What is the updated code in the code snippet using to fix the SQL injection?

-> Parameterised queries

- Establishing sensible alert thresholds in continous monitoring practices involves considering the severity, frequency, and rate of change of vulnerabilites (y/n)

-> OWASP Security Champions Playbook

