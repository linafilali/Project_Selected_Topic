# AI Sales Intelligence Engine

The **AI Sales Intelligence Engine** is an interactive analytics dashboard built with **Streamlit** that combines traditional business analytics with **Retrieval-Augmented Generation (RAG)** to provide intelligent insights from sales data and company knowledge sources.

The system analyzes sales performance, computes key business metrics, and allows users to ask natural language questions about company performance.

The goal of this project is to demonstrate how **AI-driven analytics systems** can support **executive decision-making and strategic planning**.

---

# Key Features

- Interactive **Streamlit dashboard**
- Automatic **KPI computation**
- **Sales performance visualization**
- **Retrieval-Augmented Generation (RAG)** for contextual answers
- Integration of **company strategy and industry benchmarks**
- Natural language **business question answering**

---

# System Architecture

The system is composed of three main layers:

### 1. Data Layer
Stores raw sales data and structured company knowledge.

### 2. Analytics Layer
Computes key performance indicators and prepares insights.

### 3. AI Intelligence Layer
Retrieves relevant business knowledge and generates contextual answers.

---

# Project Structure

```
Project_Selected_Topic
│
├── data
│   ├── sales_data.csv
│   └── sales_data_2017.csv
│
├── knowledge_base
│   ├── company_strategy.txt
│   ├── industry_benchmarks.txt
│   ├── kpi_rules.txt
│   └── risk_guidelines.txt
│
├── app.py
├── kpi_engine.py
├── rag_engine.py
├── filter.py
├── check.py
├── requirements.txt
```

---

# Components

### app.py
Main **Streamlit application** that provides the interactive dashboard interface.

### kpi_engine.py
Responsible for calculating business metrics such as:

- Revenue
- Profit
- Profit margin
- Sales growth
- Top performing products

### rag_engine.py
Implements the **Retrieval-Augmented Generation pipeline**, which:

- Searches the knowledge base
- Retrieves relevant business context
- Augments the AI model's responses

### data/
Contains sales datasets used for analysis.

We are using the **Superstore Sales Dataset**, a publicly available retail dataset commonly used for business analytics and dashboard development.

The dataset contains transactional sales records including:

- Order Date
- Product Name
- Category and Sub-Category
- Sales
- Profit
- Customer Segment
- Region

We filtered one year (2017) to make it simpler for testing.

### knowledge_base/
Contains business documents used by the RAG system including: (all AI generated)

- Company strategy guidelines
- Industry benchmark information
- KPI evaluation rules
- Risk management guidelines

---

# Installation

Before running the project, it is recommended to create a **Python virtual environment** to manage dependencies.

### Step 1 — Clone the repository

```bash
git clone https://github.com/linafilali/Project_Selected_Topic.git
cd Project_Selected_Topic
```

---

### Step 2 — Create a virtual environment

```bash
python -m venv ai_env
```

Activate the environment:

Mac / Linux

```bash
source ai_env/bin/activate
```

Windows

```bash
ai_env\Scripts\activate
```

---

### Step 3 — Install required packages

Install all dependencies using the requirements file:

```bash
pip install -r requirements.txt
```

This will install the required libraries such as:

- streamlit
- pandas
- plotly
- requests
- faiss (for retrieval search)

---

# Running the Application

Once the environment is activated and dependencies are installed, run the dashboard with:

```bash
streamlit run app.py
```

The application will start locally and open in your browser.

---

# Technologies Used

- Python
- Streamlit
- Pandas
- Plotly
- FAISS
- Retrieval-Augmented Generation (RAG)

---

# Future Improvements

Potential extensions of the system include:

- Improving the **semantic search capability** by enhancing the embedding and retrieval pipeline to ensure that retrieved knowledge is more contextually relevant to user queries.

- Refining the **Retrieval-Augmented Generation (RAG) architecture** to improve how the system selects and ranks knowledge base documents before generating responses.

- Implementing more advanced **document chunking and indexing strategies** to improve retrieval precision and reduce irrelevant context.
