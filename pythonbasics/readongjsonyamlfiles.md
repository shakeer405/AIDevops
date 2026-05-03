In Python, JSON (JavaScript Object Notation) and YAML (YAML Ain't Markup Language) files are both text-based formats used to serialize data structures that can easily be read by humans and parsed into native objects. They serve a similar purpose but have different syntaxes and features; the former being more common in web applications, while the latter is often preferred for configuration due to its human-readable format with less strict requirements on quotation marks around keys:

Python json Module - JSON File Handling
To work with JSON files, you need to import json. Here’s a step-by-step guide using real examples. Let's start by writing data into a file called 'example.json':

import json
filepath = "C:/example/to/your/files/directory/example.json"  
data_to_write = {"name": "John", "age": 30, "city": "New York"}  
with open(filepath, "w") as file: # opening the json file in write mode with 'w' flag and a context manager (the `with` statement)   
     json.dump(data_to_write, file) # Writing data to JSON using built-in function dump() from json module 
# Writing updates back into json with proper indentation for better human readability    
with open(filepath, "r") as fp_read: # opening a file for reading 'r' flag     
    data = json.load(fp_read)  
print("Data loaded from JSON:\n",data) 
# Adding new key-value pair to the dictionary and writing back into json    
data["country"] = "USA" 
with open(filepath, "w") as fp_write: # opening a file in write mode 'w' flag  
    json.dump(data,fp_write)     


Working with JSON Files in Python
Importing the required modules: First, you need to import the json module in Python. This module provides methods to work with JSON data.

import json

Reading JSON data: To read JSON data from a file, you can use the json.load() method. This method takes a file object as an argument and returns a Python object.
with open('data.json') as f:
    data = json.load(f)
    print(data)

Writing JSON data: To write JSON data to a file, you can use the json.dump() method. This method takes a Python object and a file object as arguments.
with open('data.json', 'w') as f:
    json.dump(data, f)

4. Parsing Json data: If you have a JSON string, you can parse it using the json.loads() method. This method takes a JSON string as an argument and returns a Python object.
json_string = '{"name": "John", "age": 30, "city": "New York"}'
data = json
data = json.loads(json_string)
print(data)

5.Modifying JSON data: You can modify JSON data by accessing the attributes of the Python object and then writing it back to a file.

data['age'] = 31
with open('data.json', 'w')
    json.dump(data, f)

**Working with YAML Files in Python:**
1.Importing the required modules: First, you need to install the pyyaml library if you haven't already. You can install it using pip:

pip install pyyaml

import yaml

2. Reading YAML data: To read YAML data from a file, you can use the yaml.load() 
this method takes a file object as an argument and returns a Python object.
with open('data.yaml') as f:
    data = yaml.load(f)
    print(data)

3.writing yaml data
to write yaml data to a file , you can use the yaml.dump() method, which takes a Python object and a file object as arguments.

with open('data.yaml', 'w') as f:
    yaml.dump(data, f)

4. Parsing YAML data: If you have a YAML string, you can parse it using the yaml.load() method. This method takes a YAML string as an argument and returns a Python object.
yaml_string = 'name: John\nage: 30\ncity: New York'
data = yaml.load(yaml_string)
print(data)

5.modifying yaml data:
you can modify yaml data by accessing the attributes of the Python object and then writing it back to a file.

data['age'] = 31    
with open('data.yaml', 'w') as f:
    yaml.dump(data, f)

Operation	JSON	YAML
Read data from file	json.load()	yaml.safe_load()
Write data to file	json.dump()	yaml.dump()
Parse data from string	json.loads()	yaml.safe_load()
Modify data	Access attributes of Python object	Access attributes of Python object
Serialize data to string	json.dumps()	yaml.dump()
Deserialize data from string	json.loads()	yaml.safe_load()

File handling:
1.Opening a File:
To work with a file, you need to open it using the built-in open() function.this 
function takes the file path as an argument and returns a file object.
file_path = 'example.txt'
file = open(file_path, 'r')

with open(file_path, 'r') as file:

the with statement is used to ensure that the file is properly closed after use.this is important to prevent resource leak

2. Reading from a File:
To read the contents of a file, you can use the read() method of the file object. this method reads the entire contents of the file and returns it as a string.
file_path = "example.txt"
with open(file_path, 'r') as file:
    content = file.read()
    print(content)

alternative way:
file_path = "example.txt"
mode= 'r'
with open(file_path, mode) as file:
    for line in file:
        print(line)

3.writing to a file:
To write to a file, you can use the write() method of the file object. this method writes a string to the file.
file_path = "example.txt"
with open(file_path, 'w') as file:
    file.write("Hello, World!")

if you want to write to an existing file, you can use the a mode

file_path = "example.txt"
with open(file_path, 'a') as file:
    file.write("Hello, World!")

4.modifying a file:
to modify the contents of a file you can read the file, make the necessary changes
and write the modified content back to the file.

file_path = "example.txt"
mode= 'rw'

with open(file_path, mode) as file:
    content = file.read()
    modified_content = content.replace("Hello", "Hi")
    file.seek(0)
    file.write(modified_content)
    file.truncate()

In this example, the file is opened in 'r+' mode, which allows both reading and writing. The contents of the file are read, modified, and then written back to the file.

5.Handling Exception:
When working with files, it's important to handle exceptions that may occur, such as file not found errors or permission errors. You can use try-except blocks to catch and handle these exceptions. Here's an example:

file_path = "example.txt"
try:
    with open(file_path, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")     
    