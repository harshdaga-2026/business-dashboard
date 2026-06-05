
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/sanjayfuloria/business-dashboard/main/business_data.csv"

df = pd.read_csv(url)

st.title("Business Performance Dashboard")

months = st.sidebar.multiselect(
    "Select Month",
    df["Month"],
    default=df["Month"]
)

filtered_df = df[df["Month"].isin(months)]

total_sales = filtered_df["Sales"].sum()
total_expenses = filtered_df["Expenses"].sum()
total_profit = filtered_df["Profit"].sum()
avg_margin = (
    filtered_df["Profit"].sum() /
    filtered_df["Sales"].sum()
) * 100

col1,col2,col3,col4 = st.columns(4)

col1.metric("Total Sales", f"₹{total_sales:,.0f}")
col2.metric("Expenses", f"₹{total_expenses:,.0f}")
col3.metric("Profit", f"₹{total_profit:,.0f}")
col4.metric("Avg Margin", f"{avg_margin:.1f}%")

fig1, ax1 = plt.subplots(figsize=(6,4))
ax1.plot(filtered_df["Month"], filtered_df["Sales"])
ax1.set_title("Monthly Sales")
st.pyplot(fig1)

fig2, ax2 = plt.subplots(figsize=(6,4))
ax2.plot(filtered_df["Month"], filtered_df["Profit"])
ax2.set_title("Profit Trend")
st.pyplot(fig2)

fig3, ax3 = plt.subplots(figsize=(6,4))
ax3.bar(filtered_df["Month"], filtered_df["Sales"], label="Sales")
ax3.bar(filtered_df["Month"], filtered_df["Expenses"], label="Expenses")
ax3.legend()
ax3.set_title("Sales vs Expenses")
st.pyplot(fig3)

filtered_df["Margin"] = (
    filtered_df["Profit"] /
    filtered_df["Sales"]
) * 100

fig4, ax4 = plt.subplots(figsize=(6,4))
ax4.bar(filtered_df["Month"], filtered_df["Margin"])
ax4.set_title("Profit Margin %")
st.pyplot(fig4)

st.subheader("Raw Data")
st.dataframe(filtered_df)
