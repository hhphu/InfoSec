# Cracking leaked passwords database

## Tasks
As a governance analyst it is part of your duties to assess the level of protection offered by implemented controls and minimize the probability of a successful breach. To be successful at your job you often need to know the techniques used by hackers to circumvent implemented controls and propose uplifts to increase the overall level of security in an organization. Gaining valid credentials gives the attackers access to the organization’s IT system, thus circumventing most of perimeter controls in place.

Your job is to crack as many passwords as possible with available tools (e.g. use Hashcat). Here are your Task instructions:

1. Review the links provided in the additional resources below to gain a background understanding of password cracking
2. Try to crack the passwords provided in the 'password dump' file below using available tools
3. Assess the 5 questions in the task instructions below in relation to the passwords provided (type of hashing algorithm, level of protection, possible controls that could be implemented, password policy, changes in policy)
4. Draft an email/memo briefly explaining your findings in relation to controls used by the organization and your proposed uplifts. 
 
You must determine the following:

- What type of hashing algorithm was used to protect passwords?
- What level of protection does the mechanism offer for passwords?
- What controls could be implemented to make cracking much harder for the hacker in the event of a password database leaking again?
- What can you tell about the organization’s password policy (e.g. password length, key space, etc.)?
- What would you change in the password policy to make breaking the passwords harder? 

## Resources
<details>
	<summary> Password Dump </summary>

 	
		experthead:e10adc3949ba59abbe56e057f20f883e
		interestec:25f9e794323b453885f5181f1b624d0b
		ortspoon:d8578edf8458ce06fbc5bb76a58c5ca4
		reallychel:5f4dcc3b5aa765d61d8327deb882cf99
		simmson56:96e79218965eb72c92a549dd5a330112
		bookma:25d55ad283aa400af464c76d713c07ad
		popularkiya7:e99a18c428cb38d5f260853678922e03
		eatingcake1994:fcea920f7412b5da7be0cf42b8c93759
		heroanhart:7c6a180b36896a0a8c02787eeafb0e4c
		edi_tesla89:6c569aabbf7775ef8fc570e228c16b98
		liveltekah:3f230640b78d7e71ac5514e57935eb69
		blikimore:917eb5e9d6d6bca820922a0c6f7cc28b
		johnwick007:f6a0cb102c62879d397b12b62c092c06
		flamesbria2001:9b3b269ad0a208090309f091b3aba9db
		oranolio:16ced47d3fc931483e24933665cded6d
		spuffyffet:1f5c5683982d7c3814d4d9e6d749b21e
		moodie:8d763385e0476ae208f21bc63956f748
		nabox:defebde7b6ab6f24d5824682a16c3ae4
		bandalls:bdda5f03128bcbdfa78d8934529048cf
  
	
</details>


- [Cracking passwords explained](https://arstechnica.com/information-technology/2013/05/how-crackers-make-minced-meat-out-of-your-passwords/)
- [Password Salting](https://arstechnica.com/information-technology/2013/05/how-crackers-make-minced-meat-out-of-your-passwords/)
- [Hash Functions](https://en.wikipedia.org/wiki/Cryptographic_hash_function)
- [Passwords Cracing Tools](https://en.wikipedia.org/wiki/Password_cracking#Software)
- [Password Strenth Checker](https://howsecureismypassword.net/)

## Cracking the passwords
- For this project, I will be using **John the Ripper** to bruteforce the hashes in the file (`passwd_dump.txt`).

```bash
	john --format=Raw-MD5  passwd_dump.txt
```

- This is how it should look like.

![image](https://github.com/hhphu/InfoSec/assets/45286750/b162dc28-ab2a-42b6-8984-7b981b3eff40)

# [View Reports](goldman-sachs-security-report.pdf)
