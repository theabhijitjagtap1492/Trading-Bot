"""
Binance Spot API client wrapper for Spot Testnet
"""
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceOrderException
from config import Config
from logger import log_api_request, log_api_response, log_error, log_trade_order, log_order_result

class BinanceSpotClient:
    """Wrapper for Binance Spot API client"""
    
    def __init__(self):
        """Initialize the Binance client for Spot Testnet"""
        Config.validate_credentials()
        self.client = Client(Config.API_KEY, Config.SECRET_KEY)
        self.client.API_URL = 'https://testnet.binance.vision/api'
    
    def get_account_info(self):
        try:
            log_api_request("GET", "/api/v3/account")
            account_info = self.client.get_account()
            log_api_response(account_info)
            return account_info
        except BinanceAPIException as e:
            log_error(e, "getting account info")
            raise
    
    def get_symbol_info(self, symbol):
        try:
            log_api_request("GET", f"/api/v3/exchangeInfo for {symbol}")
            exchange_info = self.client.get_exchange_info()
            symbol_info = next((s for s in exchange_info['symbols'] if s['symbol'] == symbol), None)
            log_api_response(symbol_info)
            return symbol_info
        except BinanceAPIException as e:
            log_error(e, f"getting symbol info for {symbol}")
            raise
    
    def get_current_price(self, symbol):
        try:
            log_api_request("GET", f"/api/v3/ticker/price for {symbol}")
            ticker = self.client.get_symbol_ticker(symbol=symbol)
            price = float(ticker['price'])
            log_api_response(f"Current price: {price}")
            return price
        except BinanceAPIException as e:
            log_error(e, f"getting current price for {symbol}")
            raise
    
    def place_market_order(self, symbol, side, quantity):
        try:
            log_trade_order("MARKET", symbol, side, quantity)
            order_params = {
                'symbol': symbol,
                'side': side,
                'type': 'MARKET',
                'quantity': quantity
            }
            log_api_request("POST", "/api/v3/order", order_params)
            order = self.client.create_order(**order_params)
            log_api_response(order)
            log_order_result(order)
            return order
        except (BinanceAPIException, BinanceOrderException) as e:
            log_error(e, f"placing market order for {symbol}")
            raise
    
    def place_limit_order(self, symbol, side, quantity, price):
        try:
            log_trade_order("LIMIT", symbol, side, quantity, price)
            order_params = {
                'symbol': symbol,
                'side': side,
                'type': 'LIMIT',
                'timeInForce': 'GTC',
                'quantity': quantity,
                'price': price
            }
            log_api_request("POST", "/api/v3/order", order_params)
            order = self.client.create_order(**order_params)
            log_api_response(order)
            log_order_result(order)
            return order
        except (BinanceAPIException, BinanceOrderException) as e:
            log_error(e, f"placing limit order for {symbol}")
            raise
    
    def place_stop_limit_order(self, symbol, side, quantity, price, stop_price):
        try:
            log_trade_order("STOP_LIMIT", symbol, side, quantity, price)
            order_params = {
                'symbol': symbol,
                'side': side,
                'type': 'STOP_LOSS_LIMIT',
                'timeInForce': 'GTC',
                'quantity': quantity,
                'price': price,
                'stopPrice': stop_price
            }
            log_api_request("POST", "/api/v3/order", order_params)
            order = self.client.create_order(**order_params)
            log_api_response(order)
            log_order_result(order)
            return order
        except (BinanceAPIException, BinanceOrderException) as e:
            log_error(e, f"placing stop-limit order for {symbol}")
            raise
    
    def get_order_status(self, symbol, order_id):
        try:
            log_api_request("GET", f"/api/v3/order for {symbol} order {order_id}")
            order_status = self.client.get_order(symbol=symbol, orderId=order_id)
            log_api_response(order_status)
            return order_status
        except BinanceAPIException as e:
            log_error(e, f"getting order status for {order_id}")
            raise
    
    def cancel_order(self, symbol, order_id):
        try:
            log_api_request("DELETE", f"/api/v3/order for {symbol} order {order_id}")
            cancel_result = self.client.cancel_order(symbol=symbol, orderId=order_id)
            log_api_response(cancel_result)
            return cancel_result
        except BinanceAPIException as e:
            log_error(e, f"canceling order {order_id}")
            raise
    
    def get_open_orders(self, symbol=None):
        try:
            params = {'symbol': symbol} if symbol else {}
            log_api_request("GET", "/api/v3/openOrders", params)
            open_orders = self.client.get_open_orders(**params)
            log_api_response(open_orders)
            return open_orders
        except BinanceAPIException as e:
            log_error(e, "getting open orders")
            raise 