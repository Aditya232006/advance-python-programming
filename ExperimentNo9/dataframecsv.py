import pandas as pd
import os

file_path = os.path.join(os.path.dirname(__file__), "example.csv")

df = pd.read_csv(file_path)

print("DataFrame from CSV:")
print(df)