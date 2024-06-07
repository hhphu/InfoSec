# Project Overview

1. Perform an automated vulnerability scan and upload results to the Faraday for analysis
Run a custom scan as per [Policy_NS_Q3](./updated-policy-ns-q3.pdf) . You'll need to use an Advanced Scan to configure this.
Export the Nessus scan results as .nessus file.
Use the Nessus Plugin in the Faraday client to import the Nessus Scan and manage it.
Note: Credentials for Faraday are root:toor

2. Perform a manual assessment on services flagged as high or critical
Run the scan per [Policy_VA_Q3](./policy-va-q3.pdf)
Use only the trusted sources given in the Policy_VA_Q3 for this assessment. Anything not on the list of trusted sources is considered unsafe as per company rules. For example, using Github to download exploits/PoC is allowed but using ExploitDB is not.
Use only the tools and programs listed in the Tools & Programs Allowed list
Test only code execution vulnerabilities on the service rated high or critical in the Nessus scan.
Modifying code is allowed.

3. Audit web application(s) per Policy_VA_Q3
Port 80 and 443 are open on the target machine. Your goal is to test the web application running on those ports.

4. Prepare an Assessment Report per Policy_VA_Q3

------
[REPORT](./Audit_Example_Corp_v3.pdf)
