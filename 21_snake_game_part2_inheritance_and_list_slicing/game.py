import time
import turtle as t
from collections import namedtuple
from dataclasses import dataclass

from food import Food
from memory import Memory
from scoreboard import Scoreboard
from snake import Snake


@dataclass
class Highscore:
    index: int = 0
    data: dict = None


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
        self.memory = Memory(settings.memory_path)
        self.scoreboard = Scoreboard(self.WALL, self.OFFSETS)
        self.draw_border(self.WALL, self.OFFSETS.border)
        self.is_over = True
        self.direction_lock = False
        self.food_counter = 0
        self.keybind()
        self.game_speed = {
            "default": settings.game_speed,
            "current": settings.game_speed,
        }

    def reset(self):
        self.is_over = False
        self.food_counter = 0
        self.food.st()
        self.scoreboard.reset()
        self.snake.reset()
        self.food.spawn_food(self.snake.segments)
        self.game_speed["current"] = self.game_speed["default"]
        self.keybind()

    def post_game(self):
        self.save_highscore()
        self.snake.hide()
        self.food.ht()
        self.screen.update()
        self.scoreboard.update(True)
        self.input_restart()

    # Input_user
    def input_restart(self):
        ACCEPT = ["y", "yes"]
        REJECT = ["n", "no"]
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

    def input_highscore(self):
        input_user = t.textinput(
            "Highscore",
            "\nCongratulations! You are a top scorer." "\nType your name:",
        )
        if input_user is None:
            input_user = "Incognito"
        return input_user

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
        if not self.food_counter % 3 and self.game_speed["current"] >= 0.1:
            self.game_speed["current"] -= 0.05
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
            self.is_over = True

    def collision_body(self):
        segments_cor = []
        for i, s in enumerate(self.snake.segments):
            if not i:
                continue
            segments_cor.append(s.cor)
        segment_head = self.snake.head
        if segment_head.cor in segments_cor:
            self.is_over = True

    def create_highscore(self, index: int = 0):
        highscore = Highscore()
        highscore.index = 0
        highscore.data = {
            "score": self.scoreboard.score,
            "date": time.time(),
            "name": self.input_highscore(),
        }
        return highscore

    def is_highscore(self):
        histories = self.memory.read()
        if not histories or len(histories) < 5:
            return self.create_highscore()
        for history in histories:
            if self.scoreboard.score > history["score"]:
                return self.create_highscore()

    def save_highscore(self):
        highscore = self.is_highscore()
        if not highscore:
            return
        histories = self.memory.read()
        if len(histories) == 5:
            histories.pop()
        histories.append(highscore.data)
        histories_sorted = sorted(
            histories, key=lambda x: x["score"], reverse=True
        )
        self.memory.save(histories_sorted)

    # Keybinds
    def keybind(self):
        self.screen.listen()
        self.screen.onkey(key="Right", fun=lambda: self.head_direction("e"))
        self.screen.onkey(key="Up", fun=lambda: self.head_direction("n"))
        self.screen.onkey(key="Left", fun=lambda: self.head_direction("w"))
        self.screen.onkey(key="Down", fun=lambda: self.head_direction("s"))

    # Utils
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

    # Play
    def start(self):
        self.snake.move()
        self.collision_body()
        self.collision_wall()
        self.collision_food()
        self.screen.update()
        self.direction_lock = False
        time.sleep(self.game_speed["current"])
