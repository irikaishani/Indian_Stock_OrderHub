import streamlit as st
import pandas as pd
import requests
import os
import gzip
import io
import json
from dotenv import load_dotenv
from datetime import datetime

# ------------------ 🌐 Page Setup ------------------ #
st.set_page_config(page_title="Indian Stock OrderHub", layout="wide", page_icon="📈")
st.title("📈 Indian Stock OrderHub (Upstox)")
st.markdown("---")

# ------------------ 🔐 Load API Token ------------------ #
load_dotenv()
access_token = os.getenv("ACCESS_TOKEN", "").strip()

# ------------------ 📦 Load NSE Equity Master ------------------ #
@st.cache_data(show_spinner="📦 Fetching NSE Stock Instruments...")
def load_stock_master():
    url = "https://assets.upstox.com/market-quote/instruments/exchange/NSE.json.gz"
    response = requests.get(url)

    with gzip.GzipFile(fileobj=io.BytesIO(response.content)) as f:
        data = json.load(f)

    df = pd.DataFrame(data)

    # ✅ Filter only NSE Equity stocks
    df = df[(df['segment'] == 'NSE_EQ') & (df['instrument_type'] == 'EQ')]

    # ✅ Remove dummy/test symbols
    df = df[~df['trading_symbol'].str.contains('TEST|DUMMY|SYNTH', case=False, na=False)]
    df = df[~df['name'].str.contains('TEST|DUMMY|SYNTH', case=False, na=False)]

    # ✅ Rename and select columns
    df = df.rename(columns={
        'trading_symbol': 'symbol',
        'instrument_key': 'instrument_key',
        'name': 'name'
    })

    return df[['instrument_key', 'symbol', 'name', 'exchange']].dropna()

# ---------------------- Load Master ---------------------- #
df = load_stock_master()

# ---------------------- UI Section ---------------------- #
st.header("📌 Phase 1: Choose Stock")

# 1️⃣ Select stock
stock_names = sorted(df['name'].unique())
selected_stock_name = st.selectbox("🔍 Select Stock by Name", stock_names)

# 2️⃣ Filter and display
filtered = df[df['name'] == selected_stock_name]
if not filtered.empty:
    selected = filtered.iloc[0]
    instrument_key = selected['instrument_key']

    st.markdown("### 📋 Stock Details")
    st.write("**🧾 Trading Symbol:**", selected['symbol'])
    st.write("**🏦 Exchange:**", selected['exchange'])
    st.write("**🧩 Instrument Key:**", instrument_key)
    


    # ------------------ 💰 Fetch LTP ------------------ #
    st.markdown("### 💰 Last Traded Price")

    quote_url = f"https://api.upstox.com/v2/market-quote/ltp?instrument_key={instrument_key}"
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}"
    }

    try:
        response = requests.get(quote_url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            ltp_data = list(data.get("data", {}).values())[0]  # get first item from dict values

            if "last_price" in ltp_data:
                ltp = ltp_data["last_price"]
                st.success(f"💸 PRICE OF THE STOCK: ₹{ltp}")
            else:
                st.warning("⚠️ 'last_price' not found in API response.")

        else:
            st.error(f"❌ API Error: {response.status_code}")
            st.text(response.text)
    except Exception as e:
        st.error("❌ Request Failed")
        st.exception(e)


# Quantity input 
st.markdown("### 🧮 Quantity Selection")
quantity = st.number_input("Enter number of shares", min_value=1, value=1, step=1)
Total_price=ltp*quantity

st.subheader(f'🧮 Total price = {Total_price}')

    # Order type selection
st.markdown("### ⚙️ Order Type")
order_type = st.selectbox("Choose Order Type", ["Market", "Limit"])

st.markdown("---")
st.subheader("➡️ Proceed to Phase 2: Buy Stock")

# ✅ Convert DataFrame to list of dictionaries
stock_list = load_stock_master().to_dict(orient="records")

# ✅ Find selected stock dictionary
selected_stock = next(
    (stock for stock in stock_list if stock.get('name') == selected_stock_name),
    None
)

if selected_stock and quantity > 0 and order_type:
    if st.button("✅ Confirm Selection and Go to Phase 2"):
        st.session_state["selection"] = {
            "name": selected_stock['name'],
            "instrument_key": selected_stock['instrument_key'],
            "symbol": selected_stock['symbol'],
            "exchange": selected_stock['exchange'],
            "last_price": ltp,
            "quantity": quantity,
            "order_type": order_type
        }
        st.success("✅ Selection saved! Redirecting to Phase 2...")
        st.switch_page("pages/Buy stock.py")  # ✅ Match filename
else:
    st.warning("⚠️ Please select stock, enter quantity, and choose order type before proceeding.")
