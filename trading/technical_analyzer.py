import numpy as np
import pandas as pd
import pandas_ta as ta
from typing import Dict, List
from utils.logger import setup_logger

class TechnicalAnalyzer:
    def __init__(self):
        self.logger = setup_logger()

    def analyze(self, market_data: Dict[str, pd.DataFrame]) -> Dict:
        try:
            analysis = {}
            for timeframe, df in market_data.items():
                if df.empty:
                    self.logger.warning(f"Empty DataFrame for timeframe {timeframe}")
                    continue
                self.logger.debug(f"Analyzing timeframe {timeframe} with shape {df.shape}")
                analysis[timeframe] = self._analyze_timeframe(df)

            return self._combine_analyses(analysis)
        except Exception as e:
            self.logger.error(f"Error in technical analysis: {str(e)}")
            return {}
