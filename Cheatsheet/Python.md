# Variable Assignment
------------------
* Integers
```python
int_variable = 10
```

* Floats
```python
float_variable = 1.25
```

* Booleans
```python
boolean_variable = True
```

* Strings
```python
string_variable = "Hello World!"
```

-------------------------
# Referencing and Printing
* Print variable values
```python
print(int_variable)
print(float_variable)
print(boolean_variable)
print(string_variable)
```

* Print variable types
```python
print(type(int_variable))
print(type(float_variable))
print(type(boolean_variable))
print(type(string_variable))
```
--------------------------
* Arithmetic Operation
```python
count = 10 + 2
print(count)
```
---------------------------------
* String Concatenation
```python
hello = "Hello " + "World!"
print(hello)
```

* String Conversion and Concatenation
```python
age = 27
words = "I am currently "
completeSentence = words + str(age)
print(completeSentence)
```

----------------------------------
# User Input
* input() function requests user input from the command line. 
* The user's response is stored as the variable value.
```python
name = input("What is your name? ")
print("Hello " + name)
```

* User inputs are received as strings.
* They must be converted into integers or floats if we intend to do arithmetic.
```python
number = input("Please enter a number to multiply by 2: ")
print(int(number) * 2)
```

----------------------------------
# Working with Files

#### Reading Text Files
* Method 1
```python
# The open() function creates a connection to an external file
# The parameter passed into the function is the relative or absolute path to file to open
sample_txt_file = open("Sample.txt","r")

# Using the .read() function then stringifies the file's contents
sampleText = sample_txt_file.read()
print(sampleText)

# Closing the connection to the external file in order to save memory
sample_txt_file.close()
```
* Method 2: By using context manager, "with" keyword, users are able to work with files from within the blocks. Once users exit the block, the files are automatically closed.
 
```python
	with open('Sample.txt','r') as sample_txt_file:
		# do something with the file
	
```

#### Writing Text Files
```python
# The open() function is also used for writing, though it defaults to "r"ead
# so we have to use the "w" mode as the second argument ("w"rite, instead of "r"ead)
diary_file = open("MyPersonalDiary.txt", "w")


# The .write() function is then used to push the text into the external file
diary_file.write("I don't write in diaries.")

# Since no spacing or newlines are added between .write() functions, they have to be programmed into the application manually
diary_file.write("\nPeriod.")
```

#### Appending Text
```python
# The "a" mode stands for append and allows the application to add new text onto the end of an existing file
notesFile = open("Notes.txt", "a")

# The .write() method in conjunction with the append mode will write to the end of a file
notesFile.write("\nThis is a completely new line of text created by the APPEND mode.")

# Closing the file
notesFile.close()
```

#### Strings Method
```python
# Since the file is now a string, it can be modified and worked with using some string functions
# The split() function breaks a string apart into a list based upon common words/characters that appear in the original string
sampleSplit = sampleText.split(" ")

# Since the string was split on spaces, individual words will now be printed when referenced
print(sampleSplit[0])
print(sampleSplit[1])
print(sampleSplit[2])
print(sampleSplit[3]) 
print("-----------")

# The find() function will navigate through some text, determine whether or not the string passed into it is contained within, and return the index of that string
print(sampleText.find("malarkey"))

# This can be exceptionally useful when checking to see if a file contains some specific keywords
if sampleText.find("malarkey") > -1:
    print("Malarkey found!")

if sampleText.find("juice") > -1:
    print("Juice found")
```

----------------------------------
# Reading CSV Files

#################################################
### Method 1 (Old): Plain Reading (no module) ###
#################################################
```python
# Connect to the file and read in the text it contains
wrestling_csv = open("WWE-Data-2016.csv", "r")
wrestling_text = wrestling_csv.read()

# Since a CSV is broken into rows and columns, it will need to be split twice
# The first split is to break the original text into rows by splitting on each new line
wrestling_rows = wrestling_text.split("\n")
print(wrestling_rows[0])
print(wrestling_rows[1])
print(wrestling_rows[2])
print(wrestling_rows[3])
print("-----------")


# The next split will then split the row into its respective columns on commas
wrestling_cells = wrestling_rows[0].split(",")
print(wrestling_cells[0])
print(wrestling_cells[1])
print(wrestling_cells[2])
print(wrestling_cells[3])
```

###################################################
### Method 2: Improved Reading using CSV module ###
###################################################
```python
import csv

csvFile = open("WWE-Data.csv")

# The `csv.reader()` method is used to read in the data within the file
contents = csv.reader(csvFile)
# Contents returned as a CSV object
print(contents)

# The CSV object can be looped through without any splitting
for row in contents:
    print(row)

    # rows are already created as lists of cells for us, so no need to split
    print(row[0])
```

----------------------------------
# OS Module
```python
# import the os library to use later
import os

# The os.path.join() function creates a file path which will work for the current file system (so this code will work for any filesystem)
real_path = os.path.join("Resources", "CoolText.txt")

# This path can then be used for open()
cool_text = open(real_path)
print(cool_text.read())
print("--------------")


# The os.path.isfile() function returns True if the file path provided points to an actual file, false otherwise
fake_path = os.path.join("Resources", "NotAFile.txt")
print(os.path.isfile(real_path))
print(os.path.isfile(fake_path))
print("--------------")


# you can use isfile before you do a read to avoid errors if you're not sure the file will be there:
fileName = input("Please enter the file you're looking for: ")

filePath = os.path.join("Resources", fileName)

if os.path.isfile(filePath):
    print("Found it!")
    # read the file here
else:
    print("That file doesn't exist")
```

##############
### OSWalk ###
##############
```python
# import the os library to use later
import os

folder_path = os.path.join("Resources", "DiaryEntries")

# The os.walk() function is used to navigate through a collection of folders/files
# This function returns three values for each step it takes: root, dirs, and files
for root, dirs, files in os.walk(folder_path):

    # The root is the folder that is currently being searched through
    print("Currently inside of... " + root)

    # The dirs list stores all of the names of the folders inside the current root
    print("The folders in here are..." + str(dirs))

    # The files list stores all of the names of the files inside the current root
    print("The files in here are..." + str(files))
    print("~~~~~~~~~~")

print("--------------")

# In order to construct the file path to use dynamically...
for root, dirs, files in os.walk("Resources"):

    # Loop through all of the files in the current root
    for file_name in files:

        # Create a path by combining (joining) the root and the file name
        current_file_path = os.path.join(root, file_name)
        print(current_file_path)

        # We can then check that the file exists through using os.path.isfile()
        print("EXISTS: " + str(os.path.isfile(current_file_path)))

```

----------------------------------
----------------------------------
# List
* Create a list and save it to a variable
```python
hobbies = ["Rock Climbing", "Bug Collecting", "Cooking", "Knitting", "Writing"]
print(hobbies)
```

* Select the first and second values from the list
```python
print(hobbies[0])
print(hobbies[1])
```
* len() tells us how long the list is (5)
```python
print(len(hobbies))
```

* Use index() to find the index of a specific value in a list
```python
print(hobbies.index("Cooking"))
```

* Use append() to add values to the end of the list
```python
hobbies.append("Gaming")
print(hobbies)
```

* Use remove() to remove values from the list
```python
hobbies.remove("Bug Collecting")
print(hobbies)
```

------------------------------
# Dictionary
* Unlike lists, dictionaries store information in pairs
    * A list of actor's names
     ```python
     actors = ["Tom Cruise",
          "Angelina Jolie",
          "Kristen Stewart",
          "Denzel Washington"]
     ```

    * A dictionary of an actor
    ```python
    actor = {"name": "Tom Cruise"}
    print(actor["name"])
    ```

* A dictionary can contain multiple pairs of information
```python
actress = {
  "name": "Angelina Jolie",
  "genre": "Action",
  "nationality": "United States"
  }
```

* A dictionary can contain multiple types of information
```python
another_actor = {
    "name": "Sylvester Stallone",
    "age": 62,
    "married": True,
    "best movies": [
      "Rocky",
      "Rocky 2",
      "Rocky 3"
      ]
    }

print(another_actor["name"] + " was in " + another_actor["best movies"][0])
```

* A dictionary can even contain another dictionary
```python
film = {"title": "Interstellar",
        "revenues": {
          "United States": 360, 
          "China": 250, 
          "United Kingdom": 73
          }
        }

print(film["title"] + " made " + film["revenues"]["United States"] + " in the US.")
```




