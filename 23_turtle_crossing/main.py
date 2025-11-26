from game.main import Game

# TODO: Better UX (text: Game Over)
# TODO: Player win scenario. (max level)
# TODO: Player score and persistent highscore.
#       Create a decreasing timer, and player score is based from
#       how quick player clear the level
# TODO: Documentation (docstring, flowchart, and readme.md)
# TODO: Final refactor

# Extra Features:
# - Better car movement logic,
#   now car moving in 2 directions.
# - Better car positioning logic,
#   now car wont stacks or too close to each other.
# - Improved UI/UX, visual road.
# - Better player movement, now with each move,
#   player is guaranteed can cross 1 line of road.
#   (better grid for player movement).
# - Better collision logic.
# - Restart mechanics.


def app():
    game = Game()
    game.boot()
    while game.is_on:
        game.play()

    game.post_play()


app()
