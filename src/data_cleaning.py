"""
Data Cleaning & Assessment Module
Synent Technologies - Data Science Internship (Summer 2026)
Task 5: Sales Data Analysis

This module loads the raw Superstore Sales dataset, performs a data assessment,
cleans the data (parsing datetimes, handling data types, validating numerical bounds),
and exports the cleaned dataset for downstream analysis.
"""

import os
import pandas as pd


def assess_dataset(df: pd.DataFrame) -> dict:
    """
    Performs a complete assessment of the dataset and prints summaries.
    
    Args:
        df (pd.DataFrame): Input dataframe.
        
    Returns:
        dict: Assessment metrics.
    """
    print("=" * 60)
    print("PHASE 1: DATASET ASSESSMENT REPORT")
    print("=" * 60)
    
    shape = df.shape
    rows, cols = shape
    print(f"Dataset Shape: {rows} rows, {cols} columns")
    
    # Missing values check
    missing_vals = df.isnull().sum()
    total_missing = missing_vals.sum()
    
    # Duplicates check
    duplicate_count = df.duplicated().sum()
    
    # Data quality summary
    print(f"\nMissing Values Check (Total Nulls: {total_missing}):")
    if total_missing > 0:
        print(missing_vals[missing_vals > 0])
    else:
        print("  - No missing values found in the dataset.")
        
    print(f"\nDuplicate Records Check: {duplicate_count}")
    
    # Numerical validation check
    negative_sales = (df['Sales'] <= 0).sum()
    negative_qty = (df['Quantity'] <= 0).sum()
    print(f"Validation Checks:")
    print(f"  - Rows with Sales <= 0: {negative_sales}")
    print(f"  - Rows with Quantity <= 0: {negative_qty}")
    
    # Data Types Summary
    print("\nColumn Data Types:")
    for col, dtype in df.dtypes.items():
        print(f"  - {col}: {dtype}")
        
    assessment_results = {
        "rows": rows,
        "columns": cols,
        "total_missing": total_missing,
        "duplicate_count": duplicate_count,
        "negative_sales": negative_sales,
        "negative_qty": negative_qty
    }
    print("=" * 60)
    return assessment_results


def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans the raw dataset:
    - Removes duplicates (if any)
    - Parses Order Date and Ship Date to datetime objects
    - Formats Postal Code as a string
    - Drops columns or records that fail numerical validation (if any)
    
    Args:
        df (pd.DataFrame): Raw dataframe.
        
    Returns:
        pd.DataFrame: Cleaned dataframe.
    """
    print("\nPHASE 2: DATA CLEANING PIPELINE")
    print("=" * 60)
    
    # Copy dataframe to avoid modifying the original in-place
    cleaned_df = df.copy()
    
    # 1. Drop duplicates
    initial_rows = len(cleaned_df)
    cleaned_df = cleaned_df.drop_duplicates()
    dropped_dups = initial_rows - len(cleaned_df)
    if dropped_dups > 0:
        print(f"  [Action] Dropped {dropped_dups} duplicate row(s).")
    else:
        print("  - No duplicate records to remove.")
        
    # 2. Parse date columns
    print("  [Action] Converting Date columns to datetime format...")
    cleaned_df['Order Date'] = pd.to_datetime(cleaned_df['Order Date'], format='%m/%d/%Y', errors='coerce')
    cleaned_df['Ship Date'] = pd.to_datetime(cleaned_df['Ship Date'], format='%m/%d/%Y', errors='coerce')
    
    # Check if date conversions caused nulls
    null_order_dates = cleaned_df['Order Date'].isnull().sum()
    null_ship_dates = cleaned_df['Ship Date'].isnull().sum()
    if null_order_dates > 0 or null_ship_dates > 0:
        print(f"  [Warning] Date parsing generated nulls. Order Date nulls: {null_order_dates}, Ship Date nulls: {null_ship_dates}")
        # Dropping unparseable dates if any
        cleaned_df = cleaned_df.dropna(subset=['Order Date', 'Ship Date'])
        
    # 3. Format Postal Code as string (handling leading zeros and converting floats to clean strings)
    print("  [Action] Standardizing 'Postal Code' to string format...")
    # Fill nulls with 0 first, convert to int, then to string
    cleaned_df['Postal Code'] = cleaned_df['Postal Code'].fillna(0).astype(int).astype(str).str.zfill(5)
    
    # 4. Numerical Column Validation
    # Ensure Sales and Quantity are positive. Filter out rows that violate this.
    cleaned_df = cleaned_df[cleaned_df['Sales'] > 0]
    cleaned_df = cleaned_df[cleaned_df['Quantity'] > 0]
    
    print("  - Data cleaning completed successfully.")
    print("=" * 60)
    return cleaned_df


def main():
    # File paths
    raw_path = "c:/COLLEGE/Synent-Internship-2026/Task-5-Sales-Analysis/data/raw/Sample - Superstore.csv"
    processed_dir = "c:/COLLEGE/Synent-Internship-2026/Task-5-Sales-Analysis/data/processed"
    output_path = os.path.join(processed_dir, "cleaned_superstore.csv")
    
    # Ensure processed directory exists
    os.makedirs(processed_dir, exist_ok=True)
    
    if not os.path.exists(raw_path):
        print(f"Error: Raw dataset file not found at {raw_path}")
        return
        
    # Load raw dataset (Latin-1 is common for Superstore sales to avoid encoding issues)
    try:
        raw_df = pd.read_csv(raw_path, encoding="latin-1")
    except Exception as e:
        print(f"Error loading raw dataset: {e}")
        return
        
    # Phase 1: Assessment
    assess_dataset(raw_df)
    
    # Phase 2: Cleaning
    cleaned_df = clean_dataset(raw_df)
    
    # Export cleaned dataset
    cleaned_df.to_csv(output_path, index=False)
    print(f"SUCCESS: Cleaned dataset saved to: {output_path}")
    print(f"Final Cleaned Dataset Shape: {cleaned_df.shape}\n")


if __name__ == "__main__":
    main()
