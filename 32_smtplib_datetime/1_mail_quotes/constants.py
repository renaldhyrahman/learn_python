from enum import Enum
from os import getenv

from dotenv import load_dotenv

# fetch .env
load_dotenv()


class Smtp(Enum):
    # 1
    HOST_1 = getenv("SMTP_HOST_1")
    PORT_1 = getenv("SMTP_PORT_1")
    USER_1 = getenv("SMTP_USER_1")
    PWD_1 = getenv("SMTP_PWD_1")
    # 2
    HOST_2 = getenv("SMTP_HOST_2")
    PORT_2 = getenv("SMTP_PORT_2")
    USER_2 = getenv("SMTP_USER_2")
    PWD_2 = getenv("SMTP_PWD_2")


PATH_QUOTES = "quotes.txt"
