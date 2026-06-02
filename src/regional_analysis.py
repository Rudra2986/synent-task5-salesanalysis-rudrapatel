"""
Regional Analysis Module
Synent Technologies - Data Science Internship (Summer 2026)
Task 5: Sales Data Analysis

This module performs regional and state-level performance analysis, identifies
geographical opportunities and low-margin states, and generates visualizations
saved to images/regional_performance.png.
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


def calculate_regional_metrics(df: pd.DataFrame) -> dict:
    """
    Computes performance metrics grouped by Region and State.
    """
    # 1. State-level performance
    state_perf = df.groupby('State')[['Sales', 'Profit']].sum().reset_index()
    state_perf['Margin_%'] = (state_perf['Profit'] / state_perf['Sales']) * 100
    
    top_states_sales = state_perf.sort_values(by='Sales', ascending=False).head(10)
    bottom_states_profit = state_perf.sort_values(by='Profit', ascending=True).head(5)
    
    return {
        "StatePerf": state_perf,
        "TopStatesSales": top_states_sales,
        "BottomStatesProfit": bottom_states_profit
    }


def plot_regional_analysis(metrics: dict, df: pd.DataFrame, output_dir: str):
    """
    Generates comparison charts and saves them to images/regional_performance.png.
    """
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "regional_performance.png")
    
    fig, axes = plt.subplots(2, 1, figsize=(15, 12))
    sns.set_theme(style="whitegrid")
    
    # Plot 1: Top 10 States by Sales Revenue
    sns.barplot(
        data=metrics['TopStatesSales'], 
        x='Sales', 
        y='State', 
        ax=axes[0], 
        palette='Blues_r',
        hue='State',
        legend=False
    )
    axes[0].set_title('Top 10 States by Sales Revenue ($)', fontsize=14, fontweight='bold')
    axes[0].set_xlabel('Total Sales ($)')
    axes[0].set_ylabel('State')
    
    # Plot 2: Profitability Margin of Top 10 States
    sns.barplot(
        data=metrics['TopStatesSales'].sort_values('Margin_%', ascending=False), 
        x='Margin_%', 
        y='State', 
        ax=axes[1], 
        palette='Greens_r',
        hue='State',
        legend=False
    )
    axes[1].set_title('Profit Margin (%) of Top 10 Sales-Generating States', fontsize=14, fontweight='bold')
    axes[1].set_xlabel('Profit Margin (%)')
    axes[1].set_ylabel('State')
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"  [Action] Saved regional analysis chart to: {output_path}")


def display_regional_insights(metrics: dict):
    """
    Extracts and prints key regional insights.
    """
    print("\n" + "=" * 60)
    print("PHASE 7: REGIONAL & STATE-LEVEL PERFORMANCE INSIGHTS")
    print("=" * 60)
    
    print("Top 5 Sales Generating States:")
    for _, row in metrics['TopStatesSales'].head(5).iterrows():
        print(f"  - {row['State']}: Sales = ${row['Sales']:,.2f} | Profit = ${row['Profit']:,.2f} | Margin = {row['Margin_%']:.2f}%")
        
    print("\nTop 5 Least Profitable States (Highest Net Losses):")
    for _, row in metrics['BottomStatesProfit'].iterrows():
        print(f"  - {row['State']}: Profit/Loss = ${row['Profit']:,.2f} | Sales = ${row['Sales']:,.2f} | Margin = {row['Margin_%']:.2f}%")
        
    print("=" * 60 + "\n")


def main():
    cleaned_path = "c:/COLLEGE/Synent-Internship-2026/Task-5-Sales-Analysis/data/processed/cleaned_superstore.csv"
    output_dir = "c:/COLLEGE/Synent-Internship-2026/Task-5-Sales-Analysis/images"
    
    try:
        df = load_cleaned_data(cleaned_path)
        metrics = calculate_regional_metrics(df)
        plot_regional_analysis(metrics, df, output_dir)
        display_regional_insights(metrics)
    except Exception as e:
        print(f"Error in regional analysis: {e}")


if __name__ == "__main__":
    main()
