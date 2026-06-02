"""
Revenue Analysis Starter Module
Synent Technologies - Data Science Internship (Summer 2026)
Task 5: Sales Data Analysis

This module performs revenue-related computations and trend visualizations.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def load_cleaned_data(file_path: str) -> pd.DataFrame:
    """
    Loads the cleaned sales dataset from the processed directory.
    """
    print(f"Loading data from: {file_path}")
    # TODO: Implement loading logic (e.g. pd.read_csv)
    return pd.DataFrame()


def calculate_monthly_revenue(df: pd.DataFrame, date_column: str, sales_column: str) -> pd.DataFrame:
    """
    Calculates monthly revenue trends.
    
    Args:
        df (pd.DataFrame): The sales dataset.
        date_column (str): The name of the date column.
        sales_column (str): The name of the sales column.
        
    Returns:
        pd.DataFrame: A grouped dataframe containing Year, Month, and Monthly Sales.
    """
    print("Calculating monthly revenue...")
    # TODO: Implement aggregation and grouping logic
    # Expected output: Grouped by Year-Month or Year & Month, sum of Sales
    return pd.DataFrame()


def plot_revenue_trends(monthly_revenue_df: pd.DataFrame, output_image_path: str):
    """
    Plots the monthly revenue trend and saves it as an image.
    
    Args:
        monthly_revenue_df (pd.DataFrame): Dataframe containing monthly sales.
        output_image_path (str): File path to save the generated plot.
    """
    print("Generating revenue trend plot...")
    # TODO: Implement plotting logic using matplotlib/seaborn
    # plt.figure(...)
    # sns.lineplot(...)
    # plt.savefig(output_image_path)
    pass


if __name__ == "__main__":
    # Test script setup
    print("Running Revenue Analysis starter script.")
