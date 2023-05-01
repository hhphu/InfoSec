## Web Servers
----------------------------------------
- HTTP Headers
```bash
curl -I "http://${TARGET}"
```

- WhatWeb
```bash
whatweb -a3 https://www.facebook.com -v
```

- WafW00f
```bash
# Installation
sudo apt install wafw00f -y

# Running the command
wafw00f -v -a https://www.testla.com
```

- Aquatone
```bash
# Installation
sudo apt install golang chromium-driver
go get github.com/michenriksen/aquatone
export PATH="$PATH":"$HOME/go/bin"

# cat the subdomain list and pipe the command to aquatone
cat facebook_aquatone.txt | aquatone -out ./aquatone -screenshot-timeout 1000

# when finished, we get aquatone_report.html to view the results.
```
