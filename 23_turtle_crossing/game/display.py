import turtle as t

from game.ui.level import UiLevel
from game.ui.road import UiRoad


class Display(t.Turtle):
    def __init__(self, data: object):
        self.data = data
        self.screen = t.Screen()
        self.screen.setup(
            width=self.data.screen.size.SCREEN_X,
            height=self.data.screen.size.SCREEN_Y,
        )
        self.screen.bgcolor("black")
        self.ui_level = UiLevel(self.data)
        self.ui_road = UiRoad(self.data)
        self.screen.tracer(0)
        self.ui_road.draw_roads()

    def refresh(self):
        self.ui_level.refresh()
        self.screen.update()
