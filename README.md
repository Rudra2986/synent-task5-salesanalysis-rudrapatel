# synent-task5-salesanalysis-rudrapatel
> **Synent Technologies - Data Science Internship (Summer 2026)**  
> **Task 5: Sales Data Analysis & Interactive Performance Dashboard**

---

## 📌 Project Overview
This project presents a comprehensive, end-to-end data analysis of the **Superstore Sales Dataset** (comprising $9,994$ customer transactions). The objective is to identify seasonal sales trends, examine category profit margins, diagnose loss-making products/regions, and deliver strategic recommendations to improve retail profitability.

An interactive analytical **Streamlit Dashboard** was developed to allow business stakeholders to dynamically filter performance metrics by customer segment, product category, and geography.

---

## 📊 Dataset Information
* **Dataset Name:** `Sample - Superstore.csv`
* **Format:** Comma-Separated Values (CSV)
* **Shape:** $9,994$ records, $21$ columns
* **Features Inspected:**
  * **Order Tracking:** `Order ID`, `Order Date`, `Ship Date`, `Ship Mode`
  * **Customer Demographics:** `Customer ID`, `Customer Name`, `Segment`
  * **Geography:** `Country`, `City`, `State`, `Postal Code`, `Region`
  * **Product Attributes:** `Product ID`, `Category`, `Sub-Category`, `Product Name`
  * **Financial Measures:** `Sales` (Gross Revenue), `Quantity` (Volume), `Discount` (%), `Profit` (Net Income)

---

## 🎯 Objectives
- Build a Python pipeline to clean and structure transaction records.
- Track monthly and annual revenue trajectories to evaluate seasonality.
- Calculate profit margins across segments, categories, and territories.
- Isolate loss-making products and discounting leaks.
- Develop and deploy a local Streamlit web application.

---

## 🛠️ Technologies Used
- **Language:** Python 3.10+
- **Data Manipulation:** `pandas`, `numpy`
- **Visualization:** `matplotlib`, `seaborn`
- **Interactive Plotting:** `plotly`
- **Web App Dashboard:** `streamlit`
- **Environment:** Jupyter Notebook, VS Code

---

## 🧪 Methodology
1. **Dataset Assessment:** Inspected types, nulls, duplicates, and validated numeric bounds ($Sales > 0$, $Quantity > 0$).
2. **Data Cleaning:** Parsed `Order Date` and `Ship Date` to `datetime64[ns]` objects, standardized US `Postal Code` as a 5-digit string, and exported results to `data/processed/cleaned_superstore.csv`.
3. **Exploratory Data Analysis:** Computed distributions, categorized segments, and plotted trends.
4. **Dashboard Development:** Constructed an interactive sidebar filtering panel and a multi-tab Plotly visualization web application.

---

## 🏆 Key Insights & Results
* **Strong Long-Term Growth:** Annual revenue rose from **$484,247.50** in 2014 to **$733,215.26** in 2017 (a $51.4\%$ increase).
* **Q4 Seasonality Peaks:** November and December represent the highest-selling periods. November 2017 was the record-high month, generating **$118,447.82**.
* **Profit Engine Categories:** **Technology** ($17.40\%$ margin) and **Office Supplies** ($17.04\%$ margin) drive the net profit pool.
* **Furniture Margin Compression:** Despite making up over $30\%$ of total revenue, **Furniture** yields a minimal profit margin of **$2.49\%$** due to major transport costs and negative profit lines like **Tables** (-$17,725.48 net profit).
* **State Leakage Hotspots:** California ($76k profit) and New York ($74k profit) perform exceptionally well. However, **Texas** (-$25,729.36 net loss) and **Ohio** (-$16,971.38 net loss) are deeply unprofitable due to excessive local discounting.

---

## 📈 Visualizations
Static charts are saved inside the [images/](file:///c:/COLLEGE/Synent-Internship-2026/Task-5-Sales-Analysis/images/) folder:
1. **[sales_profit_distributions.png](file:///c:/COLLEGE/Synent-Internship-2026/Task-5-Sales-Analysis/images/sales_profit_distributions.png):** Histograms showing the distribution of sales and profit.
2. **[revenue_trends.png](file:///c:/COLLEGE/Synent-Internship-2026/Task-5-Sales-Analysis/images/revenue_trends.png):** Line chart showing monthly seasonality.
3. **[profitability_analysis.png](file:///c:/COLLEGE/Synent-Internship-2026/Task-5-Sales-Analysis/images/profitability_analysis.png):** Visualizing margins by segment, category, and sub-category.
4. **[product_analysis.png](file:///c:/COLLEGE/Synent-Internship-2026/Task-5-Sales-Analysis/images/product_analysis.png):** Displays top 10 products by revenue and volume.
5. **[regional_performance.png](file:///c:/COLLEGE/Synent-Internship-2026/Task-5-Sales-Analysis/images/regional_performance.png):** Bar charts showing top sales-generating states and their relative profit margins.

---

## 📂 Project Structure
```
Task-5-Sales-Analysis/
│
├── data/
│   ├── raw/                 # Contains Sample - Superstore.csv
│   └── processed/           # Contains cleaned_superstore.csv
│
├── notebooks/
│   └── sales_analysis.ipynb # Complete step-by-step Jupyter Notebook
│
├── src/
│   ├── data_cleaning.py     # Assessment & Cleaning Pipeline
│   ├── revenue_analysis.py  # Monthly revenue trend metrics
│   ├── profit_analysis.py   # Margin calculations by category
│   ├── product_analysis.py  # Top product sales
│   ├── regional_analysis.py # State-level metrics
│   └── app.py               # Streamlit Dashboard App
│
├── reports/
│   └── sales_insights_report.md  # Business Insights Executive Report
│
├── images/                  # PNG Visualizations
├── models/                  # Placeholder for model files
├── README.md                # Recruiter-friendly guide
└── requirements.txt         # Project dependencies
```

---

## ⚙️ How To Run

### 1. Install Dependencies
Initialize your virtual environment (optional) and install requirements:
```powershell
pip install -r requirements.txt
```

### 2. Run the Data Pipeline
Execute the data cleaning script to generate `cleaned_superstore.csv`:
```powershell
python src/data_cleaning.py
```

### 3. Run Analysis Modules (Optional)
Generate the static visualizations and print console insights:
```powershell
python src/revenue_analysis.py
python src/profit_analysis.py
python src/product_analysis.py
python src/regional_analysis.py
```

### 4. Run the Streamlit Dashboard
Launch the interactive web-based dashboard:
```powershell
streamlit run src/app.py
```
This command will open the interactive dashboard in your default web browser (typically at `http://localhost:8501`).

---

## 👤 Author Information
- **Name:** Rudra Patel
- **Internship ID:** `SYN/J2/IP806`
- **Email:** `rudrapatel2156@gmail.com`
- **LinkedIn Profile:** [Rudra Patel](https://www.linkedin.com/in/rudrapatel-cs)
- **GitHub Profile:** [Rudra2986](https://www.github.com/Rudra2986)
