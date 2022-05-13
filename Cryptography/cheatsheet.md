# GPG
- **Create the Key Pair**
  ```bash
  gpg --gen-key
  ```
- **Validate created keys**
  ```bash
  gpg --list-keys
  ```

- **Exporting and Importing Keys**
  
  Users need to **export** their public keys to make them public, so others can use it.
  ```bash
  gpg --armor --output NAME.gpg --export NAME@email.com

      gpg: The command to run GPG.
      --armor: Puts the key in an ASCII format.
      --output NAME.gpg: Creates the public key in an accessible format. In this case, we named the key `NAME.gpg`.
      --export NAME@email.com: References which key to use from the key ring. It is referenced by the email.
  ```

- To **import** this key 
    ```bash
    gpg --import NAME.gpg
    ```

- **Encryption**
  ```bash
  gpg --armor --output encryptedmessage.txt --encrypt --recipient NAME@email.com plainmessage.txt

    gpg: The command to run GPG.
    --armor: Puts the encrypted message in an ASCII format.
    --output encryptedmessage.txt: Command for the output file, which creates the name of the encrypted file.
    --encrypt: Tells GPG to encrypt.
    --recipient NAME@email.com: Tells GPG which public key to use, based on the email address of the key.
    plainmessage.txt: Specifies for GPG which plaintext file to encrypt.
  ```


- **Step 4: Decryption**
```basg
  gpg --output decrypted_message --decrypt encryptedmessage.txt

    gpg: The command to run gpg.
    --output decrypted_message`: This creates an output file, which is the decrypted message.
    --decrypt encryptedmessage.txt`: This is indicating to decrypt and what file to decrypt.
```

--------------------------------------
# OpenSSL

- **Creating the Key and Initialization Vector**

  - The key, which is the private key, will be used for encryption and decryption.
  - The initialization vector is an additional value that adds randomness to the key.
  
```bash
openssl enc -pbkdf2 -nosalt -aes-256-cbc -k mypassword -P > key_and_IV

  - `openssl` initializes the OpenSSL program.
  - `enc` stands for _encryption_.
  - `-pbkdf2` specifies the encryption key type. 
  - `-nosalt` specifies that salting will not be applied.
      - (Salting, which will be covered in more depth later, adds a random value.)
  - `-aes-256-cbc` is the name of the cipher used. 
  - `-k PASSWORD` creates a key, with the password `mypassword`.
  - `-P > key_and_IV` prints out the key and IV to a file called `key_and_IV`.
````
- Open up the file key_and_IV, and note the key and IV in the file.

```
  key=89E01536AC207279409D4DE1E5253E01F4A1769E696DB0D6062CA9B8F56767C8
  iv =EE99333010B23C01E6364E035E97275C
```
- **Encrypting with OpenSSL**
  ```bash
  openssl enc -pbkdf2 -nosalt -aes-256-cbc -in plainmessage.txt -out plainmessage.txt.enc -base64 -K 89E01536AC207279409D4DE1E5253E01F4A1769E696DB0D6062CA9B8F56767C8 -iv EE99333010B23C01E6364E035E97275C

    - `openssl` initializes the OpenSSL program.
    - `enc` stands for _encryption_.
    - `-pbkdf2` specifies the encryption key type. 
    - `-nosalt` specifies that salting will not be applied.
    - `-aes-256-cbc` the type of cipher used.
    - `-in plainmessage.txt` is the input file that we will be encrypting.
    - `-out plainmessage.txt.enc` is the output file that is encrypted.
    - `-base64` specifies completing the encryption in a text format.
    - `-K 89E01536AC207279409D4DE1E5253E01F4A1769E696DB0D6062CA9B8F56767C8` specifies the key and the key value.
    - `-iv EE99333010B23C01E6364E035E97275C` specifies the IV and the IV value.
  ```

- Open `plainmessage.txt.enc` file. The text looks encrypted as it is not readable:
```bash
   zi9BCV1uAdGrOnzL26fGpspt91VY44MNrbtOLL/tih4=
```
   
- **Decrypting with OpenSSL**
```bash
   openssl enc -pbkdf2 -nosalt -aes-256-cbc -in plainmessage.txt.enc -d -base64 -K 89E01536AC207279409D4DE1E5253E01F4A1769E696DB0D6062CA9B8F56767C8 -iv EE99333010B23C01E6364E035E97275C

   - The syntax is the same as the encryption, except for two small changes:
    - `-d` specifies decryption.
    - `-in plainmessage.txt.enc` specifies that the input message is now the encrypted message.
``` 
---------------------------------
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
-----------------------------
# SSL Certificates
