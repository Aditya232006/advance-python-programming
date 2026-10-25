import re

files = input("Enter filenames: ").split()
count = {}

for file in files:
    match = re.search(r'\.[^.]+$', file)
    if match:
        ext = match.group()
        count[ext] = count.get(ext, 0) + 1

print(count)