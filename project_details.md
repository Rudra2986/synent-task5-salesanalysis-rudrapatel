# Synent Technologies - Data Science Internship (Summer 2026)
## Task 5: Sales Data Analysis & Interactive Performance Dashboard (Consolidated Project Details)

> **Goal:** This document serves as a complete, self-contained reference detailing the dataset, code architecture, script functions, business insights, and environment configuration of the Sales Data Analysis project. You can provide this file to any LLM/AI to immediately grant it full context for debugging, explaining, or writing extension features.

---

## 👤 Author Information
- **Name:** Rudra Patel
- **Internship ID:** `SYN/J2/IP806`
- **Email:** `rudrapatel2156@gmail.com`
- **LinkedIn Profile:** [Rudra Patel](https://www.linkedin.com/in/rudrapatel-cs)
- **GitHub Profile:** [Rudra2986](https://www.github.com/Rudra2986)

---

## 📂 Project Directory Structure
```
Task-5-Sales-Analysis/
│
├── data/
│   ├── raw/                 # Contains raw transaction data
│   │   └── Sample - Superstore.csv
│   └── processed/           # Contains cleaned transaction data
│       └── cleaned_superstore.csv
│
├── notebooks/
│   └── sales_analysis.ipynb # Step-by-step Jupyter Notebook analysis
│
├── src/                     # Core python pipeline modules
│   ├── data_cleaning.py     # Clean dataset & check bounds
│   ├── revenue_analysis.py  # Monthly & Annual revenue seasonality
│   ├── profit_analysis.py   # Profit margin analysis by Category/Sub-category
│   ├── product_analysis.py  # Top product sales & volume metrics
│   ├── regional_analysis.py # State & Regional margin analysis
│   └── app.py               # Streamlit Dashboard code (interactive Plotly graphs)
│
├── reports/
│   └── sales_insights_report.md  # Executive business summary report
│
├── images/                  # Static PNG chart outputs
│   ├── revenue_trends.png
│   ├── profitability_analysis.png
│   ├── product_analysis.png
│   └── regional_performance.png
│
├── requirements.txt         # Project packages list
├── README.md                # General readme overview
└── project_details.md       # [This File] All-in-one AI context file
```

---

## 📊 Dataset Specifications
* **Dataset Name:** `Sample - Superstore.csv` (Located under `data/raw/`)
* **Shape:** $9,994$ records, $21$ columns.
* **Fields & Data Types:**
  1. `Row ID`: `int64` (Record counter)
  2. `Order ID`: `object` (Unique transaction code)
  3. `Order Date`: `datetime64[ns]` (Standardized from `MM/DD/YYYY` string)
  4. `Ship Date`: `datetime64[ns]` (Standardized from `MM/DD/YYYY` string)
  5. `Ship Mode`: `object` (Shipping class: e.g. Second Class, Standard Class)
  6. `Customer ID`: `object` (Unique customer code)
  7. `Customer Name`: `object` (Customer name string)
  8. `Segment`: `object` (Market segment: Consumer, Corporate, Home Office)
  9. `Country`: `object` (Country: United States)
  10. `City`: `object` (City name)
  11. `State`: `object` (State name)
  12. `Postal Code`: `object` (Standardized 5-digit string, padded with leading zeros)
  13. `Region`: `object` (US Region: East, West, Central, South)
  14. `Product ID`: `object` (Unique SKU)
  15. `Category`: `object` (Broad class: Technology, Office Supplies, Furniture)
  16. `Sub-Category`: `object` (e.g. Chairs, Tables, Paper, Envelopes)
  17. `Product Name`: `object` (Product name string)
  18. `Sales`: `float64` (Gross sale value in USD; validated $> 0$)
  19. `Quantity`: `int64` (Quantity of units purchased; validated $> 0$)
  20. `Discount`: `float64` (Discount percentage applied: $0.0$ to $0.8$)
  21. `Profit`: `float64` (Net profit/loss margin in USD)

---

## ⚙️ Dependencies & Virtual Env
The required modules in `requirements.txt` are:
* `pandas` & `numpy` (Data manipulation)
* `matplotlib` & `seaborn` (Static plotting)
* `plotly` (Dynamic web charts)
* `streamlit` (Dashboard builder)

---

## 🛠️ Code Modules & Logic Explanations

### 1. `src/data_cleaning.py`
* **Purpose:** Performs initial dataset health assessment and structures the transactional dataset.
* **Key Functions:**
  * `assess_dataset(df: pd.DataFrame) -> dict`: Inspects the dataset shape, computes null counts per column, tallies duplicate records, checks for boundary errors ($Sales \le 0$ or $Quantity \le 0$), and prints a comprehensive log report.
  * `clean_dataset(df: pd.DataFrame) -> pd.DataFrame`: Removes duplicate rows, parses date strings to datetime formats using format string `%m/%d/%Y`, standardizes `Postal Code` by zero-filling to 5-digit strings (`astype(str).str.zfill(5)`), and removes rows violating positive sales/quantity bounds.
* **Output:** Exports the cleaned dataframe to `data/processed/cleaned_superstore.csv`.

### 2. `src/revenue_analysis.py`
* **Purpose:** Researches revenue seasonality, temporal trends, and annual trajectories.
* **Key Steps:**
  * Groups sales by monthly periods (`df.to_period('M')`) and annual periods.
  * Computes Month-over-Month (MoM) growth rates.
  * Identifies highest and lowest revenue months.
  * Generates a Line Plot showing the monthly revenue trajectory across 2014-2017.
* **Output:** Saves the line plot as `images/revenue_trends.png` and prints a text summary in the console.

### 3. `src/profit_analysis.py`
* **Purpose:** Investigates profitability and net profit margins across customer segments, product categories, and sub-categories.
* **Key Calculations:**
  * $\text{Profit Margin (\%)} = \left( \frac{\text{Sum of Profit}}{\text{Sum of Sales}} \right) \times 100$
  * Groups data by Category and Sub-Category to flag high-margin drivers vs. loss leaks.
  * Generates visual bar charts of profit margins.
* **Output:** Saves the profitability grid as `images/profitability_analysis.png`.

### 4. `src/product_analysis.py`
* **Purpose:** Analyzes product sales performance.
* **Key Metrics:**
  * Aggregates total `Sales` and `Quantity` per product.
  * Isolates top 10 products by revenue and units sold.
  * Highlights high-volume low-cost items vs. high-cost low-volume items.
* **Output:** Saves the product comparisons as `images/product_analysis.png`.

### 5. `src/regional_analysis.py`
* **Purpose:** Isolates spatial sales performance.
* **Key Metrics:**
  * Groups metrics by geographical US Region and State.
  * Computes total sales, profits, and margin ratios.
  * Ranks top 5 sales-generating states and bottom 5 unprofitable states.
* **Output:** Saves the metrics as `images/regional_performance.png`.

### 6. `src/app.py`
* **Purpose:** Hosts the interactive multi-view Streamlit Dashboard.
* **Key Features:**
  * Uses path calculation relative to the script file directory (`os.path.dirname(os.path.abspath(__file__))`) to locate the processed dataset safely, resolving runtime pathing errors on deployment servers.
  * Filters the data dynamically in the sidebar by Segment, Category, Region, and Year.
  * Displays interactive KPI Metric cards: Total Revenue, Total Profit, Profit Margin (%), and Total Orders.
  * Implements multi-tab panels rendering Plotly visualizations: Sales & Profit Seasonality, Category breakdowns, State Sales Map, and Top Products charts.

---

## 🏆 Key Analytical Insights
1. **Steady Expansion:** Retail revenue rose from **$484,247.50** (2014) to **$733,215.26** (2017), an increase of $51.4\%$.
2. **Seasonality:** Strong seasonality exists in Q4 (specifically November and December), peaking at **$118,447.82** in November 2017. Q1 (January/February) experiences sales troughs.
3. **Product Margin Imbalance:** Technology ($17.4\%$ margin) and Office Supplies ($17.0\%$ margin) are highly profitable. Furniture ($2.49\%$ margin) is highly compressed due to major shipping costs.
4. **Profit Leaks:** **Tables** are highly unprofitable, losing **-$17,725.48** (a margin of $-8.56\%$).
5. **State-Level Losses:** **Texas** (-$25k net profit) and **Ohio** (-$16k net profit) are the worst-performing states due to extreme promotional discounting, despite ranking high in sales volume.

---

## 🤖 Instructions for AI Prompts
If you want to feed this project to another AI, copy and paste this prompt:

```text
You are an expert Data Scientist. I am providing you with the project details of my "Superstore Sales Analysis" project (Task 5).

Here is the setup:
- Raw dataset is located in 'data/raw/Sample - Superstore.csv'.
- Cleaned dataset is generated by 'src/data_cleaning.py' and exported to 'data/processed/cleaned_superstore.csv'.
- Downstream analysis is split into 'src/revenue_analysis.py', 'src/profit_analysis.py', 'src/product_analysis.py', and 'src/regional_analysis.py'.
- The dashboard is built using Streamlit in 'src/app.py'.

Please read this file configuration and assist me with:
1. Explain how to implement a specific extension (e.g., adding machine learning forecasting for Q4 sales, or adding a new discounting optimizer tab in Streamlit).
2. Debugging any pandas/numpy error that I paste.
3. Refactoring code to be modular or optimizing performance.
```
