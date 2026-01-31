"""
Use JSON to serialize the following dictionary

"""

import json

my_dict = {i: i ** 2 for i in range(10_000)}

with open('my_dict.json', 'w') as json_file:
    json.dump(my_dict, json_file)

# after creating your JSON file, try opening it the file by double clicking it in the explorer
# can you read it ? Why or why not?

with open('my_dict.json', 'r') as json_file:
    loaded_dict = json.load(json_file)

# use code to load your json file into a new variable
# print it out to make sure it's the same.

loaded_dict = {int(k): v for k, v in loaded_dict.items()} ## Converts the dictionary keys back to integers

print(loaded_dict == my_dict)
