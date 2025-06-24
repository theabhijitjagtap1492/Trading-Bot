import streamlit as st
from binance_client import BinanceSpotClient
from logger import setup_logger
from binance.exceptions import BinanceAPIException, BinanceOrderException

setup_logger()
client = BinanceSpotClient()

st.title("Binance Spot Testnet Trading Bot")

order_type = st.selectbox("Order Type", ["Market", "Limit", "Stop-Limit"])
symbol = st.text_input("Trading Pair Symbol", "BTCUSDT")
side = st.selectbox("Side", ["BUY", "SELL"])
quantity = st.number_input("Quantity", min_value=0.0001, value=0.001, step=0.0001, format="%f")

price = None
stop_price = None
show_price = order_type in ["Limit", "Stop-Limit"]
show_stop_price = order_type == "Stop-Limit"

if show_price:
    price = st.number_input("Price", min_value=0.0, value=0.0, step=0.01, format="%f")
if show_stop_price:
    stop_price = st.number_input("Stop Price", min_value=0.0, value=0.0, step=0.01, format="%f")

if st.button("Place Order"):
    # Validation
    if order_type == "Limit" and (not price or price <= 0):
        st.error("Please enter a valid price greater than 0 for limit orders.")
    elif order_type == "Stop-Limit" and ((not price or price <= 0) or (not stop_price or stop_price <= 0)):
        st.error("Please enter valid price and stop price greater than 0 for stop-limit orders.")
    else:
        try:
            if order_type == "Market":
                order = client.place_market_order(symbol, side, quantity)
            elif order_type == "Limit":
                order = client.place_limit_order(symbol, side, quantity, price)
            elif order_type == "Stop-Limit":
                order = client.place_stop_limit_order(symbol, side, quantity, price, stop_price)
            else:
                st.error("Invalid order type.")
                order = None
            if order:
                st.success(f"Order placed!\nOrder ID: {order.get('orderId')}\nStatus: {order.get('status')}\nPrice: {order.get('price')}\nQuantity: {order.get('origQty')}\nType: {order.get('type')}\nSide: {order.get('side')}")
        except (BinanceAPIException, BinanceOrderException, ValueError) as e:
            st.error(f"Error placing order: {e}") 