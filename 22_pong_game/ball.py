from turtle import Turtle


class Ball(Turtle):
    def __init__(self, size: int, max_x: float, max_y: float):
        super().__init__(shape="circle", visible=False)
        self.SIZE = size
        self.MAX_X = max_x
        self.MAX_Y = max_y
        self.move_x = 0.5 * self.SIZE
        self.move_y = 0.5 * self.SIZE
        self.color("white")
        self.penup()
        self.st()

    def move(self):
        self.goto(
            (
                self.xcor() + self.move_x,
                self.ycor() + self.move_y,
            )
        )

    def bounce(self, axis: str):
        if axis == "x":
            self.move_x *= -1
        if axis == "y":
            self.move_y *= -1
