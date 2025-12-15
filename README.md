# datapandas

[![PyPI version](https://badge.fury.io/py/datapandas.svg)](https://pypi.org/project/datapandas/)
[![Tests](https://github.com/daykodotexe/datapandas/actions/workflows/tests.yml/badge.svg)]

````markdown
# datapandas

**datapandas** is a lightweight Python library that provides practical data quality
and profiling utilities for **pandas DataFrames**.

It is designed to help you quickly sanity-check datasets before analysis,
modeling, or reporting.

---

## ✨ Features

### 🔍 Data Quality Checks (`datacheck`)
- Dataset summary (rows, columns)
- Missing value percentage
- Duplicate row percentage
- Simple outlier detection
- Clean, readable console output

### 📊 Data Profiling (`profiling`)
- Column cardinality analysis
- Detect constant columns
- Detect high-cardinality (ID-like) columns

---

## 📦 Installation

```bash
pip install datapandas
````

---

## 🚀 Quick Start

```python
import pandas as pd
from datapandas import datacheck, profiling

df = pd.DataFrame({
    "age": [25, 30, None, 40],
    "salary": [50000, 60000, 70000, 70000],
    "id": [1, 2, 3, 4]
})

# Pretty data quality summary
datacheck.pretty_summary(df)

# Column cardinality report
profiling.cardinality_report(df)
```

---

## 📌 Example Output

```text
Rows: 4
Columns: 3
Missing values: 8.33%
Duplicate rows: 0.00%
Outlier columns: ['salary']
```

```python
{'id': 'high_cardinality'}
```

---

## 🎯 Why datapandas?

* Simple and fast
* No heavy dependencies
* Designed for real-world data work
* Useful for analysts, students, and data scientists
* Easy to extend with new checks

---

## 🧪 Testing

Run tests locally with:

```bash
pytest
```

---

## 🛠 Roadmap

Planned features:

* Type drift detection
* Data quality score (0–100)
* Report export (JSON / HTML)
* Command-line interface (CLI)

---

## 📄 License

MIT License

---

## 👤 Author

Built by **daykodotexe**

GitHub: [https://github.com/daykodotexe/datapandas](https://github.com/daykodotexe/datapandas)
PyPI: [https://pypi.org/project/datapandas/](https://pypi.org/project/datapandas/)

````

Just tell me 👍
