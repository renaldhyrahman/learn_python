import time
import turtle as t

from control_car import CarControl
from game_config import Config
from player import Player


class Game:
    def __init__(self):
        self.config = Config()
        self.is_on = False

    def boot(self):
        t.colormode(255)
        self.game_speed = self.config.SPEED
        self.setup_screen()
        self.setup_player()
        self.cars = []
        self.setup_cars()
        self.keybinds()
        self.is_on = True

    def setup_screen(self):
        screen_width = self.config.size.SCREEN_X
        screen_height = self.config.size.SCREEN_Y
        self.screen = t.Screen()
        self.screen.setup(screen_width, screen_height)
        self.screen.bgcolor("black")
        self.screen.tracer(0)

    def setup_player(self):
        self.player = Player(self.config)

    def setup_cars(self):
        self.car_control = CarControl(self.config)

    def game_over(self):
        self.is_on = False

    def keybinds(self):
        move = self.player.movement
        self.screen.listen()
        self.screen.onkeypress(key="w", fun=lambda: move("n"))
        self.screen.onkeypress(key="a", fun=lambda: move("w"))
        self.screen.onkeypress(key="d", fun=lambda: move("e"))
        # Debug force exit
        self.screen.onkey(key="o", fun=self.game_over)

    def post_play(self):
        self.screen.exitonclick()

    def play(self):
        self.car_control.cars_mov()
        self.screen.update()
        self.player.lock_movement = False
        time.sleep(self.game_speed)
