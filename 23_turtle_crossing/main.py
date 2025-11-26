from game.game import Game

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
# - Player win condition. (max level)


def app():
    game = Game()
    game.boot()
    while game.is_on:
        game.play()


app()
