import asyncio
from typing import List, Dict
from config import Config
from utils.logger import setup_logger
from trading.market_data import MarketData
from trading.technical_analyzer import TechnicalAnalyzer
from trading.risk_manager import RiskManager
from trading.trade_executor import TradeExecutor
from ml.trade_learner import TradeLearner

class TradingBot:
    def __init__(self):
        self.logger = setup_logger()
        self.logger.info("Initializing TradingBot components...")

        try:
            self.market_data = MarketData()
            self.technical_analyzer = TechnicalAnalyzer()
            self.risk_manager = RiskManager()
            self.trade_executor = TradeExecutor()
            self.trade_learner = TradeLearner()
            self.active_trades = {}
            self.logger.info("TradingBot initialization completed")
        except Exception as e:
            self.logger.error(f"Error during TradingBot initialization: {str(e)}")
            raise

    async def start(self):
        self.logger.info("Starting trading bot...")
        self.logger.info(f"Paper trading mode: {Config.PAPER_TRADING}")

        while True:
            try:
                top_assets = await self.market_data.get_top_assets(Config.TOP_ASSETS_COUNT)
                self.logger.info(f"Top {Config.TOP_ASSETS_COUNT} assets: {top_assets}")

                for asset in top_assets:
                    await self.process_asset(asset)

                if self.active_trades:
                    await self.manage_positions()

                await self.trade_learner.train()
                await asyncio.sleep(60)

            except Exception as e:
                self.logger.error(f"Error in main loop: {str(e)}")
                await asyncio.sleep(60)
