import pandas as pd
from datacheck import summary, missing_report, duplicate_report, outlier_report


def sample_df():
    return pd.DataFrame({
        "a": [1, 2, 3, None],
        "b": [10, 10, 10, 10],
        "c": [100, 200, 300, 10000],
    })


def test_missing_report():
    df = sample_df()
    pct = missing_report(df)
    assert pct > 0


def test_duplicate_report():
    df = sample_df()
    pct = duplicate_report(df)
    assert pct == 0.0


def test_outlier_report():
    df = sample_df()
    outliers = outlier_report(df)
    assert "c" in outliers


def test_summary_keys():
    df = sample_df()
    report = summary(df)

    assert "rows" in report
    assert "columns" in report
    assert "missing_pct" in report
    assert "duplicate_pct" in report
    assert "outlier_columns" in report
