"""
Day 2: Data Cleaning
Purpose: Clean dataset, fix date formats, create delay metrics, drop empty columns
Output: cleaned CSV ready for Power BI
"""

import pandas as pd

# Load raw data
df = pd.read_csv("../data/supply_chain_data.csv", encoding="latin1")

print(f"Original shape: {df.shape}")

# 1. Drop fully/mostly empty columns (identified in Day 1) 
df = df.drop(columns=["Product Description", "Order Zipcode"])

# 2. Convert date columns to proper datetime
df["order date (DateOrders)"] = pd.to_datetime(df["order date (DateOrders)"])
df["shipping date (DateOrders)"] = pd.to_datetime(df["shipping date (DateOrders)"])

# 3. Create a clean "Actual Delay in Days" column
#    (real shipping days - scheduled shipping days; positive = late)
df["Delay Days"] = df["Days for shipping (real)"] - df["Days for shipment (scheduled)"]

# 4. Create a simple readable flag
df["Is Late"] = df["Late_delivery_risk"].map({1: "Late", 0: "On Time"})

# 5. Drop rows with missing Customer Lname / Customer Zipcode (very few, safe to drop)
df = df.dropna(subset=["Customer Lname", "Customer Zipcode"])

# 6. Drop sensitive/irrelevant columns for this analysis (not needed for supply chain KPIs)
df = df.drop(columns=["Customer Email", "Customer Password", "Customer Fname", "Customer Lname", "Customer Street", "Product Image"])

print(f"Cleaned shape: {df.shape}")
print(f"\nDelay Days summary:\n{df['Delay Days'].describe()}")
print(f"\nIs Late counts:\n{df['Is Late'].value_counts()}")

# Save cleaned file
df.to_csv("../data/supply_chain_clean.csv", index=False)
print("\nSaved cleaned file to data/supply_chain_clean.csv")