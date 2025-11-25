import time
import turtle as t

from .config import GameData
from .control_car import CarControl
from .display import Display
from .player import Player


class Game:
    def __init__(self):
        self.data = GameData(
            max_car=20, cur_level=1, score=0, cur_speed=0.1, player=None
        )
        self.is_on = False

    def boot(self):
        t.colormode(255)
        self.display = Display(self.data)
        self.data.player = Player(self.data)
        self.car_control = CarControl(self.data)
        self.keybinds()
        self.is_on = True

    def keybinds(self):
        self.display.screen.listen()
        screen = self.display.screen
        player_move = self.data.player.movement
        screen.onkeypress(key="w", fun=lambda: player_move("n"))
        screen.onkeypress(key="a", fun=lambda: player_move("w"))
        screen.onkeypress(key="d", fun=lambda: player_move("e"))
        # Debug force exit
        screen.onkey(key="o", fun=self.game_over)

    def game_over(self):
        self.is_on = False

    def post_play(self):
        self.display.screen.exitonclick()

    def play(self):
        self.car_control.cars_mov()
        self.display.refresh()
        self.data.player.lock_movement = False
        time.sleep(self.data.cur_speed)
