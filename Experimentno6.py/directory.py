import os

print("Current Directory:", os.getcwd())
if not os.path.exists("MyFolder"):
    os.mkdir("MyFolder")
    print("Directory created successfully")
else:
    print("Directory already exists")

print("Directory Contents:", os.listdir())
print("Directory Exists:", os.path.exists("MyFolder"))

if os.path.exists("MyFolder") and not os.path.exists("NewFolder"):
    os.rename("MyFolder", "NewFolder")
    print("Directory renamed successfully")

print("Is Directory:", os.path.isdir("NewFolder"))

print("Absolute Path:", os.path.abspath("NewFolder"))
if os.path.exists("NewFolder") and os.path.isdir("NewFolder"):
    os.rmdir("NewFolder")
    print("Directory removed successfully")