# Project Plan: Sales Data Analysis
> **Synent Technologies - Data Science Internship (Summer 2026)**
> **Task 5: Intermediate Level**

---

## 🎯 Objectives
The primary objective of this project is to perform a detailed Exploratory Data Analysis (EDA) on a Superstore Sales Dataset to extract business performance insights. 

Key targets:
1. Clean and preprocess transaction data to remove inconsistencies.
2. Analyze sales and profit performance across time (monthly trends), product lines, and geographical boundaries.
3. Establish key business metrics like average order value (AOV), profit margins, and discount impacts.
4. Construct an interactive analytical dashboard (using Streamlit) to facilitate data-driven decision making.

---

## 🔄 Expected Workflow
The project will follow a structured data science pipeline:
```
[1. Planning & Setup] ➔ [2. Data Cleaning] ➔ [3. Exploratory Data Analysis (EDA)]
                                                            │
[6. Showcase & Submission] 🡨 [5. Dashboarding] 🡨 [4. Task-Specific Analysis]
```

1. **Planning & Setup (Current State):** Setting up the repository structures, dependencies, and environment.
2. **Data Cleaning:** Handle missing values, parse date columns, remove duplicate records, and ensure proper feature data types.
3. **Exploratory Data Analysis (EDA):** Perform initial distribution analysis, check correlation between variables (e.g., Sales vs Profit vs Discount).
4. **Task-Specific Analysis:**
   - **Revenue Analysis:** Track monthly and annual revenue trajectories to evaluate seasonality.
   - **Profit Analysis:** Evaluate profitability patterns by category, segment, and geographical regions.
   - **Product Analysis:** Discover top-performing and underperforming items and lines.
   - **Regional Analysis:** Trace distribution of sales/profit across different territories.
5. **Dashboarding:** Create a clean, responsive Streamlit dashboard application for dynamic interactions.
6. **Showcase & Submission:** Document findings, prepare a video demo, and submit.

---

## 📦 Deliverables
The final submission must include:
1. **GitHub Repository:** Publicly accessible, following the naming format: `synent-task5-salesanalysis-rudrapatel`.
2. **Data Folders:** Structured as `data/raw/` and `data/processed/`. (Do not commit large raw datasets; supply a README link or script to download).
3. **Jupyter Notebooks:** Well-documented notebook showing step-by-step code execution.
4. **Python Scripts:** Clean code files for analysis in `src/` directory.
5. **Streamlit App:** Interactive visualization code (`src/app.py`).
6. **Reports & Images:** Summary presentation/report under `reports/` and charts under `images/`.
7. **Video Demonstration:** A 1 to 3-minute video walk-through demonstrating execution, code architecture, and dashboard metrics.

---

## 🖥️ GitHub Submission Requirements
* **Repository Name:** `synent-task5-salesanalysis-rudrapatel`
* **Privacy:** Public repositories only.
* **Documentation:** The `README.md` must be thoroughly written, capturing problem statements, datasets, results, and environment installation instructions.
* **Version Control:** Regular, logical commits describing the stages of development.

---

## 🎥 Video Demonstration Requirements
* **Duration:** 1 to 3 minutes.
* **Voiceover:** Preferred (explain clear audio, screen sharing, and code walk-through).
* **Key Components to Cover:**
  - Introduction of yourself (your name).
  - High-level overview of the problem statement and dataset.
  - Brief code walk-through of cleaning and EDA in the notebook.
  - Interactive demonstration of the Streamlit dashboard app (live filters and charts).
  - Business insights and final conclusions.

---

## 📈 Expected Outputs
Upon project completion, the following output targets should be realized:
- **Cleaned Data:** Saved in `data/processed/superstore_sales_cleaned.csv`.
- **Trend Charts:** Monthly sales performance line graphs showing high-season patterns.
- **Product Insights:** Pareto charts identifying the top 20% of products generating 80% of sales and profit margins.
- **Regional Maps/Charts:** Bar graphs and bubble maps pointing out low-margin regions.
- **Interactive App:** Streamlit dashboard running locally via `streamlit run src/app.py`.
- **Business Insights Report:** Saved inside the `reports/` directory.
