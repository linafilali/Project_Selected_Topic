import pandas as pd


def compute_kpis(df):

    # Ensure correct column names
    df["Order Date"] = pd.to_datetime(df["Order Date"])

    # Revenue & Profit
    total_revenue = df["Sales"].sum()
    total_profit = df["Profit"].sum()

    profit_margin = (total_profit / total_revenue) * 100 if total_revenue != 0 else 0

    # Monthly growth
    df["Month"] = df["Order Date"].dt.to_period("M")
    monthly_sales = df.groupby("Month")["Sales"].sum()

    growth = monthly_sales.pct_change().mean() * 100

    # Top products
    top_products = (
        df.groupby("Product Name")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
        .index.tolist()
    )

    # Worst category
    worst_category = (
        df.groupby("Category")["Profit"]
        .sum()
        .idxmin()
    )

    return {
        "total_revenue": round(total_revenue, 2),
        "total_profit": round(total_profit, 2),
        "profit_margin": round(profit_margin, 2),
        "avg_growth": round(growth if pd.notna(growth) else 0, 2),
        "top_products": top_products,
        "worst_category": worst_category
    }