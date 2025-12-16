from enum import Enum
from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_WEATHER = "https://api.openweathermap.org/data/2.5"
API_KEY_WEATHER = getenv("API_KEY_WEATHER")


class Location(Enum):
    LATITUDE = getenv("LATITUDE")
    LONGITUDE = getenv("LONGITUDE")
