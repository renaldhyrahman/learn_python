from dataclasses import dataclass, field


@dataclass(frozen=True)
class Size:
    UNIT: int
    SCREEN_X: int
    SCREEN_Y: int


class ScreenConfig:
    def __init__(self):
        self.size = Size(UNIT=20, SCREEN_X=600, SCREEN_Y=600)
        self.MAX_X = self.size.SCREEN_X / 2
        self.MAX_Y = self.size.SCREEN_Y / 2
        self.CORX_CENTER = 0
        self.CORY_CENTER = 0

    def get_cor_player_start(self):
        xcor = self.CORX_CENTER
        ycor = -self.MAX_Y + self.size.UNIT
        return (xcor, ycor)

    def get_ui_level_cor(self):
        padding = 2 * self.size.UNIT
        xcor = -self.MAX_X + padding
        ycor = self.MAX_Y - padding
        return (xcor, ycor)


@dataclass
class GameData:
    max_car: int
    cur_speed: float
    cur_level: int
    score: int
    player: object
    cars: list = field(default_factory=list)
    screen: ScreenConfig = field(default_factory=ScreenConfig)
