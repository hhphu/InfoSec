## UserAdmin

When you buy a new home WiFi router, it typically comes with one admin login and password to access settings via the product's website. If you don't have this admin password, you're unable to change things like the WiFi network name and password. 

In this activity, you'll use Python to build a login system for a WiFi router that only allows those with admin credentials to log in.

### Instructions

1. Open up `Unsolved/UserAdmin.py`.

2. Create a function named `getCreds` with no parameters that will prompt the user for their username and password. This function should return a dictionary called `userInfo` that looks like the dictionaries below:

```python
# Administrator accounts list
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
```

3. Create a function named `checkLogin` with two parameters: the `userInfo` and the `adminList`. The function should check the credentials to see if they are contained within the admin list of logins. The function should set a variable `loggedIn` to `True` if the credentials are found in the admin list, and set the variable to `False` otherwise.

Now that we know how to check to see if a user is logging in with admin credentials, let's set up the part of the system that will continue to prompt the user for their username and password if they didn't enter correct admin credentials before. 

4. Create a `while` loop that will continue to call `getCreds` and `checkLogin` until a user logs in with admin credentials. 

5. After each call of `checkLogin` in the `while` loop, print to the terminal the string `"---------"`.

6. Once the user logs in with admin credentials, print to the terminal the string `"YOU HAVE LOGGED IN!"`.

3. Run the code often as you write and test individual functions with correct and incorrect admin credentials to make sure you're on the right path!

