# 19. Substring Search
# Check whether a given substring exists in the main string

main = input("Enter the main string: ")
sub = input("Enter the substring to search: ")

if sub in main:
    print("Substring found.")
else:
    print("Substring not found.")
