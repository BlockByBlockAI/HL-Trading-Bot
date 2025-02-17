import asyncio
from trading.bot import TradingBot
from utils.logger import setup_logger

logger = setup_logger()

async def main():
    try:
        bot = TradingBot()
        await bot.start()
    except Exception as e:
        logger.error(f"Fatal error in main application: {str(e)}")
        raise

if __name__ == "__main__":
    asyncio.run(main())
