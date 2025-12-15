import pandas as pd
from dqch.missing import missing_report
from dqch.duplicates import duplicate_report
from dqch.outliers import outlier_report


def summary(df: pd.DataFrame) -> dict:
    """
    Generate a quick data quality summary for a pandas DataFrame.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame")

    report = {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "missing_pct": missing_report(df),
        "duplicate_pct": duplicate_report(df),
        "outlier_columns": outlier_report(df),
    }

    return report
