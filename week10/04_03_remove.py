"""
CAUTION
Deleting anything with python will permanently delete the file!
You will not be able to recover anything you delete with python!
USE CAUTION!
CAUTION

Use Path.rmdir() and Path.unlink() to delete a folder and file respectively

"""

import os
from pathlib import Path
import shutil

new_dir = Path("tempdir")
new_file = Path("temp.txt")
moved_file = new_dir / new_file.name

print("Deleting copied file:", new_file)
if new_file.exists():
    new_file.unlink()
    print("File deleted.")
else:
    print("File does not exist, cannot delete.")
print()

print("Deleting moved file:", moved_file)
if moved_file.exists():
    moved_file.unlink()
    print("File deleted.")
else:
    print("File does not exist, cannot delete.")
print()

print("Deleting directory:", new_dir)
if new_dir.exists():
    new_dir.rmdir()
    print("Directory deleted.")
else:
    print("Directory does not exist, cannot delete.")
print()
