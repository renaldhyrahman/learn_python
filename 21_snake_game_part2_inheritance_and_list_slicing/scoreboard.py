from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, wall: float, offsets: tuple):
        super().__init__()
        self.SCORE_COR = (0, wall + offsets.score)
        self.SCORE_FONT = ("Courier", 12, "bold")
        self.INFO_COR = (0, wall - offsets.info)
        self.INFO_FONT = ("Courier", 36, "bold")
        self.ALIGNMENT = "center"
        self.ht()
        self.color("white")
        self.penup()
        self.reset()

    def update(self, is_game_over: bool = False):
        self.clear()
        text = f"Level: {self.level}    |    Score: {self.score}"
        self.goto(self.SCORE_COR)
        self.write(
            text,
            move=False,
            align=self.ALIGNMENT,
            font=self.SCORE_FONT,
        )
        if is_game_over:
            text = "GAME OVER"
            self.goto(self.INFO_COR)
            self.write(
                text,
                move=False,
                align=self.ALIGNMENT,
                font=self.INFO_FONT,
            )

    def score_increase(self):
        self.score += 1 * self.level
        self.update()

    def level_increase(self):
        self.level += 1
        self.update()

    def reset(self):
        self.score = 0
        self.level = 1
        self.update()
