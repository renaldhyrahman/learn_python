import time
import turtle as t
from collections import namedtuple

from food import Food
from scoreboard import Scoreboard
from snake import Snake

Offsets = namedtuple("Offsets", ["wall", "border", "score", "info"])


class Game:
    def __init__(self, settings: object):
        self.SCREEN_SIZE = settings.screen_size
        self.SEGMENT_LENGTH = settings.segment_length
        self.OFFSETS = Offsets(
            wall=self.SEGMENT_LENGTH * 2,
            border=self.SEGMENT_LENGTH * 0.5,
            score=self.SEGMENT_LENGTH * 0.75,
            info=self.SEGMENT_LENGTH * 6,
        )
        self.WALL = (self.SCREEN_SIZE / 2) - self.OFFSETS.wall
        self.game_speed = settings.game_speed
        self.boot(settings)

    def boot(self, settings: object):
        self.screen = t.Screen()
        self.screen.tracer(0)
        self.screen.setup(width=self.SCREEN_SIZE, height=self.SCREEN_SIZE)
        self.screen.bgcolor("black")
        self.screen.title("Snake")
        self.snake = Snake(settings)
        self.food = Food(settings)
        self.food.spawn_food(self.snake.segments)
        self.scoreboard = Scoreboard(self.WALL, self.OFFSETS)
        self.draw_border(self.WALL, self.OFFSETS.border)
        self.is_over = True
        self.direction_lock = False
        self.food_counter = 0
        self.keybind()

    def reset(self):
        self.is_over = False
        self.food_counter = 0
        self.food.st()
        self.scoreboard.reset()
        self.snake.reset()
        self.food.spawn_food(self.snake.segments)
        self.keybind()

    def post_game(self):
        self.is_over = True
        self.snake.hide()
        self.food.ht()
        self.screen.update()
        self.scoreboard.update(True)

    def input_restart(self):
        ACCEPT = ["y", "yes"]
        REJECT = ["n", "no"]
        self.post_game()
        input_user = None
        while input_user not in ACCEPT + REJECT:
            input_user = t.textinput(
                "Game Over",
                "\nDo you want to restart? Type 'y' or 'n':",
            )
            if input_user is None:
                input_user = "n"
            else:
                input_user = input_user.strip().lower()
        if input_user in ACCEPT:
            self.reset()
        else:
            t.bye()

    # Game logic
    def head_direction(self, direction: str):
        if self.direction_lock:
            return
        segment_head = self.snake.head.segment
        current = segment_head.heading()
        new = {"e": 0, "n": 90, "w": 180, "s": 270}[direction]
        if abs(new - current) != 180:
            segment_head.seth(new)
            self.direction_lock = True

    def mechanics_level(self):
        if not self.food_counter % 3 and self.game_speed >= 0.1:
            self.game_speed -= 0.05
            self.scoreboard.level_increase()

    def collision_food(self):
        segment_head = self.snake.head.segment
        if self.food.distance(segment_head) < (0.75 * self.SEGMENT_LENGTH):
            self.food_counter += 1
            self.scoreboard.score_increase()
            self.mechanics_level()
            self.snake.segment_add(1)
            self.food.spawn_food(self.snake.segments)

    def collision_wall(self):
        xcor, ycor = self.snake.head.cor
        if abs(xcor) >= self.WALL or abs(ycor) >= self.WALL:
            self.post_game()

    # Game keybind
    def keybind(self):
        self.screen.listen()
        self.screen.onkey(key="Right", fun=lambda: self.head_direction("e"))
        self.screen.onkey(key="Up", fun=lambda: self.head_direction("n"))
        self.screen.onkey(key="Left", fun=lambda: self.head_direction("w"))
        self.screen.onkey(key="Down", fun=lambda: self.head_direction("s"))

    # Game utils
    def draw_border(self, wall: float, offset: float):
        border = wall + offset
        t_border = t.Turtle()
        t_border.ht()
        t_border.speed(0)
        t_border.color("white")
        t_border.penup()
        t_border.goto(-border, border)
        t_border.pendown()
        t_border.goto(border, border)
        t_border.goto(border, -border)
        t_border.goto(-border, -border)
        t_border.goto(-border, border)

    # Game loop
    def start(self):
        self.snake.move()
        self.collision_food()
        self.collision_wall()
        self.screen.update()
        self.direction_lock = False
        time.sleep(self.game_speed)
