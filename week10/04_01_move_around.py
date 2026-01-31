"""
Use the following commands to look around your directory
You may want to do this exercise interactively with an interpreter session

Path.cwd() gets the current working directory, returns a Path object
os.chdir(path)  changes directory	

os.listdir() files and directories, returns a list
Path.glob(“*”)  returns a generator that you can use to iterate over all files and directories. Advantage is you can filter the results easily on the input.
Path.iterdir()

"""

import os
from pathlib import Path

# 1. Print the current working directory
print("Current working directory:")
cwd = Path.cwd()
print("CWD:", cwd)
print("Type:", type(cwd))
print()

# 2. Change directory to parent directory

print("Changing directory to parent directory:")
print("Before:", Path.cwd())
os.chdir("..")   # go up one directory
print("After:", Path.cwd())
print()

# 3. List directory contents using os.listdir()

print("Directory contents using os.listdir():")
items = os.listdir()
print(items)
print(type(items))
print()

# 4. Replace os.listdir() with Path.iterdir()

print("Directory contents using Path.iterdir():")
for item in Path.cwd().iterdir():
    print(item, "| dir:", item.is_dir(), "| file:", item.is_file())

print()

# 5. Pattern-based listing with Path.glob("*")

print("Pattern-based listing with Path.glob('*'):")
for item in cwd.glob("*.txt"):
    print(item)
print()