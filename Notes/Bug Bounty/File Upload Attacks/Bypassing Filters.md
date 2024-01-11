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

