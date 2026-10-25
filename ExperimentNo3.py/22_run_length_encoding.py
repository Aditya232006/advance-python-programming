# 22. Run-Length Encoding
# Compress a string by counting consecutive repeated characters



s = input("Enter a string: ")

result = ""
i = 0

while i < len(s):
    count = 1

    while i + count < len(s) and s[i] == s[i + count]:
        count += 1

    result = result + s[i] + str(count)
    i = i + count

print("Compressed string:", result)
