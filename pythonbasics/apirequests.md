Installing the requests Library: Before you can make API requests, you need to install the requests library. You can do this using pip:
pip install requests

Making a Simple GET Request: To make a GET request to an API endpoint, you can use the get() method of the requests library. Here's an
import requests

url = 'https://api.example.com/users'
response = requests.get(url)

if response.status_code == 200:
    print(response.json())
else:
    print(f'Error: {response.status_code}')

In this example, the get() method is used to send a GET request to the specified URL. The response is stored in the response variable. If the response status code is 200 (indicating success), the JSON data is printed. Otherwise, an error message is printed.

Making a POST Request: To make a POST request to an API endpoint, you can use the post() method of the requests library. Here's an example:

import requests

url = 'https://api.example.com/users'
data = {
    'name': 'John Doe',
    'email': 'johndoe@example.com'
}
response = requests.post(url, json=data)

if response.status_code == 201:
    print(response.json())
else:
    print(f'Error: {response.status_code}')

In this example, the post() method is used to send a POST request to the specified URL. The request body is passed as a JSON object using the json parameter. If the response status code is 201 (indicating success), the JSON data is printed. Otherwise, an error message is printed.

4.Handling Response Data:
The response from an api request can be in various formats such as JSON, XML, HTML, etc
you can access the response data depending on format

json response:
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f'Error: {response.status_code}')

XML response:
response = requests.get(url)
if response.status_code == 200:
    data = response.text
    # Parse XML data using a library like lxml
    # Example:
    # from lxml import etree
    # root = etree.fromstring(data)
    # print(root)    

Plain text response:
    response = requests.get(url)
if response.status_code == 200:
    data = response.text
    print(data)

Handling Authentication: Some APIs require authentication to access their endpoints. You can pass authentication credentials using headers or parameters. Here's an example:

import requests

url = 'https://api.example.com/users'   

headers = {
    'Authorization': 'Bearer your_access_token'
}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    print(response.json())          
}
else:
    print(f'Error: {response.status_code}')

Handling Errors:
APIs may return fifferent types of errors, such as 404 not found, 401 un authorized or 500 internal server error

you can handle these errors using exception handling
import requests

url = 'https://api.example.com/users/123'
response = requests.get(url)

if response.status_code == 200:
    print(response.json())
elif response.status_code == 404:
    print('User not found')
else:
    print(f'Error: {response.status_code}')