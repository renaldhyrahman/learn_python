from enum import Enum
from os import getenv

from dotenv import load_dotenv

# fetch .env
load_dotenv()


class Smtp(Enum):
    HOST = getenv("SMTP_HOST_1")
    PORT = getenv("SMTP_PORT_1")
    USER = getenv("SMTP_USER_1")
    PWD = getenv("SMTP_PWD_1")


class Path(Enum):
    LETTERS_DIR = "assets/letter_templates"
    DATA = "assets/birthdays.csv"
