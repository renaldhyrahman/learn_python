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
        ycor = -self.MAX_Y + (self.size.UNIT * 2)
        return (xcor, ycor)

    def get_ui_level_cor(self):
        padding = 2 * self.size.UNIT
        xcor = -self.MAX_X + padding
        ycor = self.MAX_Y - padding
        return (xcor, ycor)

    def get_single_road_width(self):
        return 2 * self.size.UNIT

    def get_roads_ycor(self):
        single_road_width = self.get_single_road_width()
        double_road_width = 2 * single_road_width
        road_north = 2 * double_road_width  # double_road_width + padding
        road_mid = self.CORY_CENTER
        road_south = 2 * -double_road_width
        return [road_north, road_mid, road_south]


@dataclass
class GameData:
    max_car: int
    base_velocity: int
    cur_velocity: int
    refresh_speed: float
    cur_level: int
    score: int
    player: object
    cars: list = field(default_factory=list)
    screen: ScreenConfig = field(default_factory=ScreenConfig)
