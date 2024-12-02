# Advent of Cyber 2024: Day 1 Maybe SOC-mas music, he thought, doesn't come from a store?

![image](https://github.com/user-attachments/assets/fff032bc-51c4-4921-99c6-fc14c138a34c)

## Learning Objectives
- Learn how to investigate malicious link files.
- Learn about OPSEC and OPSEC mistakes.
- Understand how to track and attribute digital identities in cyber investigations.

## What is OPSEC?
Operational Security (OPSEC) protects sensitive data by identifying vulnerabilities. Cybersecurity OPSEC failures include reusing usernames, exposing metadata, or neglecting VPNs, which reveal personal info. Even skilled attackers make mistakes, leaving traces that expose them.

## WALKTHROUGH
Go to the spawned machine and paste the following [URL](https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley) to download the youtube video. We can select either `MP3` or `MP4`.

![image](https://github.com/user-attachments/assets/23086ed0-63b5-46f4-bc0a-28372ac0dbc0)

Extract the downloaded zip file and we see there will be two files `song.mp3` and `somg.mp3`

![image](https://github.com/user-attachments/assets/065c93e3-4754-4e16-8e8e-7573370f71f8)

Let's investigate these two files. Run the `file` command: `file song.mp3` and `file somg.mp3`

  ![image](https://github.com/user-attachments/assets/83fa8d3e-bacb-462a-84f9-ab17f56d8f94)

Looks like the `song.mp3` is a regular audio file while `somg.mp3` is more suspicious as it appears to be a shortcut file `.lnk`. 
Next we run `exiftool` command: `exiftool song.mp3` and `exiftool somg.mp3`

![image](https://github.com/user-attachments/assets/2c039854-fe14-4cb7-8b5a-a635b6ff20b2)

While the first file `song.mp3` shows regular information, there's a command running PowerShell embedded in the `somg.mp3` file. 
- The **-ep Bypass** **-nop** flags disable PowerShell's usual restrictions, allowing scripts to run without interference from security settings or user profiles.
- The **DownloadFile** method pulls a file (in this case, **IS.ps1**) from a remote server (`https://raw.githubusercontent.com/MM-WarevilleTHM/IS/refs/heads/main/IS.ps1`) and saves it in the **C:\\ProgramData\\** directory on the target machine.
- Once downloaded, the script is executed with PowerShell using the **iex** command, which triggers the downloaded `s.ps1` file.

Visiting this [URL](https://raw.githubusercontent.com/MM-WarevilleTHM/IS/refs/heads/main/IS.ps1) to see the full script. **Disclaimer, this is for educational purposes only. Please do not use it on any unauthorized machines.**

As the room explained, there can be many approaches once we get to the script embedded in the file. The one approach that we will be doing here in this room is to investigate the attacker's github profile to obtain more information about him/her.
We start by the signature with in th script: "Created by the one and only M.M."

![image](https://github.com/user-attachments/assets/8afbe5e7-a280-4257-bfb8-e5485f2e4399)

Performing some OSINT technique and Google Dorking, we can find more information about the attacker, such as the issues he/she created: https://github.com/Bloatware-WarevilleTHM/CryptoWallet-Search/issues/1

![image](https://github.com/user-attachments/assets/e976e582-ffc0-4919-9ed9-bab5c67de584)

From this, we learn that it is possible to trace back to the attacker's identity based on the scripts or the tools they use. 

## ANSWER THE QUESTION
**- Looks like the song.mp3 file is not what we expected! Run "exiftool song.mp3" in your terminal to find out the author of the song. Who is the author?**

`-> Tyler Ramsbey`

**- The malicious PowerShell script sends stolen info to a C2 server. What is the URL of this C2 server?**

![image](https://github.com/user-attachments/assets/780bdd5c-402b-4e1d-b805-0229ba707e9f)

`-> http://papash3ll.thm/data`

**- Who is M.M? Maybe his Github profile page would provide clues?**
From the attacker's github, visit the other repository and we learn who M.M. is

![image](https://github.com/user-attachments/assets/f78720fc-bbc2-40f9-9c38-3f85b038698e)

`-> Mayor Malware`

**- What is the number of commits on the GitHub repo where the issue was raised?**

`-> 1`

