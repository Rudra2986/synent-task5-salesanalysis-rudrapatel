"""
Revenue Analysis Module
Synent Technologies - Data Science Internship (Summer 2026)
Task 5: Sales Data Analysis

This module performs monthly and annual revenue aggregations, identifies peaks,
troughs, and growth patterns, and generates line charts to visualize revenue trends.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def load_cleaned_data(file_path: str) -> pd.DataFrame:
    """
    Loads the cleaned sales dataset.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Cleaned dataset not found at: {file_path}")
    df = pd.read_csv(file_path)
    # Parse dates back to datetime
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df['Ship Date'] = pd.to_datetime(df['Ship Date'])
    return df


def calculate_monthly_revenue(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregates sales by Year and Month.
    """
    # Create Year-Month column for sorting and grouping
    df_temp = df.copy()
    df_temp['YearMonth'] = df_temp['Order Date'].dt.to_period('M')
    
    monthly_sales = df_temp.groupby('YearMonth')['Sales'].sum().reset_index()
    monthly_sales['YearMonth_Str'] = monthly_sales['YearMonth'].astype(str)
    
    # Calculate month-over-month growth rate
    monthly_sales['MoM_Growth_%'] = monthly_sales['Sales'].pct_change() * 100
    
    return monthly_sales


def plot_revenue_trends(monthly_sales: pd.DataFrame, output_dir: str):
    """
    Plots the monthly revenue trend and saves it as an image.
    """
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "revenue_trends.png")
    
    plt.figure(figsize=(15, 6))
    
    # Line plot for Sales
    ax = sns.lineplot(
        data=monthly_sales, 
        x='YearMonth_Str', 
        y='Sales', 
        marker='o', 
        linewidth=2.5, 
        color='#1E3A8A'
    )
    
    # Customizing axes and labels
    plt.title('Monthly Sales Revenue Trends (Superstore)', fontsize=16, fontweight='bold', pad=15)
    plt.xlabel('Order Period (Year-Month)', fontsize=12)
    plt.ylabel('Total Sales ($)', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    
    # Add values on top of points (every 3 months to avoid cluttering)
    for idx, row in monthly_sales.iterrows():
        if idx % 2 == 0:
            ax.text(
                idx, 
                row['Sales'] + 5000, 
                f"${row['Sales']/1000:.1f}k", 
                ha='center', 
                va='bottom', 
                fontsize=9, 
                color='#1F2937'
            )
            
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"  [Action] Saved monthly revenue trend chart to: {output_path}")


def display_revenue_insights(monthly_sales: pd.DataFrame):
    """
    Extracts and prints key business insights regarding revenue.
    """
    print("\n" + "=" * 60)
    print("PHASE 4: MONTHLY REVENUE ANALYSIS INSIGHTS")
    print("=" * 60)
    
    # Top 3 highest revenue periods
    highest = monthly_sales.sort_values(by='Sales', ascending=False).head(3)
    # Bottom 3 lowest revenue periods
    lowest = monthly_sales.sort_values(by='Sales', ascending=True).head(3)
    
    # General annual metrics
    monthly_sales['Year'] = monthly_sales['YearMonth'].dt.year
    annual_sales = monthly_sales.groupby('Year')['Sales'].sum().reset_index()
    
    print("Top 3 Highest Revenue Months:")
    for _, row in highest.iterrows():
        print(f"  - {row['YearMonth_Str']}: ${row['Sales']:,.2f} (MoM Growth: {row['MoM_Growth_%']:.2f}%)")
        
    print("\nTop 3 Lowest Revenue Months:")
    for _, row in lowest.iterrows():
        print(f"  - {row['YearMonth_Str']}: ${row['Sales']:,.2f} (MoM Growth: {row['MoM_Growth_%']:.2f}%)")
        
    print("\nAnnual Revenue Performance:")
    for _, row in annual_sales.iterrows():
        print(f"  - Year {int(row['Year'])}: ${row['Sales']:,.2f}")
        
    print("=" * 60 + "\n")


def main():
    cleaned_path = "c:/COLLEGE/Synent-Internship-2026/Task-5-Sales-Analysis/data/processed/cleaned_superstore.csv"
    output_dir = "c:/COLLEGE/Synent-Internship-2026/Task-5-Sales-Analysis/images"
    
    try:
        df = load_cleaned_data(cleaned_path)
        monthly_sales = calculate_monthly_revenue(df)
        plot_revenue_trends(monthly_sales, output_dir)
        display_revenue_insights(monthly_sales)
    except Exception as e:
        print(f"Error in revenue analysis: {e}")


if __name__ == "__main__":
    main()
