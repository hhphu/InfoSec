# Grep & Sed & Awk mini prokjects
- This is an introductory project that helps me get familiar with the most three basic yet powerful commands in Linux: grep, sed and awk. These thre commands give me the ability to look through files, search for data and extract them for analysis and reports.
- Resources: [Admin_logA.txt](./Admin_logA.txt) and [Admin_logB.txt](./Admin_logB.txt)
- Tasks:
	1. Combine the two files into one file called `Admin_logs.txt`
	2. Use `sed` command to replace **INCORRECT_PASSWORD** with **ACCESS_DENIED** and print the output to the new file `sed_admin_logs.txt`
	3. Use `awk` command to filter out the date and the username in the `sed_admin_logs.txt` and print the output the the new file `awk_admin_logs.txt`

-----
## Solutions
1. Combine the two files into one file called `Admin_logs.txt`
```bash
cat Admin_logA.txt Admin_logB.txt >> Admin_logs.txt
```

2. Use `sed` to replace the string
```bash
sed 's/INCORRECT_PASSWORD/ACCESS_DENIED/' >> sed_admin_logs.txt
```

3. Use `awk` to filter out the date and username in the log file
```bash
awk '{ print $4, $6}' sed_admin_logs.txt >> awk_admin_logs.txt
```

![solutions](./solutions.png)
