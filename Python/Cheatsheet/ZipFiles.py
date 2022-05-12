# Import the zipfile module into the application
import zipfile

# Create a reference to the ZIP file you would like to extract
zipfileReference = zipfile.ZipFile("Text.zip")

# Run the `.extractall()` function on the variable containing the connection to the external ZIP file
zipfileReference.extractall()

# creating another reference, this time to a locked ZIP file
lockedZip = zipfile.ZipFile("Books.zip")

# Variable used to store the password string
password = "password"

# Running the `.extractall()` function with a password
lockedZip.extractall(pwd=password.encode('cp850','replace'))