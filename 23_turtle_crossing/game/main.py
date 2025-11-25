import time
import turtle as t

from .config import GameData
from .control_car import CarControl
from .display import Display
from .player import Player


class Game:
    def __init__(self):
        self.data = GameData(
            max_car=30,
            velocity_car=0,
            cur_level=1,
            score=0,
            cur_speed=0.1,
            player=None,
        )
        self.is_on = False

    def boot(self):
        t.colormode(255)
        self.data.velocity_car = self.data.screen.size.UNIT
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

    def level_up(self):
        player = self.data.player
        size_unit = self.data.screen.size.UNIT
        if player.ycor() >= self.data.screen.MAX_Y:
            self.data.cur_level += 1
            self.data.velocity_car += size_unit / 2
            player.restart()

    def check_collision(self):
        player_hit_box = self.data.player.pos()
        is_collide = False
        for car in self.data.cars:
            if car.distance(player_hit_box) < 40:
                is_collide = True
                break
        return is_collide

    def play(self):
        self.car_control.cars_mov()
        self.level_up()
        self.display.refresh()
        # is_collide = self.check_collision()
        # if is_collide:
        #     self.game_over()
        #     return
        self.data.player.lock_movement = False
        time.sleep(self.data.cur_speed)
