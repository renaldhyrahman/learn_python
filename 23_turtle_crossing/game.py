import time
import turtle as t

from car import Car
from game_config import Config
from player import Player


class Game:
    def __init__(self):
        self.config = Config()
        self.is_on = False

    def boot(self):
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
        self.max_cars = 40
        for _ in range(self.max_cars):
            self.cars.append(Car(self.config))

    def logic_cars(self):
        padding = self.config.size.UNIT * 2
        max_x = self.config.MAX_X + padding
        for i, car in enumerate(self.cars):
            car.fd(self.config.size.UNIT)
            if car.xcor() < -max_x:
                del self.cars[i]
            if len(self.cars) < self.max_cars:
                self.cars.append(Car(self.config))

    def turn_off(self):
        self.is_on = False

    def keybinds(self):
        move = self.player.movement
        self.screen.listen()
        self.screen.onkeypress(key="w", fun=lambda: move("n"))
        self.screen.onkeypress(key="a", fun=lambda: move("w"))
        self.screen.onkeypress(key="d", fun=lambda: move("e"))
        # Debug force exit
        self.screen.onkey(key="o", fun=self.turn_off)

    def post_play(self):
        self.screen.exitonclick()

    def play(self):
        self.logic_cars()
        self.screen.update()
        time.sleep(self.game_speed)
