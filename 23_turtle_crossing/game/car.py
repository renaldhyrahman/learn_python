import colorsys as cs
import random as r
from turtle import Turtle


class Car(Turtle):
    def __init__(self, data: object):
        self.data = data
        super().__init__(shape="square", visible=False)
        self.penup()
        self.shapesize(stretch_len=2)
        self.left(180)
        self.spawn()

    def spawn(self):
        self.goto(self.normalize_cor())
        self.color(self.random_color())
        self.st()

    def random_cor(self):
        offset = self.data.screen.size.UNIT
        offset_xcor = r.randint(2, 2 * self.data.max_car) * offset
        xcor = self.data.screen.MAX_X + offset_xcor
        ycor = r.choice(self.data.screen.get_roads_ycor())
        self.direction = r.choice([1, -1])
        if self.direction < 0:
            return (xcor, ycor - offset)
        return (-xcor, ycor + offset)

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

    def normalize_cor(self):
        if not self.data.cars:
            return self.random_cor()
        # Make sure there is enough space to squeze between cars
        # (car length is 2 units)
        min_distance = r.randint(3, 4) * self.data.screen.size.UNIT
        cars = self.data.cars
        while True:
            new_cor = self.random_cor()
            if all(car.distance(new_cor) >= min_distance for car in cars):
                return new_cor
        # for car in self.data.cars:
        #     while car.distance(new_cor) < min_distance:
        #         new_cor = self.random_cor()
        # return new_cor
