📊 datapandas

**datapandas** is a lightweight Python library for **data quality checks and profiling**
on **pandas DataFrames**, with a **pre-analysis quality gate** to catch issues
before analysis or machine learning.

It helps you quickly sanity-check datasets **without heavy dependencies or complex configuration**.

---

## ✨ Features

### 🔍 Data Quality Checks (`datacheck`)
- Dataset overview (rows & columns)
- Missing value percentage (threshold-based)
- Duplicate row percentage (threshold-based)
- Detection of constant columns
- Detection of high-cardinality (ID-like) columns
- **PASS / WARN / FAIL quality status**
- Clean, readable console output

### 📊 Data Profiling (`profiling`)
- Column cardinality analysis
- Detection of constant columns
- Detection of high-cardinality (ID-like) columns

---

## 📦 Installation

```bash
pip install datapandas
````

---

## 🚀 Quick Start

```python
import pandas as pd
from datapandas import datacheck

df = pd.DataFrame({
    "age": [25, 30, None, 40],
    "salary": [50000, 60000, 70000, 70000],
    "id": [1, 2, 3, 4]
})

report = datacheck.run(df, missing_threshold=0.05)
report.summary()

if report.status == "FAIL":
    raise ValueError("Dataset failed basic quality checks")
```

---

## 🚦 Data Quality Gate

`datapandas` can be used as a lightweight **quality gate** before analysis or modeling.

Each check returns a status:

* **PASS** — no issue detected
* **WARN** — potential issue detected
* **FAIL** — threshold exceeded

The overall dataset status is the **worst status across all checks**.

---

## 📌 Example Output

```text
Overall Status: FAIL
- missing_values: FAIL (25.00% missing)
- duplicate_rows: PASS (0.00% duplicate rows)
- constant_columns: PASS (0 constant columns)
- high_cardinality_columns: WARN (1 high-cardinality column)
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
* Report export (HTML)
* Command-line interface (CLI)

---

## 👤 Author

Built by **daykodotexe**

* GitHub: [https://github.com/daykodotexe/datapandas](https://github.com/daykodotexe/datapandas)
* PyPI: [https://pypi.org/project/datapandas/](https://pypi.org/project/datapandas/)

```

---

## ✅ What to do next (no thinking required)
1. Copy-paste this into `README.md`
2. Commit it
3. Bump version to `0.2.0`
4. Ship to PyPI

You’re done with README.  
Next time someone stars your repo, **this is why**.

If you want, next I can:
- sanity-check your repo before release  
- write release notes  
- help you post the PR announcement  

Just say it.
```
