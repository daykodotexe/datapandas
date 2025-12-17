from .report import Report

def run(df, missing_threshold=0.05, duplicate_threshold=0.01):
    checks = {}

    missing_ratio = df.isna().sum().sum() / df.size
    checks["missing_values"] = {
        "value": missing_ratio,
        "status": "FAIL" if missing_ratio > missing_threshold else "PASS",
        "message": f"{missing_ratio:.2%} missing"
    }

    dup_ratio = df.duplicated().mean()
    checks["duplicate_rows"] = {
        "value": dup_ratio,
        "status": "FAIL" if dup_ratio > duplicate_threshold else "PASS",
        "message": f"{dup_ratio:.2%} duplicate rows"
    }

    
    constant_cols = [c for c in df.columns if df[c].nunique(dropna=False) == 1]
    checks["constant_columns"] = {
        "value": constant_cols,
        "status": "WARN" if constant_cols else "PASS",
        "message": f"{len(constant_cols)} constant columns"
    }

    
    high_card_cols = [
        c for c in df.columns if df[c].nunique() / len(df) > 0.9
    ]
    checks["high_cardinality_columns"] = {
        "value": high_card_cols,
        "status": "WARN" if high_card_cols else "PASS",
        "message": f"{len(high_card_cols)} high-cardinality columns"
    }

    return Report(checks)
