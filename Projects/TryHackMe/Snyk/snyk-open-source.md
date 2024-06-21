# Snyk Open Source
## Securing open-source dependencies with Snyk - a junior application security engineer's journey.

## Open Source security risks
- **Large attack surface:** An application can use hundreds or thousands of frameworks and libraries. Hence, it requires a great amount of resources to manage each of these dependencies, which can sometimes be overwhelming. One package/library may introduce a small vulnerability, but it may severely affect the applicaions.
- **Fast-paced release cycles:** Because of bugs and securities, open-source libraries/frameworks frequently push out patches and updates. Falling behind on patching can expose our applications to security risks.
- **Transitive dependencies:** A lot of libraries/frameworks depend on others. When left unmanaged, transitive dependencies can harbor unknown vulnerabilites propagating throughout an entire system.
- **Limited visibility:** When struggling to keep track of the open-source components, developers may overlook some components and fail to detect vulnerability. Teams may also do not notice that they're using outdated versions, which may pose security issues.

## Diving Deeper Into Vulnerablities
- Prototype Pollution: Injecting malicious codes into Java Script object prototype's properties.

```javascript
// Assuming global variable `Object.prototype.__proto__ = {}` exists
const pollutedObj = {
    __proto__: {
      // Adding a new property to Array.prototype
      length: 999,
    },
  };
const array = [];
array.__proto__ = pollutedObj;
console.log(Array.length); // Output: 999 instead of expected value
```

## Vulnerability Triage
- Apply CVSS: calculate the severity of the vulnerabilites using CVSS (Common Vulnerability Scoring Systems)
- Consider the context: Not every vulnerability has high risk to a company. Other factors should be taken into considerations (financial loss, data sensitivity, compliance and policies, etc.)
- Evaluate exploitability: How likely we can perform the exploit also plays a role in evaluating the vulnerability.
- Collaboration across disiplines: communications with other deparments fosters vulnerabilities triage process, helping the team to determine priorities.

## Addressing vulnerabilites
Once vulernerabilites are identified, we can use the following approach:
- Dedicated backlog: Establish a separate list of high-priority vulnerabilites requiring immediate attentions -> easy to track progress and manage vulnerabilites.
- Break down tasks into smaller chunks: Break the fixes into smaller chunks so it can be easier to test and reducing the change of introducing side effects.
- Implement CI/CD pipeline: Automate build, unit test and integrating testing processes. 
- Perform thorough manual testing: Manual testings covers edge cases, which helps us identify vulnerabilies from different angles. These manual tests should be run in Staging environment before carrying out to production environment.
- Monitoring: Continue to monitor the applications and their performances after deployment. Some patches may bring some side effects/slow down in performances.


-----
# ANSWER THE QUESTIONS
- Which JSON-formatted manifest file serves as the central hub for Node.js projects, listing metadata, scripts, and dependency declarations?

-> pakage.json

- How many dependencies do we have for this new feature?

-> 5

- Which term describes indirect pakace dependencies formed through shared prerequisites, possibly concealing vulnerabilities and demanind cautiouos assessment?

-> transitive dependencies

- What single authentication mechanism allows users to transition smoothly amongst various linked platforms and services?

-> single sign-on

- What is the version of teh vulnerable lodash package?

-> 2.4.2

- Which vulnerability allows an attacker to modify an Object?

-> prototype pollution

- What does CVSS stand for?

-> Common Vulnerability Scoring System

- Should the development team bulk fix all the vulnerabilities found in this new feature? (y/n)

-> n

- How does CircleCI help streamline pipeline configuration and standardization?

-> orb

What file defines the GitHub Actions workflow configuration that enables automation and customized sequences for building, testing and deploying?

-> yaml

- Which collaborative DevOps practice combines real-time communication channels, automation and operational agility?

-> Chatops
