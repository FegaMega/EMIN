import Game, sys

def main():
    game = Game.Game()
    while game.isRunning == True:
        game.handleEvents()
        game.update()
        game.render()
    game.exit()
    return 0

sys.exit(main())