"""
EDA Distribution Plotting Module
Synent Technologies - Data Science Internship (Summer 2026)
Task 5: Sales Data Analysis

This module performs overall sales and profit distribution visualizations
(e.g., histograms, boxplots, density estimations) and saves them to the images folder.
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


def plot_distributions(df: pd.DataFrame, output_dir: str):
    """
    Generates Sales and Profit distribution visualizations.
    """
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "sales_profit_distributions.png")
    
    # Set up 2x2 subplot layout
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    sns.set_theme(style="whitegrid")
    
    # 1. Sales Distribution (Log Scale due to high skewness)
    sns.histplot(df['Sales'], bins=50, kde=True, ax=axes[0, 0], color='#1E3A8A', log_scale=True)
    axes[0, 0].set_title('Overall Sales Distribution (Log Scale)', fontsize=12, fontweight='bold')
    axes[0, 0].set_xlabel('Sales ($)')
    axes[0, 0].set_ylabel('Frequency')
    
    # 2. Profit Distribution (Filtered to show main concentration)
    # Since profit has extreme outliers (e.g. -6000 and +8000), we zoom in on -200 to +200 to see details
    zoomed_profit = df[(df['Profit'] >= -200) & (df['Profit'] <= 200)]
    sns.histplot(zoomed_profit['Profit'], bins=50, kde=True, ax=axes[0, 1], color='#10B981')
    axes[0, 1].set_title('Profit Distribution (Concentrated Range -$200 to $200)', fontsize=12, fontweight='bold')
    axes[0, 1].set_xlabel('Profit ($)')
    axes[0, 1].set_ylabel('Frequency')
    
    # 3. Sales Boxplot (Log Scale to show outliers)
    sns.boxplot(x=df['Sales'], ax=axes[1, 0], color='#3B82F6')
    axes[1, 0].set_xscale('log')
    axes[1, 0].set_title('Sales Outliers Boxplot (Log Scale)', fontsize=12, fontweight='bold')
    axes[1, 0].set_xlabel('Sales ($)')
    
    # 4. Profit Boxplot
    sns.boxplot(x=df['Profit'], ax=axes[1, 1], color='#34D399')
    axes[1, 1].set_title('Profit Outliers Boxplot', fontsize=12, fontweight='bold')
    axes[1, 1].set_xlabel('Profit ($)')
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"  [Action] Saved Sales and Profit distributions plots to: {output_path}")


def main():
    cleaned_path = "c:/COLLEGE/Synent-Internship-2026/Task-5-Sales-Analysis/data/processed/cleaned_superstore.csv"
    output_dir = "c:/COLLEGE/Synent-Internship-2026/Task-5-Sales-Analysis/images"
    
    try:
        df = load_cleaned_data(cleaned_path)
        plot_distributions(df, output_dir)
    except Exception as e:
        print(f"Error in distribution plotting: {e}")


if __name__ == "__main__":
    main()
