"""
Regional Analysis Starter Module
Synent Technologies - Data Science Internship (Summer 2026)
Task 5: Sales Data Analysis

This module performs geographic sales performance and profit margin analysis.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def calculate_regional_performance(df: pd.DataFrame, region_col: str, sales_col: str, profit_col: str) -> pd.DataFrame:
    """
    Groups sales and profits by region.
    
    Args:
        df (pd.DataFrame): The sales dataset.
        region_col (str): Column name representing the region/state/country.
        sales_col (str): Sales values.
        profit_col (str): Profit values.
        
    Returns:
        pd.DataFrame: Performance metrics aggregated by region.
    """
    print("Calculating regional performance...")
    # TODO: Group by region_col and aggregate sum of sales, profit, and compute overall profit margin
    return pd.DataFrame()


def plot_regional_distribution(regional_df: pd.DataFrame, output_image_path: str):
    """
    Visualizes regional sales and profit contributions.
    """
    print("Generating regional distribution plot...")
    # TODO: Implement plotting logic (e.g. choropleth map or grouped bar chart)
    pass


if __name__ == "__main__":
    print("Running Regional Analysis starter script.")
