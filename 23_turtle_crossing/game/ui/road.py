from turtle import Turtle


class UiRoad(Turtle):
    def __init__(self, data: object):
        self.data = data
        super().__init__(visible=True)
        self.speed(0)
        self.color("white")

    def draw_line(self, xcor_starts: int, xcor_ends: int, ycor: int):
        self.penup()
        self.goto(xcor_starts, ycor)
        self.pendown()
        self.goto(xcor_ends, ycor)

    def draw_dash(self, xcor_starts: int, xcor_ends: int, ycor: int):
        # Dash length is half of unit size
        dash_length = self.data.screen.size.UNIT / 2
        self.penup()
        self.goto(xcor_starts, ycor)
        while self.xcor() >= xcor_ends:
            self.pendown()
            self.goto((self.xcor() - dash_length, ycor))
            self.penup()
            self.goto((self.xcor() - dash_length, ycor))

    def draw_road(self, ycor: int):
        road_width = self.data.screen.get_single_road_width()
        max_x = self.data.screen.MAX_X
        self.draw_line(max_x, -max_x, ycor + road_width)
        self.draw_dash(max_x, -max_x, ycor)
        self.draw_line(max_x, -max_x, ycor - road_width)

    def draw_roads(self):
        for ycor in self.data.screen.get_roads_ycor():
            self.draw_road(ycor)
