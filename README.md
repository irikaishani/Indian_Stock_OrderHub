# 🛒 Indian Stock OrderHub

 Indian Stock OrderHub is a Streamlit-based web application that allows users to place live equity orders on NSE using the Upstox v2 API. The app supports selecting stocks, entering quantities, choosing order types (MARKET/LIMIT), and placing CNC (Cash and Carry) delivery-based orders. It is designed with a clean multi-page interface and executes AMO (After Market Orders) if the market is closed.

---

## 📸 Visuals of the Indian Stock OrderHub

![Indian Stock Option Analyzer](https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExNjVqNXE5YXczNzB5NGM3M2ppbnYwcnZwZ3VjdTBoMm8weXJyNTJ4bSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/hI3JvRneWIgzQ7ibaB/giphy.gif)

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

```plaintext
upstox_stock_order/
│
├── .env                           # Stores access token securely
├── app.py                         # Entry point (Home page or navigation)
├── requirements.txt               # Python dependencies
│
├── pages/                         # Streamlit multipage app structure
│   ├── 2_Buy_Stock.py             # Page for stock selection and order setup
│   └── Confirm.py                 # Final page to preview and place the order
│
├── upstox-python/                 # (Optional) Clone from official Upstox GitHub


```
## ⚙️ Installation & Setup

Follow these steps to set up and run the Upstox Stock Order App on your local machine:

---

### 🔁 1. Clone the Repository

```bash
git clone https://github.com/your-username/upstox_stock_order.git
cd upstox_stock_order

```

### Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install Dependencies
```sh
pip install -r requirements.txt
```

### Setup API Access Token
ACCESS_TOKEN=your_upstox_access_token


* Create a .env file in the project root:

```sh
UPSTOX_API_KEY=your_upstox_api_key
UPSTOX_API_SECRET=your_upstox_api_secret
UPSTOX_ACCESS_TOKEN=your_upstock_api_accesstoken


```

### Start the Application
```sh
streamlit run app.py
```







