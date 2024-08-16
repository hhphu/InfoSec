from zipfile import ZipFile

def main():
    print("[+] Beginning bruteforce ")

    # Open zipfile
    with ZipFile('enc.zip') as zf:

        # Open rockyou.txt
        with open('rockyou.txt', 'rb') as rockyou:

            # strip trailing lines
            passwords = rockyou.readlines()

            # Iterate through passwords in the list to find a valid one.
            for password in passwords:
                password = password.strip()
                try:
                    zf.extractall('extracted_files', pwd=bytes(password))
                    print("[+] Password found: {}".format(password))   
                    return True
                except RuntimeError:
                    print("[-] Incorrect password {}".format(password))
                    continue     

if __name__ == "__main__":
    main()
