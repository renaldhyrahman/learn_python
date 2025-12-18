from os import getenv

from dotenv import load_dotenv

load_dotenv()

API = "https://app.100daysofpython.dev"
APP_ID = getenv("APP_ID")
APP_TOKEN = getenv("APP_KEY")
