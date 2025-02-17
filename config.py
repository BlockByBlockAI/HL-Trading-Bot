import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # API Configuration
    API_KEY = os.getenv('API_KEY')
    API_SECRET = os.getenv('API_SECRET')
    PAPER_TRADING = os.getenv('PAPER_TRADING', 'True').lower() == 'true'

    # Trading Parameters
    TIMEFRAMES = ['1h', '1d', '1w', '1M']
    INITIAL_SL_PERCENTAGE = 0.10  # 10% stop loss
    TRAILING_SL_STEP = 0.02  # 2% step for trailing stop loss
    
    # Technical Indicators
    EMA_PERIODS = [20, 50, 100, 200]
    RSI_PERIOD = 14
    RSI_OVERBOUGHT = 70
    RSI_OVERSOLD = 30
    MACD_FAST = 12
    MACD_SLOW = 26
    MACD_SIGNAL = 9
    
    # Asset Selection
    TOP_ASSETS_COUNT = 5
    
    # Machine Learning
    ML_LOOKBACK_PERIODS = 100
    ML_TRAIN_SIZE = 0.8
