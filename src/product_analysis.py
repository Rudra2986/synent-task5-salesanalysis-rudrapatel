"""
Product Analysis Module
Synent Technologies - Data Science Internship (Summer 2026)
Task 5: Sales Data Analysis

This module performs product-level analysis, identifies the top-selling products by 
revenue and unit sales, and analyzes the performance of product categories.
It also saves bar charts summarizing product performance.
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


def calculate_product_metrics(df: pd.DataFrame) -> dict:
    """
    Computes top products by sales and volume.
    """
    # 1. Top 10 products by Sales
    top_sales_prod = df.groupby('Product Name')[['Sales', 'Quantity', 'Profit']].sum().reset_index()
    top_sales_prod = top_sales_prod.sort_values(by='Sales', ascending=False).head(10)
    
    # 2. Top 10 products by Quantity (Volume)
    top_qty_prod = df.groupby('Product Name')[['Sales', 'Quantity', 'Profit']].sum().reset_index()
    top_qty_prod = top_qty_prod.sort_values(by='Quantity', ascending=False).head(10)
    
    # 3. Category Sales Share
    category_summary = df.groupby('Category')[['Sales', 'Profit']].sum().reset_index()
    category_summary['Profit_Margin_%'] = (category_summary['Profit'] / category_summary['Sales']) * 100
    
    return {
        "TopSales": top_sales_prod,
        "TopQty": top_qty_prod,
        "CategorySummary": category_summary
    }


def plot_product_analysis(metrics: dict, output_dir: str):
    """
    Generates product comparison plots and saves to images/product_analysis.png.
    """
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "product_analysis.png")
    
    fig, axes = plt.subplots(1, 2, figsize=(18, 8))
    sns.set_theme(style="whitegrid")
    
    # Plot 1: Top 10 Products by Sales
    sns.barplot(
        data=metrics['TopSales'], 
        x='Sales', 
        y='Product Name', 
        ax=axes[0], 
        palette='Blues_r',
        hue='Product Name',
        legend=False
    )
    axes[0].set_title('Top 10 Products by Sales Revenue ($)', fontsize=14, fontweight='bold')
    axes[0].set_xlabel('Total Sales ($)')
    axes[0].set_ylabel('Product Name')
    
    # Shorten long product names on the y-axis to look clean
    labels = [label.get_text()[:40] + '...' if len(label.get_text()) > 40 else label.get_text() for label in axes[0].get_yticklabels()]
    axes[0].set_yticks(range(len(metrics['TopSales'])))
    axes[0].set_yticklabels(labels)
    
    # Plot 2: Top 10 Products by Quantity Sold
    sns.barplot(
        data=metrics['TopQty'], 
        x='Quantity', 
        y='Product Name', 
        ax=axes[1], 
        palette='Oranges_r',
        hue='Product Name',
        legend=False
    )
    axes[1].set_title('Top 10 Products by Quantity Sold (Units)', fontsize=14, fontweight='bold')
    axes[1].set_xlabel('Total Quantity (Units)')
    axes[1].set_ylabel('')
    
    # Shorten labels for the second plot too
    labels2 = [label.get_text()[:40] + '...' if len(label.get_text()) > 40 else label.get_text() for label in axes[1].get_yticklabels()]
    axes[1].set_yticks(range(len(metrics['TopQty'])))
    axes[1].set_yticklabels(labels2)
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"  [Action] Saved product analysis chart to: {output_path}")


def display_product_insights(metrics: dict):
    """
    Extracts and prints key business insights regarding products.
    """
    print("\n" + "=" * 60)
    print("PHASE 6: PRODUCT PERFORMANCE INSIGHTS")
    print("=" * 60)
    
    print("Top 5 Revenue Generating Products:")
    for idx, row in metrics['TopSales'].head(5).iterrows():
        print(f"  - {row['Product Name'][:50]}... | Sales: ${row['Sales']:,.2f} | Profit: ${row['Profit']:,.2f}")
        
    print("\nTop 5 Unit Selling Products (Volume):")
    for idx, row in metrics['TopQty'].head(5).iterrows():
        print(f"  - {row['Product Name'][:50]}... | Quantity: {row['Quantity']} units | Sales: ${row['Sales']:,.2f}")
        
    print("\nProduct Category Breakdown:")
    for _, row in metrics['CategorySummary'].iterrows():
        print(f"  - {row['Category']}: Sales = ${row['Sales']:,.2f} | Profit = ${row['Profit']:,.2f} | Margin = {row['Profit_Margin_%']:.2f}%")
        
    print("=" * 60 + "\n")


def main():
    cleaned_path = "c:/COLLEGE/Synent-Internship-2026/Task-5-Sales-Analysis/data/processed/cleaned_superstore.csv"
    output_dir = "c:/COLLEGE/Synent-Internship-2026/Task-5-Sales-Analysis/images"
    
    try:
        df = load_cleaned_data(cleaned_path)
        metrics = calculate_product_metrics(df)
        plot_product_analysis(metrics, output_dir)
        display_product_insights(metrics)
    except Exception as e:
        print(f"Error in product analysis: {e}")


if __name__ == "__main__":
    main()
