from os import getenv

from dotenv import load_dotenv

# load env
load_dotenv()

API = "https://api.sunrise-sunset.org/json"

LATITUDE = getenv("LATITUDE")
LONGITUDE = getenv("LONGITUDE")
