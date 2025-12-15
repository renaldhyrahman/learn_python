from enum import Enum
from os import getenv

from dotenv import load_dotenv

# load env
load_dotenv()

API_SUNSET = "https://api.sunrise-sunset.org/json"
API_ISS_LOC = "http://api.open-notify.org/iss-now.json"

LATITUDE = float(getenv("LATITUDE"))
LONGITUDE = float(getenv("LONGITUDE"))
TZID = getenv("TZID")

DELTA_ISS_OVERHEAD = 5


class Smtp(Enum):
    USER = getenv("SMTP_USER")
    PWD = getenv("SMTP_PWD")
    HOST = getenv("SMTP_HOST")
    PORT = getenv("SMTP_PORT")
    RECEIVER = getenv("SMTP_RECEIVER")
