import os

f = open("test.txt", "w")
f.write("Hello Python")
f.close()

f = open("test.txt", "r")
print(f.read())
f.close()

os.rename("test.txt", "new.txt")
print("File renamed")

os.remove("new.txt")
print("File deleted")
