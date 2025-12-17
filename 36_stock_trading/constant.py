from os import getenv
from typing import Final

from dotenv import load_dotenv

load_dotenv()

STOCK: Final = "TSLA"
COMPANY_NAME: Final = "Tesla Inc"

ALPHAVANTAGE_API: Final = "https://www.alphavantage.co"
ALPHAVANTAGE_TOKEN: Final = getenv("ALPHAVANTAGE_TOKEN")
if not ALPHAVANTAGE_TOKEN:
    raise RuntimeError("Missing ALPHAVANTAGE_TOKEN")

NEWSAPI_API: Final = "https://newsapi.org/v2"
NEWSAPI_TOKEN: Final = getenv("NEWSAPI_TOKEN")
if not NEWSAPI_TOKEN:
    raise RuntimeError("Missing NEWSAPI_TOKEN")

TELEGRAM_BOT_API: Final = "https://api.telegram.org/bot"
TELEGRAM_BOT_TOKEN: Final = getenv("TELEGRAM_TOKEN")
if not TELEGRAM_BOT_TOKEN:
    raise RuntimeError("Missing TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID: Final = getenv("TELEGRAM_CHAT_ID")
if not TELEGRAM_CHAT_ID:
    raise RuntimeError("Missing TELEGRAM_CHAT_ID")
