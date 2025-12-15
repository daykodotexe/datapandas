import pandas as pd


def outlier_report(df: pd.DataFrame, factor: float = 1.5) -> list:
    """
    detect numeric columns with potential outliers using IQR
    """
    numeric = df.select_dtypes(include="number")
    outliers = []

    for col in numeric.columns:
        q1 = numeric[col].quantile(0.25)
        q3 = numeric[col].quantile(0.75)
        iqr = q3 - q1

        if iqr == 0:
            continue

        lower = q1 - factor * iqr
        upper = q3 + factor * iqr

        if ((numeric[col] < lower) | (numeric[col] > upper)).any():
            outliers.append(col)

    return outliers
