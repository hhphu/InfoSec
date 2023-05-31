An extensive list of archive types can be found [here](https://fileinfo.com/filetypes/compressed).

### Download ALl File Extensions
```bash
curl -s https://fileinfo.com/filetypes/compressed | html2text | awk '{print tolower($1)}' | grep "\." | tee -a compressed_ext.txt
```

## Cracking Zip
```bash
zip2john ZIP.zip >> zip.hash
john --wordlist=rockyou.txt zip.hash
john --show zip.hash
```

## Cracking OpenSSL Encrypted Archives
- Using a for-loop to Display Extracted Contents
```bash
for i in $(cat rockyou.txt); do openssl enc -aes-256-cbc -d -in GZIP.gzip -k $i 2>/dev/null | tar xz; done
```

## Cracking BitLocker Encrypted Drives
- [BitLocker](https://docs.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-device-encryption-overview-windows-10) is an encryption program for entire partitions and external drives. Microsoft developed it for the Windows operating system. It has been available since Windows Vista and uses the `AES` encryption algorithm with 128-bit or 256-bit length. If the password or PIN for BitLocker is forgotten, we can use the recovery key to decrypt the partition or drive. The recovery key is a 48-digit string of numbers generated during BitLocker setup that also can be brute-forced.

- Virtual drives are often created in which personal information, notes, and documents are stored on the computer or laptop provided by the company to prevent access to this information by third parties. Again, we can use a script called `bitlocker2john` to extract the hash we need to crack. [Four different hashes](https://openwall.info/wiki/john/OpenCL-BitLocker) will be extracted, which can be used with different Hashcat hash modes. For our example, we will work with the first one, which refers to the BitLocker password.

```bash
bitlocker2john -i Backup.vhd > backup.hashes
grep "bitlocker\$0" backup.hashes > backup.hash
cat backup.hash
```

- Using hashcat to crack backup.hash
```bash
hashcat -m 22100 backup.hash /opt/useful/seclists/Passwords/Leaked-Databases/rockyou.txt -o backup.cracked

# View the cracked hash
cat backup.cracked
```
