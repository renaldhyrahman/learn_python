from enum import Enum

TITLE = "Password Manager"
PATH_IMG = "logo.png"
PATH_SAVEFILE = "data.csv"
FIELDNAMES = ("Website", "Email", "Password")

FONT_TEXT = ("Roboto", 12, "normal")


class Size(Enum):
    CANVAS = 200
    PADDING = 50
    WIDTH_SM = 21
    WIDTH_MD = 35
    WIDTH_LG = 36
