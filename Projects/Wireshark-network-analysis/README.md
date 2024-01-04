# Wireshark Network Analysis	
----

![](https://www.freecodecamp.org/news/content/images/2020/08/wireshark-1.png)

## Overview
In this project, I will be using Wireshark to investigate pcapng files, analyzing network traffics and exfiltrate sensitive data.

## CTF1.pcapng
1. How many total Packets in the pcap file
From the menu, click `Statistics > Capture File Properties`. This will display the total packets in the pcapng file

![totalPackets](https://raw.githubusercontent.com/hhphu/images/main/Wireshark%20Project/totalPackets.png)

**Answer**: 50

2. How many ARP packets?
From the menu, click `Statistics > Protocols Hierarchy`. This will display the total ARP packets in the pcapng file.

![totalARP](https://github.com/hhphu/images/blob/main/Wireshark%20Project/arpPackets.png?raw=true)

**Answer**: 19

3. What domain did the user first try to access?
Investigating the first HTTP request (packet 23), we ses the requested URL is `http://thesimpsons.com`.

![accessingDomain](https://raw.githubusercontent.com/hhphu/images/main/Wireshark%20Project/accessingDomain.png)

**Answer**: thesimpsons.com

4. What HTTP response code did the user get?
Investigating the response packet (packet 24), we see the status code is 301, which means redirection.

![returnStatusCode](https://raw.githubusercontent.com/hhphu/images/main/Wireshark%20Project/returnStatusCode.png)

**Answer**: 301

5. What primary domain was the website directed to?
Investigating the `Hypertext Transfer Protocol` section of packet 24, we can see the domain to which the request was redirected.

![redirectedDomain](https://raw.githubusercontent.com/hhphu/images/main/Wireshark%20Project/redirectedDomain.png)

**Answer**: fox.com

6. What is the status code of packet number 36?
**Answer**: 200

7. What is the source port of original HTTP request?
From the `Transmission COntrol Protocol` section of the packet 23, we see the Source Port is 50568.
**Answer**: 50568

8. What is the primary NS server of the website being requested?
Filter the packets by DNS protocol, we immediately see the primary ns server of the domain

![primaryNSServer](https://raw.githubusercontent.com/hhphu/images/main/Wireshark%20Project/primaryNSServer.png)

**Answer**: ns01.foxinc.com

9. What is the TTL of the A record of the original website requested?
From packet 22, under the **Domain Name System (response) > Answers**, expand the domain name and we get the ttl of the A record

![ttl](https://raw.githubusercontent.com/hhphu/images/main/Wireshark%20Project/ttl.png)

**Answer**: 600 

10. In the one SYN/ACK packet, what is the time between this and the previous SYN packet in seconds? (Use exact value provided in the packet)
From the packet 26, view `Transmission Control Protoocl > [Timestamps]`. From here we see the time between the SYN/ACK packet and the first SYN packet

![timebtwSYNACK](https://raw.githubusercontent.com/hhphu/images/main/Wireshark%20Project/timebtwSYNACK.png)

**Answer**: 0.026018

11. What is Homer Simpson’s phone number? (with dashes)
In the filter, run `frame contains "homer"`. There should be only 1 packet. Analyzing the packet should yield Homer's phone number

![filterContainsHomer](https://raw.githubusercontent.com/hhphu/images/main/Wireshark%20Project/filterContainsHomer.png)

**Answer**: 856-238-2349

12. Where does Homer want Marge to meet him?
Analyzing the same frame will give us the answer.

**Answer**: Moes

13. What is the vendor name of Homer’s NIC? (five letters)
With the same frame, the venoder name of Homer's NIC is displayed in the `Ethernet II` section

**Answer**: Intel

 
