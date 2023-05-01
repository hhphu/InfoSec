------------------------------------------------
- fast and efficient tool for locally and remotely copying files.
- Default port = 873
------------------------------------------------------------

- Scanning for Rsync
```bash
sudo nmap -sV -p873 127.0.0.1
```

- Probing for Accessible Shares
```bash
nc -nv 127.0.0.1 873
```

- Enumerate an Open Share
```bash
rsync -av --list-only rsync://127.0.0.1/dev
```

- To get all the files from the remote host
```bash
rsync -av rsync://127.0.0.1/dev

# if rsync is configured to use SSH to transfer files, we can modify our commands to include the -e ssh flag or -e "ssh -p2222" if a non-standard port is used.
```
