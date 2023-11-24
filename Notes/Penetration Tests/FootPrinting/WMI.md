---------------------------------
- Windows Management Instrumentation (WMI) operates over RPC, which is port 135
- WMI is used to run command with Powershell
-----------------------------------

### Footprinting the Service
- WMIexec.py
```bash
/usr/share/doc/python3-impacket/examples/wmiexec.py $USER:$PASS@$IP HOSTNAME
```
----------------------------------------

- Gather remote processes on machine
	```Get-WmiObject Win32_Process -ComputerName WINDC01```
- To get a better view, save the output in a variable and viet the .Name property
	```$list=Get-WmiObject Win32_Process -ComputerName WINDC01```
	```$list.Name```
* Gather Services on a machine
	```Get-WmiObject Win32_Service -ComputerName WINDC01```

- In Metasploit, use ```scanner/smb/impacket/wmiexec ``` module 


