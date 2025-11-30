from enum import Enum


class Color(Enum):
    PINK = "#e2979c"
    RED = "#e7305b"
    GREEN = "#9bdeac"
    YELLOW = "#f7f5dd"
    WHITE = "#ffffff"


class Font(Enum):
    TITLE = ("Courier", 36, "bold")
    TIMER = ("Courier", 24, "bold")
    TEXT = ("Courier", 12, "normal")


# Time is in seconds, 60 * 25 means 25 minutes
class Time(Enum):
    WORK = 60 * 25
    SHORT_BREAK = 60 * 5
    LONG_BREAK = 60 * 20


class Size(Enum):
    SCREEN = 600


class FilePath(Enum):
    BG_IMAGE = "assets/tomato.png"
