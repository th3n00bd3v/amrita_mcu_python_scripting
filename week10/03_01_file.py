"""
use a context manager to open the file winnie_pooh.txt

try it two ways
a) make a Path object that points to winnie_pooh.txt
b) just write it in as a string (don't use a Path object)

Both are valid! The first method is the OO way and will yield better programs down the line.
The second way is fine for quick scripts though

## Tasks to try
1. Print out of the first line of the file
2. Print out all the entire file
3. Print in the last line of the file
4. Add a new sentence to the file "I AM A NEW SENTENCE!"

"""
from pathlib import Path

# Method 1

basedir = Path(__file__).parent
filepath = basedir / "winnie_pooh.txt"

with filepath.open("r", encoding="utf-8") as f:
    first_line = f.readline()
    print("First line:")
    print(first_line)
print()

with filepath.open("r", encoding="utf-8") as f:
    print("Entire file:")
    print(f.read())

print()

with filepath.open("r", encoding="utf-8") as f:
    lines = f.readlines()
    print("Last line:")
    print(lines[-1])

print()

with filepath.open("a", encoding="utf-8") as f:
    f.write("\nI AM A NEW SENTENCE!")


# Method 2

filename = "week10/winnie_pooh.txt"

with open(filename, "r", encoding="utf-8") as f:
    first_line = f.readline()
    print("First line:")
    print(first_line)
    
print()

with open(filename, "r", encoding="utf-8") as f:
    print("Entire file:")
    print(f.read())

print()

with open(filename, "r", encoding="utf-8") as f:
    lines = f.readlines()
    print("Last line:")
    print(lines[-1])

print()
with open(filename, "a", encoding="utf-8") as f:
    f.write("\nI AM A NEW SENTENCE! Again!")