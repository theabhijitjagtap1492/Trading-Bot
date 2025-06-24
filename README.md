# Binance Spot Testnet Trading Bot

A Python trading bot for the Binance Spot Testnet, supporting both command-line and web-based interfaces. Place market, limit, and stop-limit orders, view order results, and log all trading activity. 

## Features
- Place market, limit, and stop-limit orders on the Binance Spot Testnet
- Interactive CLI and modern Streamlit web UI
- Logging of all API requests, responses, and errors
- Configurable via environment variables

## Project Structure

- `binance_client.py`: Binance Spot API client wrapper. Handles all API interactions and order management.
- `bot.py`: Main CLI entry point. Provides an interactive menu for placing orders.
- `web_ui.py`: Streamlit web interface for placing orders via browser.
- `logger.py`: Logging setup and helper functions for API and order events.
- `env.example`: Example environment file. Copy to `.env` and fill in your credentials.
- `requirements.txt`: Python dependencies.
- `logs/bot.log`: Log file for all trading and error events.
- `Demo_video.mp4`: (Optional) Demo video of the bot in action.

## Setup Instructions

1. **Clone the repository**

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**
   - Copy `env.example` to `.env` and fill in your Binance Spot Testnet API key and secret.

4. **Create `config.py`**
   - The code expects a `config.py` file with a `Config` class providing API keys, log file path, and log level. Example template:
     ```python
     import os
     from dotenv import load_dotenv
     load_dotenv()

     class Config:
         API_KEY = os.getenv('BINANCE_API_KEY')
         SECRET_KEY = os.getenv('BINANCE_SECRET_KEY')
         LOG_FILE = 'logs/bot.log'
         LOG_LEVEL = 'INFO'

         @staticmethod
         def validate_credentials():
             if not Config.API_KEY or not Config.SECRET_KEY:
                 raise ValueError('API credentials are not set.')
     ```

## Usage

### Command-Line Interface
```bash
python bot.py
```
Follow the interactive prompts to place orders.

### Web Interface
```bash
streamlit run web_ui.py
```
Open the provided local URL in your browser to use the web UI.

## Environment Variables
See `env.example` for required variables:
- `BINANCE_API_KEY`: Your Binance Spot Testnet API key
- `BINANCE_SECRET_KEY`: Your Binance Spot Testnet secret key
- `DEFAULT_SYMBOL`: Default trading pair (e.g., BTCUSDT)
- `DEFAULT_QUANTITY`: Default order quantity

## Logs
All trading activity and errors are logged to `logs/bot.log`.

## Demo
If provided, see `Demo_video.mp4` for a demonstration of the bot in action.

## Notes
- **config.py is required**: Ensure you create this file as described above.
- This bot is for educational/testing purposes on the Binance Spot Testnet only. Do not use with real funds. 