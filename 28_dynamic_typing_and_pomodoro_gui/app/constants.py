from enum import Enum

TITLE = "Pomodoro"
PATH_IMG = "assets/tomato.png"
SIZE_SCREEN = 400
FONT_NAME = "Courier"


class Color(Enum):
    PINK = "#e2979c"
    RED = "#e7305b"
    GREEN = "#9bdeac"
    YELLOW = "#f7f5dd"
    WHITE = "#ffffff"


class Font(Enum):
    TITLE = (FONT_NAME, 36, "bold")
    TIMER = (FONT_NAME, 24, "bold")
    TEXT = (FONT_NAME, 12, "normal")


# Debug, temp change 1mins = 5 sec for development
multiplier = 5


# Time is in seconds, 60 * 25 means 25 minutes
class Timer(Enum):
    IDLE = 0
    LOOP = 4
    WORK = multiplier * 25
    SHORT_BREAK = multiplier * 5
    LONG_BREAK = multiplier * 20
