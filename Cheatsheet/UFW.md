# UFW
UFW stands for 'Uncomplicated Firewall' and is the default firewall on most Linux systems.

```bash
### Check the status of ufw
sudo ufw status
```
Remember that you have to restart ufw before any changes take effect.
```bash
### Turn on the ufw firewall or reload it
sudo ufw enable
```

```bash
### Reset the ufw firewall to default configuration
sudo ufw reset
```
Many times administrators will start by denying ALL traffic to a host, and then only allowing the traffic that it needs.

```bash
### Deny all traffic
sudo ufw default deny incoming
sudo ufw default deny outgoing
```
You can also deny or allow traffic to specific ports.

```bash
### Allow traffic to port 80
sudo ufw allow 80
```
You may have to delete a rule from time to time

```bash
### Delete a ufw firewall rule
sudo ufw delete deny 80
```
