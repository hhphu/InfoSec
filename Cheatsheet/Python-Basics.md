# My First Python Program!
```python
print("Hello World!")
```

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




