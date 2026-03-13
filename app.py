import streamlit as st
import pandas as pd
import os
import requests

# ---------------------------
# PAGE CONFIG
# ---------------------------
st.set_page_config(page_title="AI Sales Intelligence Engine", layout="wide")

st.title("AI Sales Intelligence Engine")
st.subheader("Executive Analytics & Strategic Decision Support")
st.markdown("---")

# ---------------------------
# KPI ENGINE
# ---------------------------
def compute_kpis(df):
    total_revenue = df["Revenue"].sum()
    total_profit = df["Profit"].sum()
    profit_margin = (total_profit / total_revenue) * 100 if total_revenue != 0 else 0

    df["Date"] = pd.to_datetime(df["Date"])
    df["Month"] = df["Date"].dt.to_period("M")
    monthly_revenue = df.groupby("Month")["Revenue"].sum()
    growth = monthly_revenue.pct_change().mean() * 100

    return {
        "total_revenue": round(total_revenue, 2),
        "total_profit": round(total_profit, 2),
        "profit_margin": round(profit_margin, 2),
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

# ---------------------------
# RISK LOGIC
# ---------------------------
def determine_risk_level(kpis):
    margin = kpis["profit_margin"]

    if margin >= 30:
        return "Strong", "green"
    elif margin >= 25:
        return "Healthy", "green"
    elif margin >= 20:
        return "Warning", "orange"
    else:
        return "High Risk", "red"

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
        )

        if response.status_code != 200:
            return f"Model error: {response.text}"

        return response.json().get("response", "No response returned.")

    except Exception as e:
        return f"Connection error: {str(e)}"

# ---------------------------
# STREAMLIT UI
# ---------------------------
uploaded_file = st.file_uploader("Upload Sales CSV", type=["csv"])

if uploaded_file:

    df = pd.read_csv(uploaded_file)
    kpis = compute_kpis(df)

    # KPI Dashboard
    st.subheader("Performance Dashboard")
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Revenue", f"${kpis['total_revenue']:,}")
    col2.metric("Total Profit", f"${kpis['total_profit']:,}")
    col3.metric("Profit Margin", f"{kpis['profit_margin']}%")
    col4.metric("Growth Rate", f"{kpis['avg_growth']}%")

    st.markdown("---")

    # FORM (prevents request flooding)
    with st.form("analysis_form"):
        question = st.text_input("Ask a business question")
        submitted = st.form_submit_button("Generate Analysis")

    if submitted and question:

        with st.spinner("Generating executive analysis..."):
            context = load_knowledge()
            answer = generate_answer(question, kpis, context)

        risk_level, color = determine_risk_level(kpis)

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
        st.markdown(answer)