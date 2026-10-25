import re

text = input("Enter paragraph: ")

text = re.sub(r'\b(Dr|Mr|Mrs|Ms|Prof)\.', r'\1<DOT>', text)
sentences = re.split(r'(?<=[.!?])\s+', text)
sentences = [s.replace("<DOT>", ".").strip() for s in sentences if s.strip()]

print(sentences)