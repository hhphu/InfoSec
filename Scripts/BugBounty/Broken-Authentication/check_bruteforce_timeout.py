import sys,getopt
import os
import requests


url = ""
arguments_list = sys.argv[1:]
options_short = "u:"
options_long = ["--url"]


try:
        # Parsing arguments
        arguments, values = getopt.getopt(arguments_list, options_short, options_long)

        for argument, value in arguments:
                if argument in ("-u", "--url"):
                        url = value 
except getopt.error as error:
        print(str(error))



isTimeout = False
failed_message = "Invalid credentials"

# data for POST requests
payload = {
        "userid":"admin",
        "passwd":"password",
        "submit":"submit"
}

count = 0

# Create a html file in which the response.text will be written
def export_to_html(content):
        with open('response.html', 'w') as f:
                f.write(content)

while (isTimeout == False):
        print("Checking timeout for target {}".format(url))
        count +=1
        response = requests.post(url, data=payload)
        if failed_message not in response.text:
                isTimeOut = True
                print("The application times out after {} attempts!".format(count))
                export_to_html(response.text)
                print("response.html file is generated in the same directory. Opening the file . . .")
                os.system("open response.html")
                break
