from collections import namedtuple

from game import Game

# BUG: make the ball do zigzag at certain angle with the paddle,
#      potentially `ball_collision_x` and all its chain,
#      is the cause, it can be triggered twice because ball did not
#      travel far enough after being hit, the result: `ball.bounce`
#      triggered more than one, which causing zigzag pattern.
#      Bug reproduce: move 2 taps from max_y (40 in distance)


Settings = namedtuple(
    "Settings", ["s_width", "s_height", "paddle_length", "size", "speed"]
)


def app():
    settings = Settings(
        s_width=800, s_height=600, paddle_length=5, size=20, speed=0.1
    )
    game = Game(settings)
    game.is_over = False
    while not game.is_over:
        game.play()
    game.screen.exitonclick()


app()
