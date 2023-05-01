---------------------------
- WIndows Remote Management is a simple Windows integrated remote management protocol based on the command line
- Use Simple Object Access Protocol (SOAP) to establish cononection between hosts and applications.
- Relies on TCP #5985 & 5986 (use HTTPS)
- Windows Remote Shell (WinRS) is sued to exeute arbitrary commands on the remote system.
---------------------------------

- Footprinting the Service
```bash
sudo nmap -sV -sC $IP -p5985,5986 --disable-arp-ping -n
```

- evil-winrm
```bash
evi-winrm -i $IP -u $user -p $pass
```
