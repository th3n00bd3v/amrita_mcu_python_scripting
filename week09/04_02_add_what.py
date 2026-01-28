"""
Write a function that takes two inputs and attempts to add them together.

Use a try/except block to catch all possible errors

Try adding
int + int
int + str
str + list
tuple + list
dict + dict
dict + str

Are all the exceptions the same?
"""

def try_add(a, b):
    try:
        result = a + b
        print(f"{a!r} + {b!r} = {result!r}")
    except Exception as e:
        print(f"Error adding {type(a).__name__} + {type(b).__name__}")
        print(f"Exception type: {type(e).__name__}")
        print(f"Message: {e}")

try_add(5, 10)
try_add(5, "hello")
try_add("hello", [1, 2, 3])
try_add((1, 2), [3, 4])
try_add({"a": 1}, {"b": 2})
try_add({"a": 1}, "world")