from turtle import Turtle


class Player(Turtle):
    def __init__(self, data: object):
        self.data = data
        super().__init__(shape="turtle")
        self.seth(90)
        self.lock_movement = False
        self.reset()

    def movement(self, direction: str):
        if self.lock_movement:
            return
        distance = 2 * self.data.screen.size.UNIT
        xcor, ycor = {
            "n": (0, distance),
            "e": (distance, 0),
            "w": (-distance, 0),
        }[direction]
        self.goto((self.xcor() + xcor, self.ycor() + ycor))
        self.lock_movement = True

    def reset(self):
        self.ht()
        self.penup()
        self.speed(0)
        self.color("white")
        self.goto(self.data.screen.get_cor_player_start())
        self.st()
