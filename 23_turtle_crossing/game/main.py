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
            base_velocity=0,
            cur_velocity=0,
            cur_level=0,
            score=0,
            refresh_speed=0.1,
            player=None,
        )
        self.is_on = False

    def boot(self):
        self.data.base_velocity = self.data.screen.size.UNIT / 2
        self.display = Display(self.data)
        self.car_control = CarControl(self.data)
        self.data.player = Player(self.data)
        self.game_restart()

    def game_restart(self):
        self.car_control.reset()
        self.data.player.reset()
        self.keybinds()
        self.data.cur_level = 1
        self.data.cur_velocity = self.data.base_velocity
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
        self.display.refresh()
        is_restart = self.display.ui_input.is_restart()
        if is_restart:
            self.game_restart()

    def post_play(self):
        t.bye()

    def level_up(self):
        player = self.data.player
        if player.ycor() >= self.data.screen.MAX_Y:
            self.data.cur_level += 1
            self.data.cur_velocity += self.data.base_velocity
            player.reset()

    def is_player_car_collide(self):
        player = self.data.player
        collision_hit_box = 2 * self.data.screen.size.UNIT
        result = False
        for car in self.data.cars:
            is_player_on_road = True if player.ycor() == car.ycor() else False
            is_collide = (
                True
                if abs(car.xcor() - player.xcor()) < collision_hit_box
                else False
            )
            if is_player_on_road and is_collide:
                result = True
                break
        return result

    def play(self):
        self.car_control.cars_mov()
        self.level_up()
        self.display.refresh()
        if self.is_player_car_collide():
            self.game_over()
            return
        self.data.player.lock_movement = False
        time.sleep(self.data.refresh_speed)
