"""
Sales Analysis Dashboard (Streamlit App)
Synent Technologies - Data Science Internship (Summer 2026)
Task 5: Sales Data Analysis

This application provides an interactive web-based dashboard for exploring sales trends,
product profitability, and regional distributions.
"""

import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration
st.set_page_config(
    page_title="Superstore Sales Analysis Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Styling Helpers (Custom CSS for Premium Look)
st.markdown("""
    <style>
    .main-title {
        font-size: 40px;
        font-weight: bold;
        color: #1E3A8A;
        text-align: center;
        margin-bottom: 5px;
    }
    .sub-title {
        font-size: 18px;
        color: #4B5563;
        text-align: center;
        margin-bottom: 30px;
    }
    .metric-card {
        background-color: #F3F4F6;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    </style>
""", unsafe_allow_html=True)


# 3. Main Dashboard Construction
def main():
    st.markdown('<p class="main-title">Superstore Sales Performance Dashboard</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Interactive EDA and Business Profitability Analysis</p>', unsafe_allow_html=True)

    # Sidebar Filter Controls
    st.sidebar.header("Dashboard Controls & Filters")
    uploaded_file = st.sidebar.file_uploader("Upload Cleaned Sales CSV", type=["csv"])

    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.sidebar.success("Dataset loaded successfully!")
            
            # Displays columns to confirm structure
            st.write("### Data Preview", df.head())
            
            # TODO: Add filters for Segment, Region, Category based on dataset columns
            # TODO: Display Metric Cards (Total Sales, Total Profit, Average Profit Margin)
            # TODO: Generate Plotly charts for monthly trends, categories, and regional performance
            
        except Exception as e:
            st.error(f"Error loading dataset: {e}")
    else:
        st.warning("Please upload a cleaned CSV dataset from the sidebar to activate the interactive dashboard.")
        
        # Display structural placeholders for UI presentation
        st.info("Once a dataset is provided, this dashboard will feature dynamic charts for:")
        st.markdown("""
        - **Monthly Revenue & Profit Trends** (Plotly Line Charts)
        - **Top Product Performance** (Bar Charts)
        - **Regional Heatmaps** (Geographic Scatter Plots)
        - **Discount vs. Profitability Margins** (Scatter plots with trendlines)
        """)


if __name__ == "__main__":
    main()
