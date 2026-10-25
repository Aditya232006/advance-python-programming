import pandas as pd
from datetime import date

df = pd.read_csv("bod.csv")

today = date.today()

df["Age"] = df["BirthDate"].apply(
    lambda x: today.year - int(x[:4])
)

print("Student Details:")
print(df)