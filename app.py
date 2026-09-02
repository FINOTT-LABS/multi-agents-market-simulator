import os
import time
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import streamlit as st
from openai import OpenAI

# Page configurations for a premium, clean dashboard look
st.set_page_config(
    page_title="Finott Labs | Multi-Agent Simulation Engine",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom dark-theme container styling to prevent text overlap
st.markdown("""
    <style>
    .reportview-container .main .block-container{ max-width: 95%; }
    .agent-box {
        padding: 20px;
        border-radius: 10px;
        background-color: #1e293b;
        border: 1px solid #334155;
        margin-bottom: 20px;
        color: #f8fafc;
    }
    pre { white-space: pre-wrap !important; word-wrap: break-word !important; }
    code { white-space: pre-wrap !important; }
    </style>
""", unsafe_allow_html=True)

# Initialize Client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=st.secrets["OPENROUTER_API_KEY"]  # Make sure your real key is here
)

def query_agent(agent_role, agent_persona, market_condition):
    """Fetches clean structured markdown data from Nemotron 3 Ultra"""
    system_prompt = (
        f"You are an expert quantitative AI model inside Finott Labs. Role: {agent_role}. "
        f"Persona: {agent_persona}. CRITICAL: Do not use wide horizontal ASCII grid boxes or tabs that cause overlapping text. "
        f"Use standard Markdown bolding, clean bullet points, or clean vertical tables instead."
    )
    user_content = f"Market Shock: {market_condition}\n\nProvide your analysis."
    
    for attempt in range(3):
        try:
            completion = client.chat.completions.create(
                model="nvidia/nemotron-3-ultra-550b-a55b:free",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_content}
                ],
                extra_body={"enable_thinking": False}
            )
            if completion and completion.choices:
                return completion.choices[0].message.content
        except:
            time.sleep(1)
    return "⚠️ Server busy. Please recalculate matrix."

# --- APP LAYOUT ---
st.title("⚡ FINOTT LABS | Algorithmic Multi-Agent Simulator")
st.subheader("Project Alpha-2: Autonomous Risk & Quant Matrix Sandbox")
st.markdown("---")

# Metrics Ribbon
m1, m2, m3, m4 = st.columns(4)
m1.metric("Engine Tier", "Nemotron 550B MoE", "Active: 55B")
m2.metric("Simulation Mode", "Event-Driven Shock", "Active")
m3.metric("Quant Target P&L", "+$1.5M - $2.5M", "Targeting Spread")
m4.metric("Risk Guardrails", "Max 10x Leverage", "Locked")

st.markdown("### 🛠️ Market Simulation Control Panel")

# Inputs
market_shock = st.text_area(
    "Define Macroeconomic or Supply-Side Shock Vector:",
    value="A major global shipping channel is blocked, causing oil prices to spike 15% instantly.",
    height=75
)

if st.button("🚀 Execute Simulation Engine", use_container_width=True):
    with st.spinner("Processing deep agent routing vectors..."):
        
        quant_p = "Aggressive high-frequency momentum trader. Focuses on calendar spreads, cracks, and immediate execution matrices."
        risk_p = "Conservative risk manager. Targets tail-risk, margin call cliffs, and non-stationary Volatility expansion."
        
        quant_out = query_agent("Quant Trader (Bull)", quant_p, market_shock)
        risk_out = query_agent("Risk Manager (Bear)", risk_p, market_shock)
        
        # Tabs layout separating Text Matrix vs Interactive Chart Viz
        tab1, tab2 = st.tabs(["📊 Agent Strategic Positions", "📈 Real-Time Price Simulation Plot"])
        
        with tab1:
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("### 🟢 QUANT TRADER (BULL) VECTOR")
                st.info(quant_out)
            with col2:
                st.markdown("### 🔴 RISK MANAGER (BEAR) CRITIQUE")
                st.error(risk_out)
                
        with tab2:
            st.markdown("### Simulated Shock Vector Projections ($OIL vs Portfolio Trajectory)")
            
            # Generating realistic mock simulation data points
            np.random.seed(42)
            days = np.arange(1, 31)
            base_oil = 75 + np.cumsum(np.random.normal(0.2, 1.5, 30))
            base_oil[5:] += 15.0 # Simulating the 15% instant shock on Day 5
            
            portfolio_val = 100 + np.cumsum(np.random.normal(0.1, 0.8, 30))
            portfolio_val[5:12] -= 4.5 # Risk drawdown during initial shock
            portfolio_val[12:] += 12.0 # Recovery via targeted options spread hedging
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=days, y=base_oil, name="Crude Oil Price ($/bbl)", line=dict(color="#f59e0b", width=3)))
            fig.add_trace(go.Scatter(x=days, y=portfolio_val, name="Finott Labs Portfolio NAV", line=dict(color="#10b981", width=3, dash='dash')))
            
            fig.update_layout(
                title="30-Day Forward Look Matrix Projections",
                template="plotly_dark",
                xaxis_title="Simulation Timeline (Days)",
                yaxis_title="Normalized Value Indices",
                legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01)
            )
            st.plotly_chart(fig, use_container_width=True)

