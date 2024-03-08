# wpscan
- [WPScan](https://github.com/wpscanteam/wpscan) is an automated WordPress scanner and enumeration tool. It determines if the various themes and plugins used by a WordPress site are outdated or vulnerable. 

- Installation
```bash
gem install wpscan
```

- Verify the installation
```bash
wpscan --hh
```

- WPScan can pull in vulnerability information from external sources to enhance our scans. Obtain an API token from [WPVulDB](https://wpscan.com/) to scan for vulnerability and exploit PoC. The token can be used with __wpscan__ command with __--api-token__ parameter.

- Scan the target
```bash
wpscan --url http://blog.inlanefreight.com --enumerate --api-token Kffr4fdJzy9qVcTk<SNIP>
```

- Credentials attack
  ```bash
wpscan --password-attack -t 20 -U $NAME/$NAME_LIST -P $PASS/$PASS_LIST --url $TARGET --api-token $TOKEN
  ```
