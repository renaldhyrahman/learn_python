from enum import Enum
from os import getenv
from typing import Final

from dotenv import load_dotenv

load_dotenv()

STOCK: Final = "TSLA"
COMPANY_NAME: Final = "Tesla Inc"


class API(Enum):
    ALPHAVANTAGE_API = "https://www.alphavantage.co"
    ALPHAVANTAGE_TOKEN = getenv("ALPHAVANTAGE_TOKEN")
    NEWSAPI_API = "https://newsapi.org/v2"
    NEWSAPI_TOKEN = getenv("NEWSAPI_TOKEN")


class Telegram(Enum):
    BOT_API = "https://api.telegram.org/bot"
    BOT_TOKEN = getenv("TELEGRAM_TOKEN")
    CHAT_ID = getenv("TELEGRAM_CHAT_ID")
