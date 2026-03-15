import streamlit as st
import pandas as pd
import os
import requests
<<<<<<< HEAD
=======
import plotly.express as px
from rag_engine import retrieve_relevant_chunks
>>>>>>> master

# ---------------------------
# PAGE CONFIG
# ---------------------------
st.set_page_config(page_title="AI Sales Intelligence Engine", layout="wide")

st.title("AI Sales Intelligence Engine")
st.subheader("Executive Analytics & Strategic Decision Support")
st.markdown("---")

<<<<<<< HEAD
=======

>>>>>>> master
# ---------------------------
# KPI ENGINE
# ---------------------------
def compute_kpis(df):
<<<<<<< HEAD
    total_revenue = df["Revenue"].sum()
    total_profit = df["Profit"].sum()
    profit_margin = (total_profit / total_revenue) * 100 if total_revenue != 0 else 0

    df["Date"] = pd.to_datetime(df["Date"])
    df["Month"] = df["Date"].dt.to_period("M")
    monthly_revenue = df.groupby("Month")["Revenue"].sum()
    growth = monthly_revenue.pct_change().mean() * 100
=======

    df = df.copy()

    total_revenue = df["Sales"].sum()
    total_profit = df["Profit"].sum()

    profit_margin = (total_profit / total_revenue) * 100 if total_revenue != 0 else 0

    df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
    df["Month"] = df["Order Date"].dt.to_period("M").dt.to_timestamp()

    monthly_revenue = df.groupby("Month")["Sales"].sum()

    growth = monthly_revenue.pct_change().dropna().mean() * 100

    top_products = (
        df.groupby("Product Name")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(3)
        .index.tolist()
    )

    worst_category = df.groupby("Category")["Profit"].sum().sort_values().index[0]
>>>>>>> master

    return {
        "total_revenue": round(total_revenue, 2),
        "total_profit": round(total_profit, 2),
        "profit_margin": round(profit_margin, 2),
<<<<<<< HEAD
        "avg_growth": round(growth if pd.notna(growth) else 0, 2)
    }

# ---------------------------
# LOAD KNOWLEDGE BASE
# ---------------------------
def load_knowledge():
    knowledge_texts = []
    folder_path = "knowledge_base"

    for file in os.listdir(folder_path):
        if file.endswith(".txt"):
            with open(os.path.join(folder_path, file), "r") as f:
                knowledge_texts.append(f.read())

    return "\n\n".join(knowledge_texts)
=======
        "avg_growth": round(growth if pd.notna(growth) else 0, 2),
        "monthly_sales": monthly_revenue,
        "top_products": top_products,
        "worst_category": worst_category,
    }

>>>>>>> master

# ---------------------------
# RISK LOGIC
# ---------------------------
def determine_risk_level(kpis):
<<<<<<< HEAD
=======

>>>>>>> master
    margin = kpis["profit_margin"]

    if margin >= 30:
        return "Strong", "green"
    elif margin >= 25:
        return "Healthy", "green"
    elif margin >= 20:
        return "Warning", "orange"
    else:
        return "High Risk", "red"

<<<<<<< HEAD
=======

>>>>>>> master
# ---------------------------
# LLM GENERATION
# ---------------------------
def generate_answer(question, kpis, context):

    prompt = f"""
You are a senior executive business analyst.

Use concise executive language.
Maximum 120 words.
Use bullet points only.

KPIs:
Total Revenue: {kpis['total_revenue']}
Total Profit: {kpis['total_profit']}
Profit Margin: {kpis['profit_margin']}%
Average Growth: {kpis['avg_growth']}%

Company Knowledge:
{context[:1500]}

Business Question:
{question}

Respond strictly in this format:

EXECUTIVE SUMMARY:
- 3 bullet points

RISK LEVEL:
- Strong / Healthy / Warning / High Risk
- 2 short explanations

STRATEGIC ACTIONS:
- 3 clear actions
"""

    try:
<<<<<<< HEAD
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "phi3",   # Faster + stable
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": 0.1,
                    "num_predict": 80
                }
            },
            timeout=120
=======

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "phi3",
                "prompt": prompt,
                "stream": False,
                "options": {"temperature": 0.1, "num_predict": 80},
            },
            timeout=120,
        )

        if response.status_code != 200:
            return f"Model error: {response.text}"

        return response.json().get("response", "No response returned.")

    except Exception as e:
        return f"Connection error: {str(e)}"


def generate_executive_report(kpis, context):

    prompt = f"""
You are the Chief Business Analyst for NovaRetail.

The dashboard already shows the KPIs (revenue, profit, margin, growth).
DO NOT repeat KPI values.

Your job is to provide executive interpretation only.

Use concise executive language.
Maximum 120 words.
Bullet points only.

KPIs for internal reasoning:
Revenue: {kpis['total_revenue']}
Profit: {kpis['total_profit']}
Profit Margin: {kpis['profit_margin']}%
Growth: {kpis['avg_growth']}%

Top Products: {kpis['top_products']}
Worst Category: {kpis['worst_category']}

Company Knowledge:
{context[:1500]}

Return EXACTLY this format:

EXECUTIVE INSIGHTS
- insight
- insight

BUSINESS RISKS
- risk
- risk

RECOMMENDED ACTIONS
- action
- action
"""

    try:

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "phi3",
                "prompt": prompt,
                "stream": False,
                "options": {"temperature": 0.1, "num_predict": 120},
            },
            timeout=120,
>>>>>>> master
        )

        if response.status_code != 200:
            return f"Model error: {response.text}"

        return response.json().get("response", "No response returned.")

    except Exception as e:
        return f"Connection error: {str(e)}"

<<<<<<< HEAD
# ---------------------------
# STREAMLIT UI
# ---------------------------
=======

# ---------------------------
# STREAMLIT UI
# ---------------------------

>>>>>>> master
uploaded_file = st.file_uploader("Upload Sales CSV", type=["csv"])

if uploaded_file:

<<<<<<< HEAD
    df = pd.read_csv(uploaded_file)
    kpis = compute_kpis(df)

    # KPI Dashboard
    st.subheader("Performance Dashboard")
=======
    df = pd.read_csv(uploaded_file, encoding="latin1")

    kpis = compute_kpis(df)

    # ---------------------------
    # KPI DASHBOARD
    # ---------------------------

    st.subheader("Performance Dashboard")

>>>>>>> master
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Revenue", f"${kpis['total_revenue']:,}")
    col2.metric("Total Profit", f"${kpis['total_profit']:,}")
    col3.metric("Profit Margin", f"{kpis['profit_margin']}%")
    col4.metric("Growth Rate", f"{kpis['avg_growth']}%")

    st.markdown("---")

<<<<<<< HEAD
    # FORM (prevents request flooding)
    with st.form("analysis_form"):
        question = st.text_input("Ask a business question")
=======
    # ---------------------------
    # SALES TREND
    # ---------------------------

    st.subheader("Sales Trend")

    trend_df = kpis["monthly_sales"].reset_index()
    trend_df.columns = ["Month", "Sales"]

    fig_trend = px.line(
        trend_df,
        x="Month",
        y="Sales",
        title="Monthly Sales Trend"
    )

    st.plotly_chart(fig_trend, use_container_width=True)

    # ---------------------------
    # TOP PRODUCTS
    # ---------------------------

    st.subheader("Top Products")

    top_products = (
        df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(5)
    )

    fig_products = px.bar(
        top_products.reset_index(),
        x="Product Name",
        y="Sales",
        title="Top Products by Sales"
    )

    fig_products.update_layout(xaxis_tickangle=-45)

    st.plotly_chart(fig_products, use_container_width=True)

    # ---------------------------
    # REPORT
    # ---------------------------

    st.markdown("---")
    st.subheader("AI Executive Report")

    with st.spinner("Generating executive report..."):

        context = retrieve_relevant_chunks("retail sales performance strategy risk")

        report = generate_executive_report(kpis, context)

    formatted_report = report.replace("\n", "<br>")

    st.markdown(
        f"""
        <div style="
            background: linear-gradient(90deg,#0f172a,#0b1f3a);
            padding:25px;
            border-radius:12px;
            border-left:6px solid #22c55e;
            font-size:17px;
            line-height:1.6;
        ">
        {formatted_report}
        </div>
        """,
        unsafe_allow_html=True
    )

    # ---------------------------
    # QUESTION INPUT
    # ---------------------------

    st.markdown("---")

    with st.form("analysis_form"):

        question = st.text_input("Ask a business question")

>>>>>>> master
        submitted = st.form_submit_button("Generate Analysis")

    if submitted and question:

        with st.spinner("Generating executive analysis..."):
<<<<<<< HEAD
            context = load_knowledge()
=======

            context = retrieve_relevant_chunks(question)

>>>>>>> master
            answer = generate_answer(question, kpis, context)

        risk_level, color = determine_risk_level(kpis)

<<<<<<< HEAD
        # Risk Box
        st.markdown(f"""
        <div style="
            padding:15px;
            border-radius:10px;
            background-color:#1f2937;
            border-left:6px solid {color};
            font-size:18px;
            font-weight:600;">
        🚦 Risk Status: {risk_level}
        </div>
        """, unsafe_allow_html=True)

        st.markdown("###  Executive Insight")
=======
        st.markdown(
            f"""
            <div style="
                padding:15px;
                border-radius:10px;
                background-color:#1f2937;
                border-left:6px solid {color};
                font-size:18px;
                font-weight:600;">
            🚦 Risk Status: {risk_level}
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("### Executive Insight")

>>>>>>> master
        st.markdown(answer)