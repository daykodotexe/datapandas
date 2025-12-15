import pandas as pd


def duplicate_report(df: pd.DataFrame) -> float:
    """
    return percentage of duplicate rows in the df
    """
    if len(df) == 0:
        return 0.0
    dupes = df.duplicated().sum()
    return round((dupes / len(df)) * 100, 2)
