import streamlit as st
import pandas as pd
import plotly.express as px

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Smart E-Commerce Dashboard",
    layout="wide"
)

# ================= HEADER =================
st.title("🧠 Smart E-Commerce Dashboard")
st.caption("Business insights dashboard – interactive version for course")
st.divider()

# ================= SESSION STATE =================
if "insight" not in st.session_state:
    st.session_state.insight = "order_value"

# ================= BUTTONS =================
c1, c2, c3, c4 = st.columns(4)
with c1:
    if st.button("📦 Order Value", use_container_width=True):
        st.session_state.insight = "order_value"
with c2:
    if st.button("🏷 Categories", use_container_width=True):
        st.session_state.insight = "categories"
with c3:
    if st.button("🔥 Products", use_container_width=True):
        st.session_state.insight = "products"
with c4:
    if st.button("👑 Customers", use_container_width=True):
        st.session_state.insight = "customers"

st.divider()

# ================= INSIGHT 1: ORDER VALUE =================
if st.session_state.insight == "order_value":
    with st.expander("📦 Order Value Analysis (Min – Max – Avg)", expanded=True):
        min_val = 7.27
        max_val = 138271.15
        avg_val = 9094.97
        c1, c2, c3 = st.columns(3)
        c1.metric("Minimum Order Value", f"${min_val:,.2f}")
        c2.metric("Maximum Order Value", f"${max_val:,.2f}")
        c3.metric("Average Order Value", f"${avg_val:,.2f}")
        st.info(
            "📌 Shows the minimum, maximum, and average order value to understand "
            "customer spending behavior and pricing performance."
        )

# ================= INSIGHT 2: TOP CATEGORIES =================
elif st.session_state.insight == "categories":
    with st.expander("🏷 Top Selling Categories", expanded=True):
        categories_df = pd.DataFrame({
            "Category": [
                "Clothing", "Food & Groceries", "Books", "Toys & Games",
                "Pet Supplies", "Electronics", "Furniture", "Sports & Outdoors",
                "Accessories", "Beauty & Personal Care", "Health & Wellness", "Home & Kitchen"
            ],
            "Total Sold": [
                204204, 171014, 170506, 158441,
                157479, 151281, 137849, 137255,
                136754, 114981, 88628, 79273
            ]
        })
        fig = px.bar(categories_df, x="Category", y="Total Sold",
                     title="Top Selling Categories", text="Total Sold")
        fig.update_layout(xaxis_title="Category", yaxis_title="Total Sold")
        st.plotly_chart(fig, use_container_width=True)
        st.success(
            "📌 Clothing generates the highest quantity sold, "
            "making it the strongest performing category."
        )

# ================= INSIGHT 3: BEST PRODUCTS =================
elif st.session_state.insight == "products":
    with st.expander("🔥 Best Selling Products", expanded=True):
        products_df = pd.DataFrame({
            "Product": [
                "Athletic Sports Bra",
                "Hiking Gaiters",
                "Sweet Potato and Chickpea Bowl",
                "Fashionable Fanny Pack",
                "Pet Training Clicker"
            ],
            "Sales": [23554, 23194, 23173, 23123, 23092]
        })
        top_n = st.slider("Select Top N Products", min_value=1, max_value=5, value=5)
        top_products = products_df.head(top_n)
        fig_bar = px.bar(top_products, x="Product", y="Sales", text="Sales", title=f"Top {top_n} Products")
        fig_pie = px.pie(top_products, names="Product", values="Sales", title=f"Sales Distribution for Top {top_n}")
        col1, col2 = st.columns(2)
        col1.plotly_chart(fig_bar, use_container_width=True)
        col2.plotly_chart(fig_pie, use_container_width=True)
        st.info(
            "📌 Top selling products highlight where to focus production, "
            "inventory planning, and promotional campaigns."
        )# ================= INSIGHT 4: TOP CUSTOMERS =================
elif st.session_state.insight == "customers":
    with st.expander("👑 Top Customers", expanded=True):
        customers_df = pd.DataFrame({
            "Customer": [
                "Redd Fordy",
                "Tobey Basnall",
                "Georgy Sharper",
                "Kirk Riddington",
                "Alexandr Benneyworth"
            ],
            "Total Spend ($)": [
                203162.32,
                196857.47,
                182229.21,
                167434.15,
                166332.76
            ]
        })
        top_n = st.slider("Select Top N Customers", min_value=1, max_value=5, value=5)
        top_customers = customers_df.head(top_n)
        fig = px.bar(top_customers, x="Customer", y="Total Spend ($)",
                     text="Total Spend ($)", title=f"Top {top_n} Customers")
        st.plotly_chart(fig, use_container_width=True)
        st.success(
            "📌 Identifying high-value customers helps design loyalty programs "
            "and maintain premium customer service."
        )

# ================= FOOTER =================
st.divider()
st.success("✅ Interactive Dashboard loaded successfully – ready for course use")