book1 = set(input("Enter Book 1 text: ").lower().split())
book2 = set(input("Enter Book 2 text: ").lower().split())

print("Book 1 Unique Words:", book1)
print("Book 2 Unique Words:", book2)
print("Common Words:", book1 & book2)
print("Only in Book 1:", book1 - book2)
print("Only in Book 2:", book2 - book1)
print("Total Unique Words:", len(book1 | book2))