"""
Product Analysis Starter Module
Synent Technologies - Data Science Internship (Summer 2026)
Task 5: Sales Data Analysis

This module handles identification of top-selling products, category analysis, and performance metrics.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def identify_top_selling_products(df: pd.DataFrame, product_id_col: str, sales_col: str, top_n: int = 10) -> pd.DataFrame:
    """
    Identifies the top N products by total sales.
    
    Args:
        df (pd.DataFrame): The sales dataset.
        product_id_col (str): Column identifying the product name/ID.
        sales_col (str): Column containing sales numbers.
        top_n (int): Number of top products to return.
        
    Returns:
        pd.DataFrame: Top products ranked by total sales.
    """
    print(f"Identifying top {top_n} products...")
    # TODO: Group by product_id_col, sum sales_col, sort descending, and return top_n
    return pd.DataFrame()


def analyze_category_performance(df: pd.DataFrame, category_col: str, subcategory_col: str, sales_col: str, profit_col: str) -> pd.DataFrame:
    """
    Aggregates sales and profits at category and subcategory levels.
    """
    print("Analyzing performance by category...")
    # TODO: Group by category and subcategory columns
    return pd.DataFrame()


def plot_category_sales(category_df: pd.DataFrame, output_image_path: str):
    """
    Plots a comparison bar chart of category sales and profitability.
    """
    print("Generating category sales comparison plot...")
    # TODO: Implement plotting logic
    pass


if __name__ == "__main__":
    print("Running Product Analysis starter script.")
