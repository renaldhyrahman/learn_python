import colorsys as cs
import random as r
from turtle import Turtle


class Car(Turtle):
    def __init__(self, config: object):
        self.config = config
        super().__init__(shape="square", visible=False)
        self.penup()
        self.shapesize(stretch_len=2)
        self.left(180)
        self.spawn()

    def spawn(self):
        self.goto(self.random_cor())
        self.color(self.random_color())
        self.st()

    def random_cor(self):
        axis_x = int(self.config.MAX_X)
        axis_y = int(self.config.MAX_Y)
        margin = self.config.size.UNIT * 5
        stop_x = (axis_x * 4) + 1
        start_y = -axis_y + margin
        stop_y = (axis_y - margin) + 1
        step = self.config.size.UNIT
        return (
            r.randrange(start=axis_x, stop=stop_x, step=step),
            r.randrange(start=start_y, stop=stop_y + 1, step=step),
        )

    # def normalize_cor(self, cars: list):
    #     pos_cars = []
    #     for car in cars:
    #         pos_cars.append(car.pos())

    def random_color(self):
        # hue
        h = r.random()
        # saturation; ensuring `light` color
        s = 1.0
        # lightness; ensuring result between 0.5 to 0.7
        l = r.uniform(0.5, 0.7)  # noqa E741
        _r, _g, _b = cs.hls_to_rgb(h, l, s)
        _r = int(_r * 255)
        _g = int(_g * 255)
        _b = int(_b * 255)
        return (_r, _g, _b)
