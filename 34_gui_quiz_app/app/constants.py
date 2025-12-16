from enum import Enum

API_QUESTION = "https://opentdb.com/api.php"


class ConfigView(Enum):
    TITLE = "Quizzler"
    FONT = ("Arial", 20, "italic")


class ColorPalette(Enum):
    THEME = "#375362"
    WHITE = "#FFFFFF"
    GREEN = "#51cf66"
    RED = "#FF6B6B"


class Size(Enum):
    PADDING_WINDOW = 20
    PADDING_CANVAS = 50
    PADDING_QUESTION = 20
    CANVAS = (300, 250)


class Path(Enum):
    IMG_TRUE = "app/assets/images/true.png"
    IMG_False = "app/assets/images/false.png"
