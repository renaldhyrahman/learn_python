from enum import Enum
from os import getenv

from dotenv import load_dotenv

# fetch .env
load_dotenv()


class Smtp(Enum):
    HOST = getenv("SMTP_HOST")
    PORT = getenv("SMTP_PORT")
    USER = getenv("SMTP_USER")
    PWD = getenv("SMTP_PWD")


class Path(Enum):
    LETTERS_DIR = "assets/letter_templates"
    DATA = "assets/birthdays.csv"
