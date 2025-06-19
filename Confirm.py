import streamlit as st
import requests
import os
from dotenv import load_dotenv

st.set_page_config(page_title="Final Order", layout="wide")
st.title("🚀 Final Order Execution")

# Step 1: Session check
selection = st.session_state.get("selection", None)
if not selection:
    st.error("⚠️ No stock selected! Please go back.")
    st.stop()

# Step 2: Load token
load_dotenv()
access_token = os.getenv("ACCESS_TOKEN", "").strip()

if not access_token:
    st.error("❌ Access token not found. Please check your .env file.")
    st.stop()

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': f'Bearer {access_token}',
}

# Step 3: Parse selection
order_type = selection["order_type"].upper()
txn_type = selection["transaction_type"].upper()
instrument_token = selection["instrument_key"]
quantity = int(selection["quantity"])
limit_price = selection.get("limit_price") or float(selection["last_price"])
product_code = "D"  # 'D' for Delivery (CNC) in HFT

total_cost = float(limit_price) * quantity

# Step 4: Skip Funds check (Optional Warning)
st.markdown("### 💰 Funds Check")
st.warning("⚠️ Skipping funds check – requires main access token, not HFT.")
st.markdown(f"🧾 **Estimated Order Cost**: ₹{total_cost:,.2f}")

# Step 5: Create order payload
order_payload = {
    'quantity': quantity,
    'product': product_code,
    'validity': 'DAY',
    'price': limit_price if order_type == 'LIMIT' else 0,
    'tag': 'OrderHub',
    'instrument_token': instrument_token,
    'order_type': order_type,
    'transaction_type': txn_type,
    'disclosed_quantity': 0,
    'trigger_price': 0,
    'is_amo': True
}

# Step 6: Show preview
st.markdown("### 📄 Order Preview")
st.json(order_payload)

# Step 7: Place order
if st.button("✅ Confirm and Place Order"):
    try:
        url = 'https://api-hft.upstox.com/v2/order/place'
        response = requests.post(url, json=order_payload, headers=headers)

        st.markdown("### 📬 API Response")
        st.code(f"Response Code: {response.status_code}")

        try:
            st.json(response.json())
        except Exception:
            st.text(response.text)

    except Exception as e:
        st.exception(f"🚨 Error placing order: {e}")
