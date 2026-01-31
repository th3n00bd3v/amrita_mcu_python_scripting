"""

1. Open winnie_pooh.txt
2. read in 100 lines at a time
3. after each 100 lines, write those lines to a new file
4. name each file differently (create a system to auto-increment the file names)
5. place all the files in a new folder (that you needed to create earlier)


"""
from pathlib import Path
import os

source_file = Path("winnie_pooh.txt")
output_dir = Path("winnie_pooh_split")

output_dir.mkdir(exist_ok=True)

file_lines = 100

with source_file.open("r") as f:
    file_count = 1

    while True:
        lines = []

        for _ in range(file_lines):
            line = f.readline()
            if not line:
                break
            lines.append(line)

        if not lines:
            break

        output_file = output_dir / f"winnie_pooh_part_{file_count}.txt"
        with output_file.open("w") as out_f:
            out_f.writelines(lines)

        print(f"Wrote {len(lines)} lines to {output_file}")
        file_count += 1