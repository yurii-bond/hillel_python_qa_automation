import json
import pandas as pd

json_string = '{"name": "John", "age": 30, "city": "New York"}'

data = {
    'name': 'John',
    'age': 30,
    'city': "New York"
}

json_data_string = json.dumps(data)

print(f'json_data_string: {json_data_string}')
print(type(json_data_string))
print(f'json_string:      {json_string}')
print(type(json_string))
new_data = json.loads(json_string)

print(f'new_data: {new_data}')
print(type(new_data))

string = None
file_path = '../../../sample2.json'
with open(file_path, 'r') as file:
    string = file.read()

print(string)
print(type(string))

json_object = json.loads(string)

print(json_object)
print(type(json_object))


df = pd.json_normalize(json_object)
print(f'dataframe {df}')

for row in df:
    print(df[row])
