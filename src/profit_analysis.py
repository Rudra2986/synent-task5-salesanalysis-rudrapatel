"""
Profit Analysis Starter Module
Synent Technologies - Data Science Internship (Summer 2026)
Task 5: Sales Data Analysis

This module performs profitability analysis, margin calculations, and visualizations.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def calculate_profit_margins(df: pd.DataFrame, profit_column: str, sales_column: str) -> pd.DataFrame:
    """
    Computes overall and row-level profit margins.
    
    Args:
        df (pd.DataFrame): The sales dataset.
        profit_column (str): Column name containing profit values.
        sales_column (str): Column name containing sales values.
        
    Returns:
        pd.DataFrame: DataFrame with an added 'Profit_Margin' column.
    """
    print("Calculating profit margins...")
    # TODO: Implement margin computation: (Profit / Sales) * 100
    return df


def analyze_profitability_by_segment(df: pd.DataFrame, segment_column: str, profit_column: str) -> pd.DataFrame:
    """
    Aggregates profit metrics based on customer segments.
    
    Args:
        df (pd.DataFrame): The sales dataset.
        segment_column (str): Column name for customer segments.
        profit_column (str): Column name for profit.
        
    Returns:
        pd.DataFrame: Aggregated table of profits per segment.
    """
    print("Analyzing profit by segment...")
    # TODO: Group by segment_column and compute total/average profit
    return pd.DataFrame()


def plot_profit_distribution(df: pd.DataFrame, segment_column: str, profit_column: str, output_image_path: str):
    """
    Plots profit distribution or margins by segment and saves to file.
    """
    print("Plotting profit distributions...")
    # TODO: Implement plotting logic (e.g. boxplot or barplot)
    pass


if __name__ == "__main__":
    print("Running Profit Analysis starter script.")
