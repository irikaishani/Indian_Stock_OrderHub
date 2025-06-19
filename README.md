# 🛒 Indian Stock OrderHub

 Indian Stock OrderHub is a Streamlit-based web application that allows users to place live equity orders on NSE using the Upstox v2 API. The app supports selecting stocks, entering quantities, choosing order types (MARKET/LIMIT), and placing CNC (Cash and Carry) delivery-based orders. It is designed with a clean multi-page interface and executes AMO (After Market Orders) if the market is closed.

---

## 📸 Visuals of the Indian Stock OrderHub


---

## 🚀 Features

- 📦 Select NSE equity stocks using instrument token
- 🛒 Choose:
  - Order Type: `MARKET` or `LIMIT`
  - Transaction Type: `BUY` or `SELL`
- ✅ Place CNC (Cash and Carry) delivery orders via Upstox API
- 🕒 Automatically handles After Market Orders (`is_amo = True`)
- 🔐 Access token loaded securely from `.env` file
- 📑 Order summary preview before confirmation
- ⚠️ Displays clean error messages for invalid tokens or API issues

---

## 🧠 Tech Stack

- **Frontend:** Streamlit
- **Backend:** Python
- **APIs Used:**
  - [Upstox v2 API](https://upstox.com) – for live trading and order placement

---

## 📂 Folder Structure

