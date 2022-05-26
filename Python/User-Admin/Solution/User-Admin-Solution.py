# Administrator accounts list
from cmath import log
from xmlrpc.client import boolean

adminList = [
    {
        "username": "DaBigBoss",
        "password": "DaBest"
    },
    {
        "username": "root",
        "password": "toor"
    }
]

# Build your login functions below
userInfo = {}
loggedIn = False


def getCreds():
    usernameInput = input("Enter username: ")
    passowrdInput = input("Enter password: ")
    userInfo.update({"username": usernameInput, "password": passowrdInput})


def checkLogin(userInfo, adminList):
    username = userInfo["username"]
    password = userInfo["password"]

    for credential in adminList:
        if ((credential["username"] == username) and
                (credential["password"] == password)):
            return True
    userInfo.clear()

    return False


while True:
    getCreds()
    loggedIn = checkLogin(userInfo, adminList)

    if (loggedIn):
        print("Successfully logged in.")
        break
    else:
        print("Invalid username or password. Try again")
        print("----------------------------------------")
