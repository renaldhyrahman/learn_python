from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.penup()
        self.FONT = ("Courier", 48, "bold")
        self.COR = (0, 200)
        self.score_l = 0
        self.score_r = 0
        self.update()

    def update(self):
        self.clear()
        self.color("white")
        self.goto(self.COR)
        text = f"{self.score_l}  |  {self.score_r}"
        self.write(text, move=True, align="center", font=self.FONT)

    def score_increase(self, l_or_r: str):
        if l_or_r == "l":
            self.score_l += 1
        if l_or_r == "r":
            self.score_r += 1
        self.update()
