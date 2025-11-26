from turtle import Turtle


class UiText(Turtle):
    def __init__(self, data: object):
        self.data = data
        super().__init__(visible=False)
        self.FONT = ("Courier", 12, "bold")
        self.ALIGN = "left"
        self.color("white")
        self.penup()

    def refresh(self):
        cor = self.data.screen.get_ui_level_cor()
        self.clear()
        text = f"Level: {self.data.cur_level}"
        self.goto(cor)
        self.write(text, align=self.ALIGN, font=self.FONT)
