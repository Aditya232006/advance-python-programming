marital = input("Enter marital status (married/unmarried): ").lower()
gender = input("Enter gender (male/female): ").lower()
age = int(input("Enter age: "))

if marital == "married":
  print("Driver is Insured.")
elif marital == "unmarried" and gender == "male" and age > 30:
  print("Driver is Insured.")
elif marital == "unmarried" and gender == "female" and age > 25:
  print("Driver is Insured.")
else:
  print("Driver is Not Insured.")