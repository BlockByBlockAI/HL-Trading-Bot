from typing import Dict
from config import Config
from hyperliquid.exchange import Exchange
from hyperliquid.utils import constants
from utils.logger import setup_logger
from utils.wallet import create_wallet_config

class TradeExecutor:
    def __init__(self):
        self.logger = setup_logger()
        self.paper_trading = Config.PAPER_TRADING

        try:
            wallet_config = create_wallet_config()
            self.exchange = Exchange(
                wallet=wallet_config,
                base_url="https://api.hyperliquid.xyz"
            )
            self.logger.info("Exchange client initialized successfully")
        except Exception as e:
            self.logger.error(f"Error during TradeExecutor initialization: {str(e)}")
            raise
