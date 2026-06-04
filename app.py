import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Forex Position Size Calculator",
    page_icon="📈",
    layout="centered"
)

# Title
st.title("📈 Forex Position Size Calculator")

st.info(
    "Calculate your position size based on account balance, risk percentage and stop loss."
)

# Pair Selection
pair = st.selectbox(
    "Select Instrument",
    [
        "EURUSD",
        "GBPUSD",
        "USDJPY",
        "XAUUSD",
        "NAS100",
        "US30"
    ]
)

# Inputs
account_size = st.number_input(
    "Account Size ($)",
    min_value=0.0,
    value=10000.0
)

risk_percent = st.number_input(
    "Risk Percentage (%)",
    min_value=0.01,
    value=1.0
)

stop_loss = st.number_input(
    "Stop Loss (Pips / Points)",
    min_value=0.1,
    value=20.0
)

# Pip Values
pip_values = {
    "EURUSD": 10,
    "GBPUSD": 10,
    "USDJPY": 9,
    "XAUUSD": 1,
    "NAS100": 1,
    "US30": 1
}

# Calculations
risk_amount = account_size * (risk_percent / 100)

lot_size = risk_amount / (
    stop_loss * pip_values[pair]
)

# Results
st.divider()

st.subheader("Results")

st.metric(
    "Risk Amount",
    f"${risk_amount:.2f}"
)

st.metric(
    "Lot Size",
    f"{lot_size:.2f}"
)

# Warning
st.warning(
    "Contract sizes and pip values may vary between brokers. Always verify before placing a live trade."
)

# Footer
st.markdown("---")
st.caption("Built with Python & Streamlit")