import re

text = "Python is easy. Python is powerful. I love Python."

result = re.match(r"Python", text)

if result:
    print("1. match():", result.group())
else:
    print("1. match(): No match")

result = re.search(r"powerful", text)

if result:
    print("2. search():", result.group())
else:
    print("2. search(): No match")

result = re.findall(r"Python", text)
print("3. findall():", result)



print("4. finditer():")
for match in re.finditer(r"Python", text):
    print("   Found:", match.group(), "at position", match.start())

result = re.split(r"\.", text)
print("5. split():", result)

result = re.sub(r"Python", "Java", text)
print("6. sub():", result)


result = re.subn(r"Python", "Java", text)
print("7. subn():", result)

text2 = "12345"

result = re.fullmatch(r"\d+", text2)

if result:
    print("8. fullmatch(): Complete string matched")
else:
    print("8. fullmatch(): No complete match")


pattern = re.compile(r"\d+")

numbers = pattern.findall("My marks are 85 and 90")
print("9. compile():", numbers)