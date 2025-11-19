from collections import namedtuple

from game import Game

# Main feature
# - Movement and control
# - Wall collision
# - Food collision
# TODO: Body collision
# TODO:
# TODO: Refactor and docstring
# Extra features:
# - Improved UX
#   (display 'wall', better visualization of snake
#   (segmented exoskeleton) to see how long your snake is)
# - Level mechanics
#   (snake move faster after consuming certain amount of food)
# - Better scoring
#   (more levels equal to more score)
# - Restart mechanics
# - Better food placement
#   (food will not spawn exactly where the snake is)
# - Persistent high-score


Settings = namedtuple(
    "Settings",
    [
        "segment_length",
        "segment_count",
        "game_speed",
        "screen_size",
        "memory_path",
    ],
)


def app():
    game = Game(
        Settings(
            segment_length=20,
            segment_count=3,
            game_speed=0.3,
            screen_size=600,
            memory_path="highscore.json",
        )
    )
    game.is_over = False
    while not game.is_over:
        game.start()
        if game.is_over:
            game.post_game()


app()
