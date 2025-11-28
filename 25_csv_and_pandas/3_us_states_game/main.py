from game.game import Game


def app():
    game = Game()
    while game.is_on:
        game.play()


app()
