import re
text = input("Enter text file name: ")
target = input("Enter word to replace: ")
replacement = input("Enter replacement: ")
choice = input("Case-sensitive? (yes/no): ")

with open(text, "r") as f:
    data = f.read()

if choice.lower() == "yes":
    data = data.replace(target, replacement)
else:
    data = re.sub(re.escape(target), lambda m: replacement, data, flags=re.I)

with open("newfile.txt", "w") as f:
    f.write(data)

print("File saved as newfile.txt")