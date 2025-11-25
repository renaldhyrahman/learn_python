from game.main import Game

# TODO: Improve cars position logic,
#       sometimes cars are stacked together or
#       too close to each other
# TODO: Improve UI/UX, draw road
# TODO: Improve player movement and collision logic,
#       better grid
# TODO: Final refactor


def app():
    game = Game()
    game.boot()
    while game.is_on:
        game.play()

    game.post_play()


app()
