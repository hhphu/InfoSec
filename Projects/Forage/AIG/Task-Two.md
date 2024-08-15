# Task Two

## Setting the scene for your next task
Your advisory email in the last task was great. It provided context to the affected teams on what the vulnerability was, and how to remediate it. 

Unfortunately, an attacker was able to exploit the vulnerability on the affected server and began installing a ransomware virus. Luckily, the Incident Detection & Response team was able to prevent the ransomware virus from completely installing, so it only managed to encrypt one zip file. 

Internally, the Chief Information Security Officer does not want to pay the ransom, because there isn’t any guarantee that the decryption key will be provided or that the attackers won’t strike again in the future. 

Instead, we would like you to bruteforce the decryption key. Based on the attacker’s sloppiness, we don’t expect this to be a complicated encryption key, because they used copy-pasted payloads and immediately tried to use ransomware instead of moving around laterally on the network.

## Here is the background information for your task
In this task, you will write a Python script to bruteforce the decryption key of the encrypted file.

# [View script](bruteforce.py)
