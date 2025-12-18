from os import getenv
from typing import Final

from dotenv import load_dotenv

load_dotenv()

PYTHON_API: Final = "https://app.100daysofpython.dev"
PYTHON_APP_ID: Final = getenv("PYTHON_APP_ID")
if not PYTHON_APP_ID:
    raise RuntimeError("Missing PYTHON_APP_ID")
PYTHON_APP_TOKEN: Final = getenv("PYTHON_APP_TOKEN")
if not PYTHON_APP_TOKEN:
    raise RuntimeError("Missing PYTHON_APP_TOKEN")

SHEETY_API = "https://api.sheety.co/"
SHEETY_USERNAME = getenv("SHEETY_USERNAME")
if not SHEETY_USERNAME:
    raise RuntimeError("Missing SHEETY_USERNAME")
SHEETY_TOKEN = getenv("SHEETY_TOKEN")
if not SHEETY_TOKEN:
    raise RuntimeError("Missing SHEETY_TOKEN")
