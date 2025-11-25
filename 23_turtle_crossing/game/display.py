import turtle as t
from typing import Callable


class Display:
    def __init__(self, config: object):
        self.screen = t.Screen()
        self.screen.setup(
            width=config.size.SCREEN_X, height=config.size.SCREEN_Y
        )
        self.screen.bgcolor("black")
        self.screen.tracer(0)

    def refresh(self):
        self.screen.update()

    def keybinds(
        self, player_move: Callable[[str], None], game_over: Callable[[], None]
    ):
        self.screen.listen()
        self.screen.onkeypress(key="w", fun=lambda: player_move("n"))
        self.screen.onkeypress(key="a", fun=lambda: player_move("w"))
        self.screen.onkeypress(key="d", fun=lambda: player_move("e"))
        # Debug force exit
        self.screen.onkey(key="o", fun=game_over)
