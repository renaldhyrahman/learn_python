import time
import turtle as t

from ball import Ball
from paddle import Paddle


class Game:
    def __init__(self, settings):
        self.MAX_X = 0.5 * settings.s_width
        self.MAX_Y = 0.5 * settings.s_height
        self.SIZE = settings.size
        self.PADDLE_LENGTH = settings.paddle_length
        self.PADDLE_OFFSET = 0.5 * self.PADDLE_LENGTH * self.SIZE
        self.PADDLE_COR_X = self.MAX_X - self.PADDLE_OFFSET
        self.OFFSET_X = self.MAX_X - self.PADDLE_COR_X + (1.5 * self.SIZE)
        self.boot()

    def boot(self):
        self.screen = t.Screen()
        self.screen.title("Pong")
        self.screen.setup(self.MAX_X * 2, self.MAX_Y * 2)
        self.screen.bgcolor("black")
        self.screen.tracer(0)
        self.paddle_l = Paddle(self.PADDLE_LENGTH, -self.PADDLE_COR_X)
        self.paddle_r = Paddle(self.PADDLE_LENGTH, self.PADDLE_COR_X)
        self.ball = Ball(self.SIZE, self.MAX_X, self.MAX_Y)
        self.is_over = True
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
        ball_ycor = self.ball.ycor()
        wall_top = self.MAX_Y - self.SIZE
        wall_bot = -self.MAX_Y + self.SIZE
        if (ball_ycor > wall_top) or (ball_ycor < wall_bot):
            self.ball.bounce("y")

    def is_hit_paddle(self, paddle: Paddle):
        return self.ball.distance(paddle) < self.PADDLE_OFFSET

    def ball_collision_x(self, paddle_r: Paddle, paddle_l: Paddle):
        ball_xcor = self.ball.xcor()
        green_zone = self.MAX_X - self.OFFSET_X
        collision_r = self.is_hit_paddle(paddle_r) and ball_xcor > green_zone
        collision_l = self.is_hit_paddle(paddle_l) and ball_xcor < -green_zone
        if collision_r or collision_l:
            self.ball.bounce("x")

    def play(self):
        self.ball.move()
        self.ball_collision_y()
        self.ball_collision_x(self.paddle_r, self.paddle_l)
        self.screen.update()
        time.sleep(0.1)
        # print(self.PADDLE_OFFSET)  # 50.0
        # print(self.PADDLE_COR_X)  # 350
        # print(self.OFFSET_X)  # 80.0
        # print(self.MAX_X - self.OFFSET_X)  # 320.0
