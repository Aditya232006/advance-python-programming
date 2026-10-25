# 15. Remove single-line comments from a Python source file


file = open("program.py", "r")
output = open("without_comments.py", "w")

for line in file:
    if not line.strip().startswith("#"):
        output.write(line)

file.close()
output.close()

print("Comments removed successfully.")