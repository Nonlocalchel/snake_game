from src.pages.game.game import Game
from src.interface.infrastructure import Infrastructure

if __name__ == "__main__":
    game = Game(Infrastructure())
    game.loop()
