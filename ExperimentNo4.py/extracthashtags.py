import re

text = input("Enter post: ")
print(re.findall(r'#[A-Za-z0-9_]+', text))