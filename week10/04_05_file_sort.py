"""

Create two new folders
a. vowel
b. consonant

Iterate over your previously created files from 04_04_split_file.py
Open each file and check if the first word begins in a vowel or consonant
If it begins in a vowel, move the file to the vowel folder
Otherwise move the file to the consonant folder

"""
from pathlib import Path
import shutil

source_dir = Path("winnie_pooh_split")
vowel_dir = Path("vowel")
consonant_dir = Path("consonant")

vowel_dir.mkdir(exist_ok=True)
consonant_dir.mkdir(exist_ok=True) 

vowels = set("AEIOUaeiou")
for file_path in source_dir.iterdir():
    if file_path.is_file():
        with file_path.open("r") as f:
            first_line = f.readline().strip()
            first_word = first_line.split()[0] if first_line else ""

            if first_word and first_word[0] in vowels:
                target_dir = vowel_dir
            else:
                target_dir = consonant_dir

        shutil.move(str(file_path), target_dir / file_path.name)
        print(f"Moved {file_path.name} to {target_dir}")
        
