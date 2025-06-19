import streamlit as st
import pandas as pd

st.set_page_config(page_title="Buy/Sell Selection", layout="wide")
st.title("📥 Phase 2: Order Action")

# Load selection data
selection = st.session_state.get("selection", None)

if not selection:
    st.error("⚠️ No stock selected! Please go back to the Home page and select a stock.")
    st.stop()

# Display selection summary
st.markdown("### 📦 Selected Stock:")
stock_data = {
    "Name": [selection["name"]],
    "Symbol": [selection["symbol"]],
    "Exchange": [selection["exchange"]],
    "Quantity": [selection["quantity"]],
    "Order Type": [selection["order_type"]],
    "Last Price": [f"₹{selection['last_price']}"]
}
st.table(pd.DataFrame(stock_data))

# Limit price input if order type is LIMIT
if selection["order_type"].upper() == "LIMIT":
    limit_price = st.number_input("💰 Enter Limit Price (₹)", min_value=0.0, value=float(selection["last_price"]), step=0.05)
    st.session_state["selection"]["limit_price"] = limit_price
else:
    st.session_state["selection"]["limit_price"] = None

# Transaction type selection
st.markdown("### 🔁 **Choose Transaction Type**")
transaction_type = st.radio("", ["BUY", "SELL"], horizontal=True)
st.session_state["selection"]["transaction_type"] = transaction_type



# Proceed button
if st.button("📤 Proceed to Final Order"):
    st.switch_page("pages/Confirm.py")
