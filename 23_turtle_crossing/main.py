from game.main import Game

# TODO: Improve cars position logic,
#       sometimes cars are stacked together or
#       too close to each other


def app():
    game = Game()
    game.boot()
    while game.is_on:
        game.play()

    # Dev: Force game over
    print("Game is off !!")

    game.post_play()


app()
