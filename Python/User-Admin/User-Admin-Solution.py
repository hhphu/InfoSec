# Administrator accounts list
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
userInfo = []


def getCreds():
    username = input("Enter username ")
    passowrd = input("Enter password")
    return userInfo.append({"username": username,
                            "password": passowrd})


def checkLogin(userInfo, adminList):
    loggedIn = False
