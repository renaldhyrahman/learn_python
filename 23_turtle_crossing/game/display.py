import turtle as t

from game.ui.road import UiRoad
from game.ui.text import UiText


class Display(t.Turtle):
    def __init__(self, data: object):
        self.data = data
        self.screen = t.Screen()
        self.screen.setup(
            width=self.data.screen.size.SCREEN_X,
            height=self.data.screen.size.SCREEN_Y,
        )
        self.screen.title("Turtle Crossing")
        self.screen.bgcolor("black")
        self.ui_text = UiText(self.data)
        self.ui_road = UiRoad(self.data)
        self.screen.tracer(0)
        self.ui_road.draw_roads()

    def refresh(self):
        self.ui_text.refresh()
        self.screen.update()
