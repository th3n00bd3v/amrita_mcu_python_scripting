"""
Use pathlib.Path objects to 

a) create a new directory
b) create a new file
c) move a file from your current directory into the new directory

use shutil to
d) copy the file back into the original location (while keeping it in the new directory)

"""

import os
from pathlib import Path
import shutil

new_dir = Path("tempdir")
new_file = Path("temp.txt")

print("Creating new directory:", new_dir)
new_dir.mkdir(exist_ok=True)
print("Directory created.")
print()

print("Creating new file:", new_file)
with new_file.open("w") as f:
    f.write("This is a temporary file.\n")
    print("File created.")
print()

print("Moving file into new directory...")
shutil.move(new_file, new_dir / new_file.name)
print("File moved to directory:" , new_dir / new_file.name)
print()

print("Copying file back to original location...")
shutil.copy(str(new_dir / new_file.name), str(new_file))
print("File copied back.")




