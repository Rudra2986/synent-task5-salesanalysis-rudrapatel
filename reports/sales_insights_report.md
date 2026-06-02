# Business Insights Report: Superstore Sales Performance Analysis
> **Prepared for:** Synent Technologies Data Science Division  
> **Prepared by:** Rudra Patel (Data Science Intern)  
> **Date:** June 2, 2026  

---

## 📋 Executive Summary
This report summarizes the operational and financial performance of the Superstore based on the detailed analysis of $9,994$ order transactions from 2014 to 2017. While the business shows healthy annual growth and excellent margins in key product categories (Technology and Office Supplies), severe profitability leaks exist in the Furniture category and several major states (such as Texas and Ohio). This report outlines the main findings and provides data-driven recommendations to stabilize margins and drive growth.

---

## 📈 Key Findings
1. **Revenue Growth:** Annual revenue grew from **$484,247.50** in 2014 to **$733,215.26** in 2017, representing a $51.4\%$ cumulative sales expansion.
2. **Category Imbalances:** Technology and Office Supplies generate **$267,945.75** in combined net profit (margins $>17\%$). Conversely, Furniture accounts for $32.3\%$ of sales but contributes only **$18,451.27** to net profit (a marginal margin of $2.49\%$).
3. **Loss Hotspots:** Sub-categories like **Tables** (-$17,725.48 net loss) and states like **Texas** (-$25,729.36 net loss) are significantly eroding overall business profit margins.

---

## 📊 Revenue Insights (Phase 4)
* **Seasonal Sales Peaks:** Monthly sales are heavily seasonal, consistently peaking in **November** and **December**. The single highest month in the dataset is **November 2017** with **$118,447.82** in revenue (a $52.3\%$ increase month-over-month).
* **Q1 Troughs:** The business experiences recurring sales contraction in **January** and **February**, with the lowest monthly sales recorded in **February 2014** (**$4,519.89**).
* **Growth Trajectory:** Annual sales dipped slightly in 2015 ($470k) but surged in 2016 ($609k) and 2017 ($733k), showing robust long-term demand.

---

## 💸 Profit Insights (Phase 5)
* **Champion Segments:** The Consumer segment is the largest driver of net profit ($134k), though the Corporate segment exhibits a similar profit margin of approximately $17\%$.
* **Profit Margin Winners:** 
  * **Labels:** $44.42\%$ profit margin
  * **Paper:** $43.39\%$ profit margin
  * **Envelopes:** $42.27\%$ profit margin
* **Profit Margin Leaks:**
  * **Tables:** -$17,725.48 net profit (Margin: **-8.56%**)
  * **Bookcases:** -$3,472.56 net profit (Margin: **-3.02%**)
  * **Supplies:** -$1,189.10 net profit (Margin: **-2.55%**)

---

## 📦 Product Insights (Phase 6)
* **High-Value Champions:** The **Canon imageCLASS 2200 Advanced Copier** is the single most valuable product, generating **$61,599.82** in revenue and **$25,199.93** in net profit (a $40.9\%$ margin).
* **Deceptive Performers:** The **Cisco TelePresence System EX90** generated **$22,638.48** in revenue (ranking 3rd overall) but resulted in a net loss of **-$1,811.08** due to excessive discounting.
* **Volume Drivers:** Staples and Envelopes dominate transaction volumes (staples alone accounted for over $330$ units sold), yielding high-margin, low-risk cash flows.

---

## 🗺️ Regional Insights (Phase 7)
* **West Coast Dominance:** The West Region is the most profitable market, generating **$108,418.45** in profit (Margin: $14.94\%$), followed closely by the East Region (**$91,522.78**).
* **Central Region Vulnerability:** The Central region has the lowest profit margin (**$7.92\%$**), driven by high discounts and logistics overheads.
* **State Performance Divergence:**
  * **Top Performers:** California (**$76,381.39** net profit) and New York (**$74,038.55** net profit) are the core profit engines.
  * **Bottom Performers:** **Texas** (-$25,729.36 net loss) and **Ohio** (-$16,971.38 net loss) are the most unprofitable states despite ranking in the top 10 for sales volume.

---

## 💡 Recommendations
1. **Re-price or Phase Out Tables:** The Tables sub-category has negative margins across all segments. Synent recommends renegotiating supplier costs, adjusting retail pricing, or phasing out low-margin table models.
2. **Review Discounting Policies in Texas/Ohio:** The high losses in Texas and Ohio are directly correlated with excessive retail discounts. Implement strict discount caps (maximum $15\%$) in these states to restore profitability.
3. **Double-Down on High-Margin Categories:** Shift marketing capital and inventory allocations toward Office Supplies (specifically Paper and Envelopes) and Technology (Copiers and Phones) to leverage their high profit margins.
4. **Leverage Q4 Seasonality:** Allocate advertising spend in Q3 to maximize checkout conversions during the high-demand months of November and December.
