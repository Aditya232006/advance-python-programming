# 13. Search for a word and display occurrences and line numbers
search_word = input("Enter word to search: ")

file = open("student.txt", "r")

count = 0
line_numbers = []

for line_no, line in enumerate(file, start=1):
    words = line.split()

    for word in words:
        if word.strip(".,!?").lower() == search_word.lower():
            count += 1
            line_numbers.append(line_no)

file.close()

print("Number of occurrences:", count)
print("Line numbers:", line_numbers)