
# Stegnography

- Embed message into an image
```bash
steghide embed -cf <IMAGE_FILE> -ef <FILE.txt>

  embed: specify that we want to hide the message
  -cf <IMAGE_FILE> (cover file): specify the file in which data is hidden.
  -ef <FILE.txt> (embed file): specify the file that is being hidden.
```

- Extract secret message
```bash
steghide extract -sf <IMAGE_FILE>

  extract: indicate we want to extract the message.
  -sf <IMAGE_FILE> (stegofile): specify the file to run the steganography 
```
