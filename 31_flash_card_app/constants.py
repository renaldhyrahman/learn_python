from enum import Enum

TITLE = "Flashy"
DELAY = 3  # in seconds
LANGUAGES = ("French", "English")


class Path(Enum):
    DATA = "assets/data/french_words.csv"
    IMG_CARD_FRONT = "assets/images/card_front.png"
    IMG_CARD_BACK = "assets/images/card_back.png"
    IMG_RIGHT = "assets/images/right.png"
    IMG_WRONG = "assets/images/wrong.png"
    RESULT = "words_to_learn.csv"


class Color(Enum):
    GREEN = "#B1DDC6"
    BLACK = "#444"
    WHITE = "#FFF"


class Font(Enum):
    LANGUAGE = ("Ariel", 40, "italic")
    WORD = ("Ariel", 60, "bold")


class Size(Enum):
    CANVAS = (800, 526)
    PADDING = 50


class Coordinate(Enum):
    IMAGE = (400, 263)
    LANGUAGE = (400, 150)
    WORD = (400, 263)
