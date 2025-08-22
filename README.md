# Scripts for Companies

Collection of small Python scripts and modules used for business tasks and
experiments.

## Contents

### `src/csvexcel`
Converts a CSV file into a formatted Excel workbook. The tool opens a file
selection dialog, optionally splits the data into worksheets by a chosen
column and applies basic header formatting.

Run with:
```bash
python src/csvexcel/main.py
```

### `src/ram`
A minimal in-memory byte-addressable RAM simulator. Demonstrates reading,
writing and iterating over memory contents.

Run the demo with:
```bash
python src/ram/main.py
```

### `src/leetcode_algorithms.py`
Collection of solutions to classic algorithmic problems inspired by LeetCode.
Each function is self-contained and demonstrates approaches to
common interview questions.

## Requirements

These scripts require Python 3.10+ and the following third-party packages:

- pandas
- openpyxl

Install dependencies with pip:
```bash
pip install pandas openpyxl
```

The `ram` module uses only the Python standard library.
