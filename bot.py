"""
Main CLI entry point for the Binance Futures Trading Bot
"""
import argparse
from binance.exceptions import BinanceAPIException, BinanceOrderException
from binance_client import BinanceSpotClient
from logger import setup_logger, log_error


def print_order_result(order):
    print("\nOrder Result:")
    print(f"  Order ID:   {order.get('orderId')}")
    print(f"  Status:     {order.get('status')}")
    print(f"  Price:      {order.get('price')}")
    print(f"  Quantity:   {order.get('origQty')}")
    print(f"  Type:       {order.get('type')}")
    print(f"  Side:       {order.get('side')}")


def interactive_menu():
    print("\n=== Binance Spot Testnet Trading Bot ===")
    print("Select order type:")
    print("1. Market Order")
    print("2. Limit Order")
    print("3. Stop-Limit Order")
    order_type = input("Enter choice (1/2/3): ").strip()
    symbol = input("Enter trading pair symbol (e.g., BTCUSDT): ").strip().upper()
    side = input("Enter side (BUY/SELL): ").strip().upper()
    quantity = float(input("Enter quantity: ").strip())
    price = None
    stop_price = None
    if order_type == '2' or order_type == '3':
        price = float(input("Enter price: ").strip())
    if order_type == '3':
        stop_price = float(input("Enter stop price: ").strip())
    return order_type, symbol, side, quantity, price, stop_price


def main():
    setup_logger()
    client = BinanceSpotClient()

    # Interactive CLI menu
    order_type, symbol, side, quantity, price, stop_price = interactive_menu()

    try:
        if order_type == '1':
            order = client.place_market_order(symbol, side, quantity)
        elif order_type == '2':
            order = client.place_limit_order(symbol, side, quantity, price)
        elif order_type == '3':
            order = client.place_stop_limit_order(symbol, side, quantity, price, stop_price)
        else:
            raise ValueError('Invalid order type.')
        print_order_result(order)
    except (BinanceAPIException, BinanceOrderException, ValueError) as e:
        log_error(e, "CLI order placement")
        print(f"Error: {e}")

if __name__ == "__main__":
    main() 