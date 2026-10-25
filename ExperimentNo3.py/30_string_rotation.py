str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if len(str1) == len(str2) and str2 in str1 + str1:
    print("Yes")
else:
    print("No")


# String Rotation Check

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if len(str1) != len(str2):
    print("No")
else:
    combined = str1 + str1

    if str2 in combined:
        print("Yes")
    else:
        print("No")