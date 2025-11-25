import time
import turtle as t

from .config import Config
from .control_car import CarControl
from .display import Display
from .player import Player


class Game:
    def __init__(self):
        self.config = Config()
        self.is_on = False

    def boot(self):
        t.colormode(255)
        self.game_speed = self.config.SPEED
        self.display = Display(self.config)
        self.player = Player(self.config)
        self.cars = []
        self.car_control = CarControl(self.config)
        self.display.keybinds(self.player.movement, self.game_over)
        self.is_on = True

    def game_over(self):
        self.is_on = False

    def post_play(self):
        self.display.screen.exitonclick()

    def play(self):
        self.car_control.cars_mov()
        self.display.refresh()
        self.player.lock_movement = False
        time.sleep(self.game_speed)
