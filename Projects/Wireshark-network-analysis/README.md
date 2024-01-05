# Wireshark Network Analysis	
----

![](https://www.freecodecamp.org/news/content/images/2020/08/wireshark-1.png)

## Overview
In this project, I will be using Wireshark to investigate pcapng files, analyzing network traffics and exfiltrate sensitive data.

## CTF1.pcapng
**1. How many total Packets in the pcap file**
   
From the menu, click `Statistics > Capture File Properties`. This will display the total packets in the pcapng file

![totalPackets](https://raw.githubusercontent.com/hhphu/images/main/Wireshark%20Project/totalPackets.png)

Answer: 50

**2. How many ARP packets?**
   
From the menu, click `Statistics > Protocols Hierarchy`. This will display the total ARP packets in the pcapng file.

![totalARP](https://raw.githubusercontent.com/hhphu/images/main/Wireshark%20Project/arpPackets.png)

Answer: 19

**3. What domain did the user first try to access?**
   
Investigating the first HTTP request (packet 23), we ses the requested URL is `http://thesimpsons.com`.

![accessingDomain](https://raw.githubusercontent.com/hhphu/images/main/Wireshark%20Project/accessingDomain.png)

Answer: thesimpsons.com

**4. What HTTP response code did the user get?**
   
Investigating the response packet (packet 24), we see the status code is 301, which means redirection.

![returnStatusCode](https://raw.githubusercontent.com/hhphu/images/main/Wireshark%20Project/returnStatusCode.png)

Answer: 301

**5. What primary domain was the website directed to?**
   
Investigating the `Hypertext Transfer Protocol` section of packet 24, we can see the domain to which the request was redirected.

![redirectedDomain](https://raw.githubusercontent.com/hhphu/images/main/Wireshark%20Project/redirectedDomain.png)

Answer: fox.com

**6. What is the status code of packet number 36?**
   
Answer: 200

**7. What is the source port of original HTTP request?**
   
From the `Transmission COntrol Protocol` section of the packet 23, we see the Source Port is 50568.

Answer: 50568

**8. What is the primary NS server of the website being requested?**
    
Filter the packets by DNS protocol, we immediately see the primary ns server of the domain

![primaryNSServer](https://raw.githubusercontent.com/hhphu/images/main/Wireshark%20Project/primaryNSServer.png)

Answer: ns01.foxinc.com

**9. What is the TTL of the A record of the original website requested?**
    
From packet 22, under the **Domain Name System (response) > Answers**, expand the domain name and we get the ttl of the A record

![ttl](https://raw.githubusercontent.com/hhphu/images/main/Wireshark%20Project/ttl.png)

Answer: 600 

**10. In the one SYN/ACK packet, what is the time between this and the previous SYN packet in seconds? (Use exact value provided in the packet)**
    
From the packet 26, view `Transmission Control Protoocl > [Timestamps]`. From here we see the time between the SYN/ACK packet and the first SYN packet

![timebtwSYNACK](https://raw.githubusercontent.com/hhphu/images/main/Wireshark%20Project/timebtwSYNACK.png)

Answer: 0.026018

**11. What is Homer Simpson’s phone number? (with dashes)**
    
In the filter, run `frame contains "homer"`. There should be only 1 packet. Analyzing the packet should yield Homer's phone number

![filterContainsHomer](https://raw.githubusercontent.com/hhphu/images/main/Wireshark%20Project/filterContainsHomer.png)

Answer: 856-238-2349

**12. Where does Homer want Marge to meet him?**
    
Analyzing the same frame will give us the answer.

Answer: Moes

**13. What is the vendor name of Homer’s NIC? (five letters)**
    
With the same frame, the venoder name of Homer's NIC is displayed in the `Ethernet II` section

Answer: Intel

## CTF2.pcapng
**1. Decrypt the wireless PCAP with the WPA key. How many HTTP packets?**

To decrypt the PCAP file:
	- First go to **Edit > Preferences**.
	- From the menu on the left, expand the **Protocols** option, then select **IEEE 802.11**. 
	- Once the option is selected, make sure the box "Enable decryption" is checked.
	- Click `Edit` button next to the "Decryption keys" text. Then in a new window, add the key-value pair: `wpa-pwd:Induction`

![decryptWPA](https://raw.githubusercontent.com/hhphu/images/main/Wireshark%20Project/decryptWPA.png)

Once we decrypt the PCAP file, we can check the total number of HTTP packets by filtering, which is displayed at the bottom right of Wireshark

Answer: 18

**2. IP address of Karens-imac.local.**

In packet 439, the packet details have both the values:  `Internet Protocol Version 4, Src: Karens-iMac.local (192.168.0.50), Dst: rr.pmtpa.wikimedia.org (66.230.200.100).`

![src-dstIP](https://raw.githubusercontent.com/hhphu/images/main/Wireshark%20Project/src-dstIP.png)

Answer: 192.168.0.50

**3.IP address of rr.pmtpa.wikimedia.org.**

Answer: 66.230.200.100

**4. What is the SSID of the wireless router?**

From the top menu, select **Wireless > WLAN Traffic**. The SSID will be displayed.

![ssid](https://raw.githubusercontent.com/hhphu/images/main/Wireshark%20Project/ssid.png)

Answer: coherer

**5. DNS provides this TTL for the CNAME of  en.wikimedia.org.**

Filter the file by DNS. Look at a frame with the CNAME (429). Select **Domain Name System > Answer > en.wikipedia.org**, we'll see the CNAME's TTL

![cnameTTL](https://raw.githubusercontent.com/hhphu/images/main/Wireshark%20Project/cnameTTL.png)

Answer: 811

**6. Total count of SUCCESSFUL ICMP, “DESTINATION REACHABLE” packets.**

Filter by ICMP, we see all the packets result in "Destination Unreachable". Hence the answer is 0

![icmpReachable](https://raw.githubusercontent.com/hhphu/images/main/Wireshark%20Project/icmpReachable.png)

Answer: 0

**7. Television show the user was viewing the transcripts for (three letters).**

Inspecting several HTTP packets (778 and others), we see they have Host name is snltranscripts.jt.org. Hence, we can deduce that the show is Saturday Night Live.

![snl](https://raw.githubusercontent.com/hhphu/images/main/Wireshark%20Project/snl.png)

Answer: snl

## CTF3.pcapng
**1. What is the primary protocol in these packets?**

Once openning the PCAP file, we see the primary protocol is ARP

![primaryProtocol](https://raw.githubusercontent.com/hhphu/images/main/Wireshark%20Project/primaryProtocol.png)

Answer: ARP

**2. What is likely the true MAC address of 192.168.1.254?**

From packet #2, we see both the original and the duplicated IP for 2 different MAC addresses. The one in Frame 1 is likely to be the true MAC address.

![originalMAC](https://raw.githubusercontent.com/hhphu/images/main/Wireshark%20Project/originalMAC.png)

Answer: 00:22:90:35:64:8a

**3. Which is likely the hacker's MAC address of 192.168.1.254?**

From the same screenshot above, we see the hacker's MAC address.

Answer: 00:50:56:8e:ee:89

**4. What year did this traffic occur in?**

Inspect details of any frame, we see the time of the incident

![timeOccur](https://raw.githubusercontent.com/hhphu/images/main/Wireshark%20Project/timeOccur.png)

Answer: 2015



 
