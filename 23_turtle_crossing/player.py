from turtle import Turtle


class Player(Turtle):
    def __init__(self, config: object):
        super().__init__(shape="turtle", visible=False)
        self.config = config
        self.penup()
        self.left(90)
        self.speed(0)
        self.color("white")
        self.goto(self.config.get_player_pos_start())
        self.st()

    def movement(self, direction: str):
        distance = self.config.size.UNIT
        xcor, ycor = {
            "n": (0, distance),
            "e": (distance, 0),
            "w": (-distance, 0),
        }[direction]
        self.goto((self.xcor() + xcor, self.ycor() + ycor))
        print(self.pos())
