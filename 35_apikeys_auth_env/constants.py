from enum import Enum
from os import getenv

from dotenv import load_dotenv

load_dotenv()


class API(Enum):
    OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5"
    OWM_KEY = getenv("API_KEY_WEATHER")


class Location(Enum):
    LATITUDE = getenv("LATITUDE")
    LONGITUDE = getenv("LONGITUDE")
