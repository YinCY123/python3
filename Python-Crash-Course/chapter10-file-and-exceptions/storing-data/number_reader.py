import json

filename = 'numbers.json'
with open(filename, 'r') as f_obj:
    numbers = json.load(f_obj)

print(numbers)