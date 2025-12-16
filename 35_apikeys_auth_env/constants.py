from enum import Enum
from os import getenv

from dotenv import load_dotenv

load_dotenv()


class OpenWeatherMap(Enum):
    API = "https://api.openweathermap.org/data/2.5"
    TOKEN = getenv("API_TOKEN_WEATHER")


class Telegram(Enum):
    BOT_API = "https://api.telegram.org/bot"
    BOT_TOKEN = getenv("TELEGRAM_BOT_TOKEN")
    CHAT_ID = getenv("TELEGRAM_CHAT_ID")


class Location(Enum):
    LATITUDE = getenv("MY_LATITUDE")
    LONGITUDE = getenv("MY_LONGITUDE")
