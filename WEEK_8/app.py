
import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Supply Chain Analytics",
    page_icon=" ",
    layout="wide"
)


# ---------------- PROFESSIONAL STYLE ----------------
st.markdown("""
<style>
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1500px;
    }

    [data-testid="stSidebar"] {
        background-color: #F4F6F9;
        border-right: 1px solid #E2E7EF;
    }

    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2 {
        color: #142D4E;
        font-size: 1.15rem;
    }

    h1 {
        color: #142D4E !important;
        font-weight: 700 !important;
        letter-spacing: -0.7px;
    }

    h2, h3 {
        color: #203B5C !important;
        font-weight: 650 !important;
    }

    [data-testid="stMetric"] {
        background: #FFFFFF;
        border: 1px solid #DCE3EC;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 2px 6px rgba(20,45,78,0.04);
    }

    [data-testid="stMetricLabel"] {
        color: #64748B !important;
        font-size: 14px !important;
    }

    [data-testid="stMetricValue"] {
        color: #142D4E !important;
        font-size: 27px !important;
        font-weight: 700 !important;
    }

    [data-testid="stTabs"] button {
        font-weight: 600;
    }

    [data-testid="stDataFrame"] {
        border: 1px solid #E2E8F0;
        border-radius: 8px;
    }

    hr {
        border-color: #E2E8F0;
    }
</style>
""", unsafe_allow_html=True)

# Consistent chart defaults
px.defaults.template = "plotly_white"
px.defaults.color_discrete_sequence = [
    "#24476B",
    "#4C78A8",
    "#72A0C1",
    "#A5BBD0",
    "#D49A56",
    "#789B8A"
]


# ---------------- LOAD DATA ----------------
@st.cache_data
def load_data():
    df = pd.read_csv(
        "data/Cleaned_Dataset.csv",
        encoding="latin1"
    )

    df["order date (DateOrders)"] = pd.to_datetime(
        df["order date (DateOrders)"],
        format="mixed",
        errors="coerce"
    )

    numeric_cols = [
        "Sales", "Order Item Quantity",
        "Days for shipping (real)",
        "Days for shipment (scheduled)",
        "Order Profit Per Order",
        "Benefit per order"
    ]

    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    return df

df = load_data()

# ---------------- CHART FORMATTING ----------------

def style_chart(fig):
    fig.update_layout(
        font=dict(
            family="Arial, sans-serif",
            size=12,
            color="#334155"
        ),

        title=dict(
            font=dict(size=17, color="#142D4E"),
            x=0.02,
            xanchor="left",
            y=0.98,
            yanchor="top"
        ),

        plot_bgcolor="#FFFFFF",
        paper_bgcolor="#FFFFFF",

        # Reserve space for title and legend
        margin=dict(
            l=55,
            r=35,
            t=100,
            b=110
        ),

        # Move legend below the chart
        legend=dict(
            orientation="h",
            yanchor="top",
            y=-0.25,
            xanchor="left",
            x=0,
            font=dict(size=10)
        ),

        height=430
    )

    fig.update_xaxes(
        showgrid=False,
        linecolor="#DCE3EC",
        automargin=True
    )

    fig.update_yaxes(
        gridcolor="#EDF1F5",
        zeroline=False,
        automargin=True
    )

    return fig


# ---------------- DASHBOARD HEADER ----------------
st.title("Supply Chain Performance Analytics")

st.markdown(
    "Operational and commercial performance across "
    "sales, customers, markets and logistics."
)

st.caption(
    "DATA SOURCE: DataCo Supply Chain Dataset  |  "
    "ANALYSIS: Exploratory Data Analysis and Business Intelligence"
)
st.divider()

# ---------------- SIDEBAR FILTERS ----------------
st.sidebar.title("Dashboard Filters")


    

def add_filter(label, column):
    values = sorted(df[column].dropna().unique().tolist())

    return st.sidebar.multiselect(
        label,
        options=values,
        default=[],
        placeholder="Select one or more...",
        key=f"filter_{column}"
    )


markets = add_filter("Select Market", "Market")
regions = add_filter("Select Region", "Order Region")
categories = add_filter("Select Category", "Category Name")
shipping = add_filter("Shipping Mode", "Shipping Mode")
segments = add_filter("Customer Segment", "Customer Segment")

min_date = df["order date (DateOrders)"].min().date()
max_date = df["order date (DateOrders)"].max().date()

date_range = st.sidebar.date_input(
    "Order Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)



# ---------------- APPLY FILTERS ----------------
filtered = df.copy()

filter_mapping = {
    "Market": markets,
    "Order Region": regions,
    "Category Name": categories,
    "Shipping Mode": shipping,
    "Customer Segment": segments
}

for column, selected in filter_mapping.items():
    if selected:
        filtered = filtered[
            filtered[column].isin(selected)
        ]



# ---------------- KPI SECTION ----------------
total_sales = filtered["Sales"].sum()
total_orders = filtered["Order Id"].nunique()
total_customers = filtered["Customer Id"].nunique()

avg_order_value = (
    total_sales / total_orders if total_orders else 0
)

late_percentage = (
    filtered["Late_delivery_risk"].mean() * 100
)

st.subheader("Business Overview")

# First row
c1, c2, c3 = st.columns(3)

c1.metric(
    "💰 Total Sales",
    f"${total_sales / 1_000_000:.2f}M"
)

c2.metric(
    "📦 Total Orders",
    f"{total_orders:,}"
)

c3.metric(
    "👥 Total Customers",
    f"{total_customers:,}"
)

# Second row
c4, c5 = st.columns(2)

c4.metric(
    "🛒 Average Order Value",
    f"${avg_order_value:,.2f}"
)

c5.metric(
    "🚚 Late Delivery Risk",
    f"{late_percentage:.1f}%"
)

st.divider()

# ---------------- TABS ----------------
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Overview",
    "💰 Sales Analysis",
    "🚚 Shipping Analysis",
    "👥 Customer Analysis",
    "📁 Data Explorer"
])

# ---------------- OVERVIEW ----------------
with tab1:
    st.subheader("Sales Performance")

    col1, col2 = st.columns(2)

    with col1:
        monthly = (
            filtered.dropna(subset=["order date (DateOrders)"])
            .assign(Month=lambda x: x["order date (DateOrders)"].dt.to_period("M").astype(str))
            .groupby("Month", as_index=False)["Sales"].sum()
        )

        fig = px.line(
            monthly,
            x="Month",
            y="Sales",
            markers=True,
            title="Monthly Sales Trend"
        )
        st.plotly_chart(
           style_chart(fig),
           use_container_width=True,
        )

    with col2:
        region_sales = (
            filtered.groupby("Order Region", as_index=False)["Sales"]
            .sum()
            .sort_values("Sales", ascending=False)
        )

        fig = px.bar(
            region_sales,
            x="Order Region",
            y="Sales",
            color="Sales",
            title="Sales by Region"
        )
        st.plotly_chart(
            style_chart(fig),
            use_container_width=True,
        )

    col3, col4 = st.columns(2)

    with col3:
        category_sales = (
            filtered.groupby("Category Name", as_index=False)["Sales"]
            .sum()
            .nlargest(10, "Sales")
        )

        fig = px.bar(
            category_sales,
            x="Sales",
            y="Category Name",
            orientation="h",
            title="Top 10 Product Categories"
        )
        st.plotly_chart(
             style_chart(fig),
             use_container_width=True,
        )

    with col4:
        fig = px.pie(
            filtered,
            names="Shipping Mode",
            values="Order Item Quantity",
            title="Shipping Mode Distribution"
        )
        st.plotly_chart(
            style_chart(fig),
            use_container_width=True,
        )

# ---------------- SALES ANALYSIS ----------------
with tab2:
    st.subheader("Sales and Product Insights")

    col1, col2 = st.columns(2)

    with col1:
        market_sales = (
            filtered.groupby("Market", as_index=False)["Sales"]
            .sum()
        )

        fig = px.bar(
            market_sales,
            x="Market",
            y="Sales",
            color="Market",
            title="Market-wise Sales"
        )
        st.plotly_chart(
            style_chart(fig),
            use_container_width=True,
        )

    with col2:
        fig = px.scatter(
            filtered.sample(min(3000, len(filtered)), random_state=42),
            x="Order Item Quantity",
            y="Sales",
            color="Market",
            opacity=0.55,
            title="Quantity vs Sales by Market"
        )
        st.plotly_chart(
            style_chart(fig),
            use_container_width=True,
        )

    st.subheader("Product Category Performance")

    st.dataframe(
        filtered.groupby("Category Name", as_index=False)
        .agg(
            Total_Sales=("Sales", "sum"),
            Total_Quantity=("Order Item Quantity", "sum"),
            Orders=("Order Id", "nunique")
        )
        .sort_values("Total_Sales", ascending=False),
        use_container_width=True
    )

# ---------------- SHIPPING ANALYSIS ----------------
with tab3:
    st.subheader("Delivery and Logistics Performance")

    col1, col2 = st.columns(2)

    with col1:
        ship_data = (
            filtered.groupby("Shipping Mode", as_index=False)
            ["Days for shipping (real)"].mean()
        )

        
    shipping_avg = (
        filtered.groupby("Shipping Mode")["Days for shipping (real)"]
        .mean()
        .reset_index()
    )

    shipping_avg.columns = [
        "Shipping Mode",
        "Average Shipping Days"
    ]

    fig = px.bar(
        shipping_avg.sort_values("Average Shipping Days"),
        x="Average Shipping Days",
        y="Shipping Mode",
        orientation="h",
        text="Average Shipping Days",
        title="Average Actual Shipping Days by Mode",
        color_discrete_sequence=["#426B91"]
    )

    fig.update_traces(
        texttemplate="%{text:.2f} days",
        textposition="outside",
        showlegend=False
    )

    fig.update_layout(
        showlegend=False,
        height=370,
        margin=dict(l=20, r=65, t=65, b=45)
    )

    fig.update_xaxes(title="Average Shipping Days", showgrid=True)
    fig.update_yaxes(title="", showgrid=False)

    st.plotly_chart(fig, use_container_width=True)


    with col2:
        status_data = (
            filtered["Delivery Status"]
            .value_counts()
            .reset_index()
        )
        status_data.columns = ["Delivery Status", "Count"]

        fig = px.pie(
            status_data,
            names="Delivery Status",
            values="Count",
            hole=0.4,
            title="Delivery Status Distribution"
        )
        
    # Delivery chart layout
    fig.update_traces(
         hole=0.48,
         textposition="inside",
         textinfo="percent",
         textfont=dict(size=13, color="white"),
        domain=dict(x=[0.15, 0.85], y=[0.12, 0.88])
    )

    fig.update_layout(
         title=dict(
             text="Delivery Status Distribution",
             x=0.5,
             xanchor="center"
         ),
         height=450,
         autosize=True,
         margin=dict(l=35, r=35, t=75, b=100),
         showlegend=True,
         legend=dict(
             orientation="h",
             x=0.5,
             xanchor="center",
             y=-0.08,
             yanchor="top",
             font=dict(size=11)
         )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    
    

    st.subheader("Actual vs Scheduled Shipping Time")

    shipping_comparison = filtered.groupby(
        "Shipping Mode", as_index=False
    ).agg(
        Actual_Days=("Days for shipping (real)", "mean"),
        Scheduled_Days=("Days for shipment (scheduled)", "mean")
    )

    shipping_comparison = shipping_comparison.melt(
        id_vars="Shipping Mode",
        var_name="Shipping Type",
        value_name="Days"
    )

    fig = px.bar(
        shipping_comparison,
        x="Shipping Mode",
        y="Days",
        color="Shipping Type",
        barmode="group",
        title="Actual vs Scheduled Delivery"
    )
    st.plotly_chart(
        style_chart(fig),
        use_container_width=True,
    )

# ---------------- CUSTOMER ANALYSIS ----------------
with tab4:
    st.subheader("Customer Insights")

    col1, col2 = st.columns(2)

    with col1:
        segment_data = (
            filtered.groupby("Customer Segment", as_index=False)
            .agg(Sales=("Sales", "sum"))
        )

        fig = px.pie(
            segment_data,
            names="Customer Segment",
            values="Sales",
            title="Sales by Customer Segment"
        )
        st.plotly_chart(
            style_chart(fig),
            use_container_width=True,
        )

    with col2:
        customer_orders = (
            filtered.groupby("Customer Id", as_index=False)
            .agg(Orders=("Order Id", "nunique"))
            .sort_values("Orders", ascending=False)
            .head(10)
        )

        fig = px.bar(
            customer_orders,
            x="Customer Id",
            y="Orders",
            title="Top 10 Customers by Order Count"
        )
        st.plotly_chart(
            style_chart(fig),
            use_container_width=True,
        )

# ---------------- DATA EXPLORER ----------------
with tab5:
    st.subheader("Filtered Dataset Explorer")

    st.write(f"Showing {len(filtered):,} records")

    safe_columns = [
        "Order Id", "Order Date" if False else "order date (DateOrders)",
        "Market", "Order Region", "Category Name",
        "Product Name", "Sales", "Order Item Quantity",
        "Shipping Mode", "Delivery Status",
        "Customer Segment"
    ]

    st.dataframe(
        filtered[safe_columns].head(500),
        use_container_width=True,
        hide_index=True
    )

    csv = filtered[safe_columns].to_csv(index=False).encode("utf-8")

    st.download_button(
        "⬇️ Download Filtered Data",
        data=csv,
        file_name="filtered_supply_chain_data.csv",
        mime="text/csv"
    )

# ---------------- FOOTER ----------------
st.divider()
st.caption(
    "Supply Chain Analytics Dashboard | Built using Python, "
    "Pandas, Streamlit and Plotly"
)
