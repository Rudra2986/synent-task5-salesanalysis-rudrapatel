"""
Sales Analysis Interactive Dashboard (Streamlit App)
Synent Technologies - Data Science Internship (Summer 2026)
Task 5: Sales Data Analysis

This application provides a premium, interactive web dashboard to explore sales performance,
revenue seasonality, profitability margins, product ranks, and regional analysis.
"""

import os
import pandas as pd
import streamlit as st
import plotly.express as px

# 1. Page Configuration
st.set_page_config(
    page_title="Superstore Sales Analytics Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Load cleaned data helper
@st.cache_data
def load_data():
    # Robust path resolution relative to script file (src/app.py -> project root)
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, "data", "processed", "cleaned_superstore.csv")
    
    if not os.path.exists(file_path):
        # Fallback to absolute workspace path if needed
        file_path = "c:/COLLEGE/Synent-Internship-2026/Task-5-Sales-Analysis/data/processed/cleaned_superstore.csv"
        
    if not os.path.exists(file_path):
        return None
        
    df = pd.read_csv(file_path)
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df['Ship Date'] = pd.to_datetime(df['Ship Date'])
    return df


# 3. Main Dashboard Construction
def main():
    # Load dataset
    df = load_data()
    
    if df is None:
        st.error("Error: Cleaned dataset not found. Please execute the data cleaning pipeline first by running: `python src/data_cleaning.py`")
        return

    # Header section
    st.markdown("""
        <div style="background-color:#1E3A8A;padding:20px;border-radius:10px;margin-bottom:20px">
            <h1 style="color:white;text-align:center;margin:0">Superstore Sales Performance Dashboard</h1>
            <p style="color:#D1D5DB;text-align:center;margin:5px 0 0 0;font-size:16px">Synent Technologies Data Science Internship - Task 5</p>
        </div>
    """, unsafe_allow_html=True)

    # Sidebar Filters
    st.sidebar.header("📊 Filter Controls")
    
    # 1. Segment filter
    segments = ['All'] + list(df['Segment'].unique())
    selected_segment = st.sidebar.selectbox("Select Customer Segment", segments)
    
    # 2. Region filter
    regions = ['All'] + list(df['Region'].unique())
    selected_region = st.sidebar.selectbox("Select Geographic Region", regions)
    
    # 3. Category filter
    categories = ['All'] + list(df['Category'].unique())
    selected_category = st.sidebar.selectbox("Select Product Category", categories)

    # Apply filters
    filtered_df = df.copy()
    if selected_segment != 'All':
        filtered_df = filtered_df[filtered_df['Segment'] == selected_segment]
    if selected_region != 'All':
        filtered_df = filtered_df[filtered_df['Region'] == selected_region]
    if selected_category != 'All':
        filtered_df = filtered_df[filtered_df['Category'] == selected_category]

    # Metric Row
    total_sales = filtered_df['Sales'].sum()
    total_profit = filtered_df['Profit'].sum()
    overall_margin = (total_profit / total_sales * 100) if total_sales > 0 else 0
    total_orders = filtered_df['Order ID'].nunique()

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="💰 Total Sales Revenue", value=f"${total_sales:,.2f}")
    with col2:
        st.metric(
            label="📈 Net Business Profit", 
            value=f"${total_profit:,.2f}",
            delta=f"{overall_margin:.2f}% Margin",
            delta_color="normal" if total_profit >= 0 else "inverse"
        )
    with col3:
        st.metric(label="🛍️ Total Orders Placed", value=f"{total_orders:,}")
    with col4:
        avg_order = (total_sales / total_orders) if total_orders > 0 else 0
        st.metric(label="🏷️ Average Order Value", value=f"${avg_order:,.2f}")

    st.markdown("---")

    # Tabs for different analyses
    tab1, tab2, tab3, tab4 = st.tabs([
        "📅 Monthly Revenue Trends", 
        "💸 Sub-Category Profitability", 
        "📦 Product Performance", 
        "🗺️ Regional Performance"
    ])

    # TAB 1: Monthly Revenue Trends
    with tab1:
        st.subheader("Monthly Revenue Trajectory")
        # Aggregate by YearMonth
        filtered_df['YearMonth'] = filtered_df['Order Date'].dt.to_period('M')
        monthly_data = filtered_df.groupby('YearMonth')[['Sales', 'Profit']].sum().reset_index()
        monthly_data['Period'] = monthly_data['YearMonth'].astype(str)
        
        fig_revenue = px.line(
            monthly_data, 
            x='Period', 
            y='Sales', 
            title="Sales Revenue MoM Trends",
            labels={"Sales": "Revenue ($)", "Period": "Order Month"},
            markers=True,
            color_discrete_sequence=['#1E3A8A']
        )
        st.plotly_chart(fig_revenue, use_container_width=True)
        
        st.markdown("""
        **Seasonality Summary:** 
        - Notice how revenue exhibits a significant seasonality cycle, spiking during November and December (holiday shopping) and dipping sharply in January and February.
        """)

    # TAB 2: Sub-Category Profitability
    with tab2:
        st.subheader("Profitability Margin Analysis")
        subcat_data = filtered_df.groupby('Sub-Category')[['Sales', 'Profit']].sum().reset_index()
        subcat_data['Margin (%)'] = (subcat_data['Profit'] / subcat_data['Sales']) * 100
        subcat_data = subcat_data.sort_values(by='Margin (%)', ascending=False)
        
        fig_margin = px.bar(
            subcat_data, 
            x='Margin (%)', 
            y='Sub-Category', 
            orientation='h',
            title="Profit Margin (%) by Product Sub-Category",
            color='Profit',
            color_continuous_scale=px.colors.diverging.RdYlGn,
            labels={"Margin (%)": "Profit Margin (%)"}
        )
        st.plotly_chart(fig_margin, use_container_width=True)
        
        st.markdown("""
        **Margin Warning:** 
        - Sub-categories in **red** (like **Tables** and **Bookcases**) have negative profit margins, indicating severe profitability leakage.
        """)

    # TAB 3: Product Performance
    with tab3:
        st.subheader("Top Revenue & Sales Generating Products")
        top_n = st.slider("Select number of top products to display", min_value=5, max_value=20, value=10)
        
        top_products = filtered_df.groupby('Product Name')[['Sales', 'Profit']].sum().reset_index()
        top_products = top_products.sort_values(by='Sales', ascending=False).head(top_n)
        
        fig_products = px.bar(
            top_products, 
            x='Sales', 
            y='Product Name', 
            orientation='h',
            title=f"Top {top_n} Products by Revenue",
            color='Profit',
            color_continuous_scale='Viridis',
            labels={"Sales": "Total Sales ($)"}
        )
        # Invert y-axis to show top product on top
        fig_products.update_layout(yaxis={'categoryorder': 'total ascending'})
        st.plotly_chart(fig_products, use_container_width=True)

    # TAB 4: Regional Performance
    with tab4:
        st.subheader("Geographical Distribution")
        state_data = filtered_df.groupby('State')[['Sales', 'Profit']].sum().reset_index()
        state_data['Margin (%)'] = (state_data['Profit'] / state_data['Sales']) * 100
        state_data = state_data.sort_values(by='Sales', ascending=False).head(15)
        
        fig_states = px.bar(
            state_data, 
            x='State', 
            y='Sales', 
            color='Profit',
            title="Top 15 States by Sales Revenue and Net Profit",
            color_continuous_scale=px.colors.sequential.Plotly3,
            labels={"Sales": "Total Sales ($)"}
        )
        st.plotly_chart(fig_states, use_container_width=True)
        
        st.markdown("""
        **Regional Insights:**
        - California and New York are our key profit drivers. 
        - Notice that **Texas** and **Pennsylvania** generate high sales but exhibit negative net profit (losses), highlighting major local discount leaks.
        """)


if __name__ == "__main__":
    main()
Untracked_Placeholder = """
Run this dashboard locally:
`streamlit run src/app.py`
"""
