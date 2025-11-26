from collections import namedtuple

from .game import Game

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
            game_speed=0.5,
            screen_size=600,
            memory_path="highscore.json",
        )
    )
    game.is_over = False
    while not game.is_over:
        game.start()
        if game.is_over:
            game.over()
