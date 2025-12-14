from enum import Enum

PATH_IMG_CARD_BACK = "assets/images/card_back.png"
PATH_IMG_CARD_FRONT = "assets/images/card_front.png"
PATH_IMG_RIGHT = "assets/images/right.png"
PATH_IMG_WRONG = "assets/images/wrong.png"
PATH_DATA = "assets/data/french_words.csv"


class Color(Enum):
    BG_GREEN = "#B1DDC6"


class Font(Enum):
    LANGUAGE = ("Ariel", 40, "italic")
    WORD = ("Ariel", 60, "bold")
