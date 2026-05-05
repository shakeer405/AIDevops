import requests
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
print(response.status_code)
print(response.headers)
# print(response.json())
if response.status_code == 200:
    data = response.json()
    print(f'successfully fetched data: {response.status_code}')
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")


import requests

url = 'https://jsonplaceholder.typicode.com/posts'
data = {
    'name': 'John Doe1',
    'email': 'johndoe1@example.com'
}
response = requests.post(url, json=data)
print(response.status_code)

print(response.json())

if response.status_code == 201:
    print(response.json())
else:
    print(f'Error: {response.status_code}')    

Authentication:
import requests

url = 'https://api.example.com/users'
headers = {
    'Authorization': 'Bearer your_token'
}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    print(response.json())
else:
    print(f'Error: {response.status_code}')

import requests

url = 'https://api.example.com/users/123'
response = requests.get(url)

if response.status_code == 200:
    print(response.json())
elif response.status_code == 404:
    print('User not found')
else:
    print(f'Error: {response.status_code}')    