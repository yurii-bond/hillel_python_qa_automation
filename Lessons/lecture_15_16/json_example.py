import json


data = {
    'name': 'John',
    'age': 30,
    'city': "New York"
}

json_string = json.dumps(data, indent=4)
print(json_string)


json_object = json.loads(json_string)

print(json_object)

name = json_object['name']
age = json_object['age']
print(name)
print(age)


