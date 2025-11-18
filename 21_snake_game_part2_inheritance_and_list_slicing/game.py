import time
from turtle import Screen

from snake import Snake


class Game:
    def __init__(self, settings: object):
        self.screen = Screen()
        self.screen_size = settings.screen_size
        self.wall = (settings.screen_size / 2) - settings.segment_length
        self.game_speed = settings.game_speed
        self.snake = Snake(settings)
        self.boot()
        self.score = 0

    # Game logic
    def head_direction(self, direction: str):
        segment_head = self.snake.head.segment
        current = segment_head.heading()
        new = {"e": 0, "n": 90, "w": 180, "s": 270}[direction]
        if abs(new - current) != 180:
            segment_head.seth(new)

    def is_hit_wall(self):
        xcor, ycor = self.snake.head.cor
        if abs(xcor) >= self.wall or abs(ycor) >= self.wall:
            return True
        return False

    def increase_speed(self):
        if self.game_speed < 0.1:
            return
        self.game_speed -= 0.05

    # Game keybind
    def keybind(self):
        self.screen.listen()
        self.screen.onkey(key="Right", fun=lambda: self.head_direction("e"))
        self.screen.onkey(key="Up", fun=lambda: self.head_direction("n"))
        self.screen.onkey(key="Left", fun=lambda: self.head_direction("w"))
        self.screen.onkey(key="Down", fun=lambda: self.head_direction("s"))
        # Debug: manual add segment
        self.screen.onkey(
            key="a", fun=lambda: self.snake.add_segment(1, False)
        )
        # Debug: manual increase speed
        self.screen.onkey(key="s", fun=self.increase_speed)

    def boot(self):
        self.screen.setup(width=self.screen_size, height=self.screen_size)
        self.screen.bgcolor("black")
        self.screen.title("Snake")
        self.screen.tracer(0)
        self.is_over = True
        self.keybind()

    def start(self):
        time.sleep(self.game_speed)
        self.snake.move()
        self.screen.update()
        if self.is_hit_wall():
            self.is_over = True
