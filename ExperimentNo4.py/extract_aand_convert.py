import re
from datetime import datetime

text = input("Enter text: ")

pattern = r'\d{2}/\d{2}/\d{4}|\d{2}-\d{2}-\d{4}|\d{4}\.\d{2}\.\d{2}|[A-Za-z]+ \d{1,2}, \d{4}'
dates = re.findall(pattern, text)

for d in dates:
    for fmt in ("%d/%m/%Y", "%m-%d-%Y", "%Y.%m.%d", "%B %d, %Y"):
        try:
            print(datetime.strptime(d, fmt).strftime("%Y-%m-%d"))
            break
        except ValueError:
            pass