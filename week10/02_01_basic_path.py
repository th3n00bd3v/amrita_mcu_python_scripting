"""
Let's make a very basic Path object

"""

from pathlib import Path

##
cwd = Path(__file__).parent

## create a new path using concatenation



# you can use cwd.joinpath
# or you can use the special / symbol (overloaded for concatenation)

path1 = cwd.joinpath("winnie_pooh.txt")

## Option 2

path2 = cwd / "winnie_pooh.txt"

## examine your new path object

p = path2


## print the following parts

# .parent

# .anchor

# .name

# .stem

# .suffix

# .parent


print("parent:", p.parent)
print("anchor:", p.anchor)
print("name:", p.name)
print("stem:", p.stem)
print("suffix:", p.suffix)
print()



## check if your path is a directory or file

## .is_file()

## .is_dir()

print("is_file():", p.is_file())
print("is_dir():", p.is_dir())

## print out your path and look at the type (you may need to print(type(your_path_here)))
## does it accurately reflect your OS?

print("Full path:", cwd)
print("Type:", type(cwd))
print()