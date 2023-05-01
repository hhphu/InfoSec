- The whole enumeration process is split into three levels: 
	- Infrastructure-based enumeration
	- Host-based enumeration
	- OS-based enueration

![](https://academy.hackthebox.com/storage/modules/112/enum-method3.png)

- Everything is built under layers:
	- Internet Presence: public facing surface, externally accessible infrastructure (domain, subdomains, ASN, IP addresses, etc.)
	- Gateway: Security measures used to protect the company external and internal infrastructures (firewalls, IDS/IPS, DMZ, VPN, Cloudfare)
	- Accessible Services: interfaces that can be accessed internnally or externally (Service Type, Port, Versoin, Interfaces)
	- Proccesses: internal procecesses, resources and desitnions with the services (PID, tasks, Proccessed Data, etc.)
	- Privileges: Internal permissions to accessible services (Groups, users, Permissions)
	- OS Setup: Internal components and system setup.

- Goals when performing a blackbox testing:
	- Internet Presence: identify all possible target systems and interfaces that can be tested
	- Gateway: understand what we are dealing with and what we have to watch out for
	- Accessible services: understand the reason and functionality of the target system and gain the necessary knowledge to communicate with it and exploit it for our purpses effectively
	- Processes: understand these factors and identify the dependencies between them
	- Privileges: identify privileges and undersntad what is/is not possible with these privileges
	- OS Setup: see how the administratotrs manage the systems and what sensitive internal information we can glean from them.
- 