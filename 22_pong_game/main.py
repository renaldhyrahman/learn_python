from collections import namedtuple

from game import Game

# Create the screen
# Create and move a paddle
# Create another paddle
# Create the ball and make it move
# Detect collision with wall and bounce
# Detect collision with paddle
# Detect when paddle misses
# Keep score

Settings = namedtuple(
    "Settings", ["s_width", "s_height", "paddle_length", "size"]
)


def app():
    settings = Settings(s_width=800, s_height=600, paddle_length=5, size=20)
    game = Game(settings)
    game.is_over = False
    while not game.is_over:
        game.play()
    game.screen.exitonclick()


app()
