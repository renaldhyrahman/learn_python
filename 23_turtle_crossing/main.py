from game.main import Game


def app():
    game = Game()
    game.boot()
    while game.is_on:
        game.play()

    # Dev: Force game over
    print("Game is off !!")

    game.post_play()


app()
