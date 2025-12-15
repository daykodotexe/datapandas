import pandas as pd
from datapandas.profiling import cardinality_report

def test_cardinality_report():
    df = pd.DataFrame({
        "id": [1, 2, 3, 4],
        "constant": [1, 1, 1, 1],
        "value": [10, 20, 30, 40],
    })

    report = cardinality_report(df)
    assert "id" in report
    assert "constant" in report
