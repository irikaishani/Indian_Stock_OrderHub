# 📈 Indian Stock OrderHub

This project is a Streamlit-based multi-page web application that allows you to:
- Select a stock from the NSE
- Choose buy/sell options
- Preview the order
- Place an order via the Upstox API
- Automatically queue the order as AMO (After Market Order) if the market is closed

---

## 🚀 Features

- 📦 Select and preview stock details
- 🛒 Choose order type: Market or Limit
- 🔁 Choose transaction type: BUY or SELL
- 🔐 Securely load access token via `.env` file
- 📬 Order gets placed using Upstox `/v2/order/place` API
- 🕒 Automatically uses `is_amo = True` for execution when the market opens

---

## 📁 Project Structure

