# 16. Character Frequency
# Display the frequency of every character in a string

s = input("Enter a string: ")
frequency = {}

for ch in s:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

print("Character frequency:")
for ch, count in frequency.items():
    print(ch, ":", count)
