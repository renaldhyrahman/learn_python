from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, length: int, cor_x: float):
        super().__init__(shape="square", visible=False)
        self.speed(0)
        self.color("white")
        self.shapesize(stretch_len=length, stretch_wid=1)
        self.left(90)
        self.penup()
        self.setpos(cor_x, 0)
        self.st()
