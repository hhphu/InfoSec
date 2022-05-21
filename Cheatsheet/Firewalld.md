# Firewalld

Firewalld is more complicated than ufw, but also more flexible. `firewalld` also allows you to organize firewall rules for different interfaces into different **zones**. This makes it easier to make isolated updates to specific interfaces.

Firewalld also doesn't require you to restart it between changes.

- Start the firewalld service
```bash
sudo /etc/init.d/firewalld start
```

- View all the firewall Zones
```bash
sudo firewall-cmd --list-all-zones
```

- Assign the interface eth1 to zone 'home'
```bash
sudo firewall-cmd --zone=home --change-interface=eth1
```

Firewalld also allows you to enable services per zone.

- List all available services to allow or deny
```bash
sudo firewall-cmd --get-services
```

- List all services applied to zone 'DMZ'
```bash
sudo firewall-cmd zone=DMZ --list-all
```

Setting rules with Firewalld require a bit more syntax than UFW

- Block traffic from address 10.10.10.10 in the office zone.
```bash
sudo firewall-cmd --zone=office --add-rich-rule="rule family='ipv4' source address='10.10.10.10' reject"
```
