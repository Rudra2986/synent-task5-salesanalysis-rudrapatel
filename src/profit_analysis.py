"""
Profit Analysis Module
Synent Technologies - Data Science Internship (Summer 2026)
Task 5: Sales Data Analysis

This module performs profitability analysis, aggregates profit margins across categories,
regions, segments, and sub-categories, and identifies loss-making hot spots.
It also saves bar charts illustrating profit distributions.
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
    return df


def calculate_profitability_metrics(df: pd.DataFrame) -> dict:
    """
    Aggregates profit metrics by Category, Sub-Category, Region, and Customer Segment.
    """
    # 1. Category Profitability
    cat_profit = df.groupby('Category')[['Sales', 'Profit']].sum().reset_index()
    cat_profit['Margin_%'] = (cat_profit['Profit'] / cat_profit['Sales']) * 100
    
    # 2. Sub-Category Profitability
    subcat_profit = df.groupby('Sub-Category')[['Sales', 'Profit']].sum().reset_index()
    subcat_profit['Margin_%'] = (subcat_profit['Profit'] / subcat_profit['Sales']) * 100
    
    # 3. Regional Profitability
    region_profit = df.groupby('Region')[['Sales', 'Profit']].sum().reset_index()
    region_profit['Margin_%'] = (region_profit['Profit'] / region_profit['Sales']) * 100
    
    # 4. Customer Segment Profitability
    segment_profit = df.groupby('Segment')[['Sales', 'Profit']].sum().reset_index()
    segment_profit['Margin_%'] = (segment_profit['Profit'] / segment_profit['Sales']) * 100
    
    return {
        "Category": cat_profit,
        "Sub-Category": subcat_profit,
        "Region": region_profit,
        "Segment": segment_profit
    }


def plot_profit_analysis(metrics: dict, output_dir: str):
    """
    Generates profitability charts and saves them to images/profitability_analysis.png.
    """
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "profitability_analysis.png")
    
    # Set up 2x2 subplots
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    sns.set_theme(style="whitegrid")
    
    # 1. Profit by Category
    sns.barplot(
        data=metrics['Category'].sort_values('Profit', ascending=False), 
        x='Category', 
        y='Profit', 
        ax=axes[0, 0], 
        palette='Blues_r',
        hue='Category',
        legend=False
    )
    axes[0, 0].set_title('Net Profit by Category', fontsize=12, fontweight='bold')
    axes[0, 0].set_ylabel('Total Profit ($)')
    
    # 2. Profit Margin by Segment
    sns.barplot(
        data=metrics['Segment'].sort_values('Margin_%', ascending=False), 
        x='Segment', 
        y='Margin_%', 
        ax=axes[0, 1], 
        palette='Greens_r',
        hue='Segment',
        legend=False
    )
    axes[0, 1].set_title('Profit Margin (%) by Segment', fontsize=12, fontweight='bold')
    axes[0, 1].set_ylabel('Profit Margin (%)')
    
    # 3. Profit Margin by Sub-Category (Horizontal Bar Chart)
    subcat_sorted = metrics['Sub-Category'].sort_values('Margin_%', ascending=False)
    # Color coding negative margins differently
    colors = ['#EF4444' if x < 0 else '#10B981' for x in subcat_sorted['Margin_%']]
    sns.barplot(
        data=subcat_sorted, 
        y='Sub-Category', 
        x='Margin_%', 
        ax=axes[1, 0], 
        palette=colors,
        hue='Sub-Category',
        legend=False
    )
    axes[1, 0].set_title('Profit Margin (%) by Sub-Category', fontsize=12, fontweight='bold')
    axes[1, 0].set_xlabel('Profit Margin (%)')
    
    # 4. Profit by Region
    sns.barplot(
        data=metrics['Region'].sort_values('Profit', ascending=False), 
        x='Region', 
        y='Profit', 
        ax=axes[1, 1], 
        palette='Purples_r',
        hue='Region',
        legend=False
    )
    axes[1, 1].set_title('Net Profit by Region', fontsize=12, fontweight='bold')
    axes[1, 1].set_ylabel('Total Profit ($)')
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"  [Action] Saved profitability analysis chart to: {output_path}")


def display_profit_insights(metrics: dict, df: pd.DataFrame):
    """
    Extracts and prints key business insights regarding profitability and losses.
    """
    print("\n" + "=" * 60)
    print("PHASE 5: PROFITABILITY ANALYSIS INSIGHTS")
    print("=" * 60)
    
    print("Profit & Margins by Category:")
    for _, row in metrics['Category'].sort_values('Profit', ascending=False).iterrows():
        print(f"  - {row['Category']}: Profit = ${row['Profit']:,.2f} | Margin = {row['Margin_%']:.2f}%")
        
    print("\nTop 3 Profit Margin Sub-Categories:")
    for _, row in metrics['Sub-Category'].sort_values('Margin_%', ascending=False).head(3).iterrows():
        print(f"  - {row['Sub-Category']}: Margin = {row['Margin_%']:.2f}% | Profit = ${row['Profit']:,.2f}")
        
    print("\nLoss-making Sub-Categories:")
    losses = metrics['Sub-Category'][metrics['Sub-Category']['Profit'] < 0]
    if not losses.empty:
        for _, row in losses.sort_values('Profit').iterrows():
            print(f"  - {row['Sub-Category']}: Loss = ${row['Profit']:,.2f} | Margin = {row['Margin_%']:.2f}%")
    else:
        print("  - No loss-making sub-categories found.")
        
    # Analyze regional loss
    print("\nRegional Profit Performance:")
    for _, row in metrics['Region'].sort_values('Profit', ascending=False).iterrows():
        print(f"  - {row['Region']}: Profit = ${row['Profit']:,.2f} | Margin = {row['Margin_%']:.2f}%")
        
    print("=" * 60 + "\n")


def main():
    cleaned_path = "c:/COLLEGE/Synent-Internship-2026/Task-5-Sales-Analysis/data/processed/cleaned_superstore.csv"
    output_dir = "c:/COLLEGE/Synent-Internship-2026/Task-5-Sales-Analysis/images"
    
    try:
        df = load_cleaned_data(cleaned_path)
        metrics = calculate_profitability_metrics(df)
        plot_profit_analysis(metrics, output_dir)
        display_profit_insights(metrics, df)
    except Exception as e:
        print(f"Error in profit analysis: {e}")


if __name__ == "__main__":
    main()
