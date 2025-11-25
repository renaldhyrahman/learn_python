from dataclasses import dataclass


@dataclass
class Size:
    UNIT: int = 0
    SCREEN_X: int = 0
    SCREEN_Y: int = 0


class Config:
    def __init__(self):
        self.size = Size(UNIT=20, SCREEN_X=600, SCREEN_Y=600)
        self.SPEED = 0.1
        self.MAX_X = self.size.SCREEN_X / 2
        self.MAX_Y = self.size.SCREEN_Y / 2

    def get_player_pos_start(self):
        xcor = 0
        ycor = -self.MAX_Y + self.size.UNIT
        return (xcor, ycor)
