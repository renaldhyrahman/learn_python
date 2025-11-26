import time
import turtle as t

from .config import GameData
from .control_car import CarControl
from .display import Display
from .player import Player


class Game:
    def __init__(self):
        self.data = GameData(
            max_car=0,
            base_velocity=0,
            cur_velocity=0,
            cur_level=0,
            max_level=0,
            refresh_speed=0,
            player=None,
        )
        self.is_on = False

    def boot(self):
        self.data.max_car = 30
        self.data.base_velocity = self.data.screen.size.UNIT / 2
        self.data.max_level = 5
        self.data.refresh_speed = 0.1
        self.display = Display(self.data)
        self.car_control = CarControl(self.data)
        self.data.player = Player(self.data)
        self.game_restart()

    def game_restart(self):
        self.data.cur_velocity = self.data.base_velocity
        self.data.cur_level = 1
        self.car_control.reset()
        self.data.player.reset()
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

    def prompt_restart(self, is_win: bool):
        if self.display.ui_input.is_restart(is_win):
            self.game_restart()
        else:
            self.post_play()

    def game_over(self):
        self.is_on = False
        self.display.refresh()
        self.prompt_restart(is_win=False)

    def game_win(self):
        self.is_on = False
        self.display.refresh()
        self.prompt_restart(is_win=True)

    def post_play(self):
        t.bye()

    def level_up(self):
        player = self.data.player
        if player.ycor() >= self.data.screen.MAX_Y:
            if self.data.cur_level == 5:
                self.game_win()
                return
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
