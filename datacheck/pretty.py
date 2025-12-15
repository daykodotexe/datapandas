from datacheck.summary import summary


def pretty_summary(df) -> None:
    """
    print a human-readable data quality summary
    """
    report = summary(df)

    print("📊 Data Quality Summary")
    print("-" * 30)
    print(f"Rows: {report['rows']}")
    print(f"Columns: {report['columns']}")
    print(f"Missing values: {report['missing_pct']}%")
    print(f"Duplicate rows: {report['duplicate_pct']}%")

    if report["outlier_columns"]:
        print("Potential outliers detected in:")
        for col in report["outlier_columns"]:
            print(f"  - {col}")
    else:
        print("No obvious outliers detected.")
