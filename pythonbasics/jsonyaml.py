import json
filepath = "test.json"
data={"name": "John", "age": 30, "city": "New York"}
with open(filepath, 'w') as json_file:
    json.dump(data, json_file)

with open(filepath, 'r') as json_file:
    data = json.load(json_file)
print("Data read from json file", data)    

with open(filepath, 'r') as json_file:
    data = json.load(json_file)
print("Data read from json file", data)

data["coutry"]= "USA"
with open(filepath, 'w') as json_file:
    json.dump(data, json_file)
print("Data updated in json file", data)