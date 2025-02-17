from typing import Dict
from config import Config

def create_wallet_config() -> Dict:
    """
    Creates a wallet configuration for Hyperliquid SDK based on environment variables.
    The wallet config follows the format specified in the SDK documentation.
    """
    return {
        "secret_key": Config.API_KEY,
        "account_address": Config.API_SECRET,
        "multi_sig": {
            "authorized_users": []
        }
    }
