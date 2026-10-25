# 25. Second Most Frequent Character
# Find the second most frequently occurring character

s = input("Enter a string: ")
frequency = {}

for ch in s:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

sorted_items = sorted(frequency.items(), key=lambda item: item[1], reverse=True)

if len(sorted_items) < 2:
    print("There is no second most frequent character.")
else:
    print("Second most frequent character:", sorted_items[1][0])
    print("Frequency:", sorted_items[1][1])
