from typing import Dict
from config import Config
from utils.logger import setup_logger

class RiskManager:
    def __init__(self):
        self.logger = setup_logger()

    def calculate_position_size(self, asset: str, entry_price: float) -> float:
        try:
            return self._calculate_base_position_size(entry_price)
        except Exception as e:
            self.logger.error(f"Error calculating position size: {str(e)}")
            return 0
