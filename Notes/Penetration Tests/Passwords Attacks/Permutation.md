-----------
# Hashcat
------------------------
- Generate Rule-based Wordlist using Hashcat
```bash
hashcat --force password.list -r custom.rule --stdout | sort -U > mut_password.list
cat mut_password.list
```

- Hashcat Existing Rules
```bash
ls /usr/share/hashcat/rules
```

-------
# CeWL
--------------
- Scan potential words from the company's website and sve them in a separate list, which can be combineed with rules to create customized password.
```bash
cewl https://www.inlanefreight.com -d 4 -m 6 --lowercase -w inlane.wordlist
	-d: the depth to spider
	-m: minimum length of the word
	-w: store result in an output file.
```
