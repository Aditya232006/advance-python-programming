# 24. Most Frequent Character
# Find the character with the highest frequency

s = input("Enter a string: ")
frequency = {}

for ch in s:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

most_frequent = max(frequency, key=frequency.get)
print("Most frequent character:", most_frequent)
print("Frequency:", frequency[most_frequent])
