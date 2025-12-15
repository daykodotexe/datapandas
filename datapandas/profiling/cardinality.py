import pandas as pd

def cardinality_report(df, high_threshold=0.9, low_threshold=1):
    rows = len(df)
    report = {}

    for col in df.columns:
        unique = df[col].nunique(dropna=True)

        if unique <= low_threshold:
            report[col] = "low_cardinality"
        elif rows > 0 and unique / rows >= high_threshold:
            report[col] = "high_cardinality"

    return report
