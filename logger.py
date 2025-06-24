"""
Logging module for the Binance Futures Trading Bot
"""
import logging
import os
from datetime import datetime
from config import Config

def setup_logger():
    """Setup and configure the logger"""
    
    # Create logs directory if it doesn't exist
    os.makedirs('logs', exist_ok=True)
    
    # Configure logging
    logging.basicConfig(
        level=getattr(logging, Config.LOG_LEVEL),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(Config.LOG_FILE),
            logging.StreamHandler()  # Also log to console
        ]
    )
    
    return logging.getLogger('BinanceTradingBot')

def log_api_request(method, endpoint, params=None):
    """Log API request details"""
    logger = logging.getLogger('BinanceTradingBot')
    logger.info(f"API Request: {method} {endpoint}")
    if params:
        logger.info(f"Parameters: {params}")

def log_api_response(response):
    """Log API response details"""
    logger = logging.getLogger('BinanceTradingBot')
    logger.info(f"API Response: {response}")

def log_error(error, context=""):
    """Log error details"""
    logger = logging.getLogger('BinanceTradingBot')
    logger.error(f"Error {context}: {str(error)}")

def log_trade_order(order_type, symbol, side, quantity, price=None):
    """Log trade order details"""
    logger = logging.getLogger('BinanceTradingBot')
    price_info = f" at {price}" if price else ""
    logger.info(f"Placing {order_type} {side} order for {quantity} {symbol}{price_info}")

def log_order_result(order_result):
    """Log order result details"""
    logger = logging.getLogger('BinanceTradingBot')
    logger.info(f"Order Result: {order_result}") 