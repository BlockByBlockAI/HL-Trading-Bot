import pandas as pd
from typing import Dict, List
from hyperliquid.info import Info
from hyperliquid.exchange import Exchange
from config import Config
from utils.logger import setup_logger
from utils.wallet import create_wallet_config

class MarketData:
    # List of supported markets
    SUPPORTED_MARKETS = [
        "BTC", "ETH", "SOL", "HYPE", "BNB", 
        "XRP", "DOGE", "BERA", "IP", "AI16Z"
    ]

    def __init__(self):
        self.logger = setup_logger()
        self.logger.info("Initializing MarketData with Hyperliquid SDK...")

        try:
            # Initialize Info API client with explicit mainnet URL
            self.base_url = "https://api.hyperliquid.xyz"
            self.info = Info(base_url=self.base_url)
            self.logger.info("Info API client initialized with mainnet URL")
            self.logger.info(f"Using base URL: {self.base_url}")

            # Initialize exchange with wallet configuration
            wallet_config = create_wallet_config()
            self.exchange = Exchange(
                wallet=wallet_config,
                base_url=self.base_url
            )
            self.logger.info("Exchange client initialized successfully")

        except Exception as e:
            self.logger.error(f"Error during MarketData initialization: {str(e)}")
            raise
