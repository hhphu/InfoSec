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

