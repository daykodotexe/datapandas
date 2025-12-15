import pandas as pd
from datacheck import summary, pretty_summary

df = pd.DataFrame({
    "age": [23, 25, None, 40],
    "salary": [50000, 52000, 51000, 200000]
})

print(summary(df))
pretty_summary(df)
