# 📊 datapandas

**datapandas** is a lightweight Python library for **data quality checks and profiling**
on **pandas DataFrames**.

It helps you **quickly sanity-check datasets** before analysis, modeling, or reporting —
without heavy dependencies or complex configuration.

---

## ✨ Features

### 🔍 Data Quality Checks (`datacheck`)

* Dataset overview (rows & columns)
* Missing value percentage
* Duplicate row percentage
* Simple outlier detection
* Clean, readable console output

### 📊 Data Profiling (`profiling`)

* Column cardinality analysis
* Detection of constant columns
* Detection of high-cardinality (ID-like) columns

---

## 📦 Installation

```bash
pip install datapandas
```

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

* ⚡ Simple and fast
* 🪶 Lightweight (no heavy dependencies)
* 🧠 Designed for real-world data workflows
* 🎓 Useful for analysts, students, and data scientists
* 🧩 Easy to extend with custom checks

---

## 🧪 Testing

Run tests locally with:

```bash
pytest
```

---

## 🛠 Roadmap

Planned features include:

* Type drift detection
* Data quality score (0–100)
* Report export (JSON / HTML)
* Command-line interface (CLI)

---

## 👤 Author

Built by **daykodotexe**

* GitHub: [https://github.com/daykodotexe/datapandas](https://github.com/daykodotexe/datapandas)
* PyPI: [https://pypi.org/project/datapandas/](https://pypi.org/project/datapandas/)

Say the word.
