# Supply Chain & Inventory Analytics Dashboard

An end-to-end Power BI dashboard analyzing supply chain performance — delivery delays, shipping efficiency, and product-level stockout risk — built on 180K+ real order transactions.

## Overview

This project simulates a real-world business intelligence engagement: taking raw transactional order data and turning it into an executive-ready dashboard that answers three core business questions:

1. **How is delivery performance trending, and where are the delays happening?**
2. **Which products are at risk of stocking out based on recent demand shifts?**
3. **How do sales, delivery performance, and inventory risk connect at the category level?**

## Dataset

- **Source**: [DataCo Smart Supply Chain for Big Data Analysis](https://www.kaggle.com/datasets/shashwatwork/dataco-smart-supply-chain-for-big-data-analysis) (Kaggle)
- **Size**: 180,519 orders, 53 original columns, spanning 2015–2018
- **Cleaned to**: 180,508 rows, 47 columns after removing empty/sensitive fields

## Tools Used

- **Python (Pandas)** — data cleaning, feature engineering (Delay Days, Is Late)
- **Power BI Desktop** — data modeling, DAX measures, dashboard design
- **DAX** — custom business logic for delay metrics and stockout risk scoring
- **Git/GitHub** — version control

## Dashboard Pages

### 1. Executive Overview
High-level KPIs (Total Orders, Late Delivery %, Avg Delay Days, On-Time Rate, Total Sales), top-selling categories, regional delay hotspots, and a 4-year delivery performance trend.


### 2. Delivery Performance
Breaks down delay by shipping mode and geography, with a world map of delay intensity and a ranked table of the worst-performing regions.

### 3. Stockout Risk Analysis
A custom-built risk model: compares each product's **recent 30-day demand** against a derived reorder point to flag products at risk of stocking out — since the raw dataset has no live inventory field, this required deriving a demand-based proxy for stock risk.

### 4. Category Deep Dive
Combines sales, delay, and stockout risk in one view to show which categories are simultaneously high-demand and high-risk — the areas that matter most operationally.

## Key Insights

- **55% of all orders** were delivered late — a major systemic delivery issue, not an edge case
- **Second Class shipping** has the highest average delay (1.99 days); **Standard Class** the lowest
- **Central Asia and Central Africa** are the most delay-prone regions
- **6 products** were flagged high stockout risk based on recent demand acceleration, concentrated in Accessories, Girls' Apparel, and sporting goods categories
- Delivery performance dipped in 2016–2017 before sharply recovering into 2018

## Methodology Note: Stockout Risk Logic

Since this is transactional (not inventory-snapshot) data, stockout risk was derived rather than pulled directly:

```
Recent Avg Daily Demand = order quantity summed over the last 30 days / 30
Reorder Point = Recent Avg Daily Demand × 10 (lead time + safety stock buffer)
Simulated Stock = Overall Avg Daily Demand × 15
Stockout Risk = "High Risk" if Simulated Stock < Reorder Point, else "Safe"
```

This flags products whose **recent demand has accelerated** beyond what their historical average would suggest — the same pattern that causes real-world stockouts.

## Author

**Prajjwal Kumar** — [GitHub](https://github.com/Prajjwalkumar-ai)
