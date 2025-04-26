# Hammer

![image](https://github.com/user-attachments/assets/36179ea0-5003-4e31-bfa9-86aad857e8f0)

**URL:** https://tryhackme.com/room/hammer

## Set up
For convenience, I add the target's IP address to the hosts file so I don't have to kepe remember the IP

```bash
echo $IP hammer.thm >> /etc/hosts
```

## ENUMERATION
- Run an `nmap` scan on the target

```bash
nmap -A -p- hammer.thm
```

- We found that the application is running on port 1337

![image](https://github.com/user-attachments/assets/b3e937f4-4c1a-4c90-8bff-52ce2362c7c1)

- Inspect the page sources of the home page, we find the naming convention for the application

- ![image](https://github.com/user-attachments/assets/64424b7f-146b-4dc9-a449-255dc4ad73fa)

- We now can use ffuf to enumerate directories. I use the list right here [directory-list-2.3-small.txt](https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/directory-list-2.3-small.txt)

```bash
ffuf -w directory-list-2.3-small.txt:FUZZ -u http://hammer.thm:1337/hmr_FUZZ -fc 200
```

![image](https://github.com/user-attachments/assets/b834d6be-e1ac-42a5-bef8-f230e4f595b5)

- We find an unusual directory: `logs`. Accessing this directory, we retrieve an email `tester.hammer.thm`
