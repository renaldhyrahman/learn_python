import time
import turtle as t

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard


class Game:
    def __init__(self, settings):
        self.MAX_X = 0.5 * settings.s_width
        self.MAX_Y = 0.5 * settings.s_height
        self.SIZE = settings.size
        self.DEFAULT_SPEED = settings.speed
        self.PADDLE_LENGTH = settings.paddle_length
        self.PADDLE_OFFSET = 0.5 * self.PADDLE_LENGTH * self.SIZE
        self.PADDLE_COR_X = self.MAX_X - self.PADDLE_OFFSET
        self.OFFSET_X = self.MAX_X - self.PADDLE_COR_X + (1.5 * self.SIZE)
        self.GREEN_X = self.MAX_X - self.OFFSET_X
        self.boot()

    def boot(self):
        self.screen = t.Screen()
        self.screen.title("Pong")
        self.screen.setup(self.MAX_X * 2, self.MAX_Y * 2)
        self.screen.bgcolor("black")
        self.screen.tracer(0)
        self.scoreboard = Scoreboard()
        self.paddle_l = Paddle(self.PADDLE_LENGTH, -self.PADDLE_COR_X)
        self.paddle_r = Paddle(self.PADDLE_LENGTH, self.PADDLE_COR_X)
        self.ball = Ball(self.SIZE, self.MAX_X, self.MAX_Y)
        self.is_over = True
        self.cur_speed = self.DEFAULT_SPEED
        self.keybinds()

    def move_paddle(self, direction: str, obj_paddle: Paddle):
        distance = {"n": self.SIZE, "s": -self.SIZE}[direction]
        paddle_y_green = self.MAX_Y - (2 * self.SIZE)
        if abs(obj_paddle.ycor() + distance) < paddle_y_green:
            obj_paddle.fd(distance)

    def keybinds(self):
        self.screen.listen()
        self.screen.onkeypress(
            key="Up", fun=lambda: self.move_paddle("n", self.paddle_r)
        )
        self.screen.onkeypress(
            key="Down", fun=lambda: self.move_paddle("s", self.paddle_r)
        )
        self.screen.onkeypress(
            key="w", fun=lambda: self.move_paddle("n", self.paddle_l)
        )
        self.screen.onkeypress(
            key="s", fun=lambda: self.move_paddle("s", self.paddle_l)
        )

    def ball_collision_y(self):
        wall = self.MAX_Y - self.SIZE
        if abs(self.ball.ycor()) > wall:
            self.ball.bounce("y")

    def is_ball_near_paddle(self, paddle: Paddle):
        return self.ball.distance(paddle) < self.PADDLE_OFFSET

    def is_ball_collision_paddle(self, paddle: Paddle):
        is_passing_green_zone = abs(self.ball.xcor()) > self.GREEN_X
        return self.is_ball_near_paddle(paddle) and is_passing_green_zone

    def ball_collision_x(self, paddle_r: Paddle, paddle_l: Paddle):
        collision_r = self.is_ball_collision_paddle(paddle_r)
        collision_l = self.is_ball_collision_paddle(paddle_l)
        if collision_r or collision_l:
            self.ball.bounce("x")
            if self.cur_speed > self.DEFAULT_SPEED / 4:
                self.cur_speed -= self.DEFAULT_SPEED / 5
            print(self.cur_speed)

    def observer_score(self):
        if self.ball.xcor() > (self.MAX_X - self.SIZE):
            self.reset_speed()
            self.scoreboard.score_increase("l")
            self.ball.reset()
        if self.ball.xcor() < (-self.MAX_X + self.SIZE):
            self.reset_speed()
            self.scoreboard.score_increase("r")
            self.ball.reset()

    def reset_speed(self):
        self.cur_speed = self.DEFAULT_SPEED

    def play(self):
        self.ball.move()
        self.ball_collision_y()
        self.ball_collision_x(self.paddle_r, self.paddle_l)
        self.observer_score()
        self.screen.update()
        time.sleep(self.cur_speed)
