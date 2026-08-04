"""
Day 1: Supply Chain Dataset Exploration
Purpose: Understand the dataset structure before building the Power BI dashboard
"""

import pandas as pd

# Load dataset (DataCo dataset often needs latin1 encoding)
df = pd.read_csv("../data/supply_chain_data.csv", encoding="latin1")

print("=" * 60)
print("BASIC INFO")
print("=" * 60)
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
print()

print("=" * 60)
print("COLUMN NAMES")
print("=" * 60)
for col in df.columns:
    print(col)
print()

print("=" * 60)
print("DATA TYPES")
print("=" * 60)
print(df.dtypes)
print()

print("=" * 60)
print("MISSING VALUES (top 15 columns with most nulls)")
print("=" * 60)
print(df.isnull().sum().sort_values(ascending=False).head(15))
print()

print("=" * 60)
print("SAMPLE ROWS")
print("=" * 60)
print(df.head(5))
print()

print("=" * 60)
print("KEY DATE/DELAY COLUMNS (adjust names after checking column list above)")
print("=" * 60)
# Common column names in DataCo dataset - verify against your actual columns
possible_date_cols = [c for c in df.columns if "date" in c.lower() or "Date" in c]
print("Columns with 'date' in name:", possible_date_cols)

possible_delay_cols = [c for c in df.columns if "delay" in c.lower() or "late" in c.lower() or "risk" in c.lower()]
print("Columns with 'delay/late/risk' in name:", possible_delay_cols)

# Save a cleaned summary to file for reference
with open("../data/column_summary.txt", "w") as f:
    f.write("COLUMNS:\n")
    for col in df.columns:
        f.write(f"{col} | dtype: {df[col].dtype} | nulls: {df[col].isnull().sum()}\n")

print("\nSaved column summary to data/column_summary.txt")