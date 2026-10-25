import numpy as np
import pandas as pd

arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

df = pd.DataFrame(
    arr,
    index=["A", "B", "C"],
    columns=["X", "Y", "Z"]
)

print(df)