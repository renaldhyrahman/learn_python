from os import getenv
from typing import Final

from dotenv import load_dotenv

load_dotenv()

PIXELA_API: Final = "https://pixe.la/v1/users"


USER_USERNAME: Final = getenv("APP_USERNAME")
if not USER_USERNAME:
    raise RuntimeError("Missing USER_USERNAME")
USER_TOKEN: Final = getenv("APP_USERTOKEN")
if not USER_TOKEN:
    raise RuntimeError("Missing USER_TOKEN")
