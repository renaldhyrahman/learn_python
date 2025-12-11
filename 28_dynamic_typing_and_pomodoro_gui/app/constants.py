from enum import Enum

TITLE = "Pomodoro"
PATH_IMG = "assets/tomato.png"
SIZE_SCREEN = 500
FONT_NAME = "Courier"


class Color(Enum):
    PINK = "#e2979c"
    RED = "#e7305b"
    GREEN = "#9bdeac"
    YELLOW = "#f7f5dd"
    WHITE = "#ffffff"
    BLACK = "#000000"


class Font(Enum):
    TITLE = (FONT_NAME, 36, "bold")
    TIMER = (FONT_NAME, 24, "bold")
    TEXT = (FONT_NAME, 12, "normal")


class Timer(Enum):
    # (<displayed text>, <max_counter>)
    MAX_LOOP = ("✔", 4)
    # (<displayed text>, <time in minutes>)
    IDLE = ("Timer", 0)
    WORK = ("Work", 25)
    SHORT_BREAK = ("Short Break", 5)
    LONG_BREAK = ("Long Break", 20)
