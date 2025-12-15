import pandas as pd


def missing_report(df: pd.DataFrame) -> float:
    """
    return percentage of missing values in the df
    """
    total = df.size
    missing = df.isna().sum().sum()
    return round((missing / total) * 100, 2) if total > 0 else 0.0
