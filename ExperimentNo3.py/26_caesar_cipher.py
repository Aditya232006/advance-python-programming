# 26. Caesar Cipher
# Encrypt and decrypt a message using the Caesar Cipher algorithm

text = input("Enter a message: ")
shift = int(input("Enter shift value: "))
choice = input("Encrypt or Decrypt? (E/D): ").upper()

result = ""

for ch in text:
    if ch.isalpha():
        base = ord('A') if ch.isupper() else ord('a')
        offset = (ord(ch) - base + shift) % 26
        result += chr(base + offset)
    else:
        result += ch

if choice == 'D':
    shift = -shift
    result = ""
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            offset = (ord(ch) - base + shift) % 26
            result += chr(base + offset)
        else:
            result += ch

print("Result:", result)
