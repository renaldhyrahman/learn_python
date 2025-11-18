from dataclasses import dataclass

from game import Game

# TODO: Body collision
# TODO: Generate food + random placing
# (need body detection, not placing food on current body)
# TODO: Increase body count after eat food
# TODO: Display score
# TODO: Restart Mechanics
# TODO: Persistent personal high-score
# TODO: Level mechanics
# (snake move faster after eat certain amount of food)
# TODO: Refactor
# BUG: sometimes, snake can do u-turn when2 keys are pressed at same time


@dataclass
class Settings:
    segment_length: int = 0
    segment_count: int = 0
    game_speed: float = 0
    screen_size: int = 0


def app():
    settings = Settings(
        segment_length=20, segment_count=3, game_speed=0.2, screen_size=600
    )
    game = Game(settings)
    game.is_over = False
    while not game.is_over:
        game.start()
    game.screen.exitonclick()


app()
