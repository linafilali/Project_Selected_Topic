import pandas as pd

df = pd.read_csv("data/sales_data_2017.csv")

# Verify Revenue
print("Total Revenue:", df["Sales"].sum())

# Verify Profit
print("Total Profit:", df["Profit"].sum())

# Verify Revenue
revenue = df["Sales"].sum()
profit = df["Profit"].sum()
margin = (profit / revenue) * 100
print("Profit Margin:", margin)

# Verify Sales Trend Chart
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Month"] = df["Order Date"].dt.to_period("M")
monthly_sales = df.groupby("Month")["Sales"].sum()
print(monthly_sales)

# Verify Top Products Chart
top_products = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)
print(top_products)