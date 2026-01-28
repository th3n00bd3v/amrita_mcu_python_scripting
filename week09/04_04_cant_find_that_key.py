"""
Wrap the code below so the exception will be caught.

Handle the exception by adding the desired key with a default value.


"""
my_dict = {1: 2, 3: 4}

try:
    print(my_dict["hi"])

except KeyError:
    my_dict["hi"] = 0
    print("Key not found. Added default value.")
    print(my_dict["hi"])

print(my_dict)
