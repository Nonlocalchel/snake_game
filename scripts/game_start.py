from src.pages.game.game import Game
from src.pages.game.infrastructure_game import InfrastructureGame

if __name__ == "__main__":
    game = Game(InfrastructureGame())
    game.loop()
