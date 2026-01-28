"""
implement a key-lookup procedure for a dictionary

Try to get the key and update the value by n
If an en exception is raised, handle it by creating the key with a default value
if no exception is raised, update the value
Regardless of what happens, print the dictionary
"""

## Answer coded below

def update_dict(d, key, n, default=0):
    try:
        # Try to get and update the existing key
        d[key] += n
    except KeyError:
        # If key doesn't exist, create it with a default value
        d[key] = default + n
    else:
        # Runs only if no exception was raised
        pass
    finally:
        # Always runs
        print(d)



data = {"a": 10, "b": 5}

update_dict(data, "a", 3)
update_dict(data, "c", 7)
update_dict(data, "d", -12)
