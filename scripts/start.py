from src.logic.snakeApplication import SnakeApplication
from src.interface.infrastructure import Infrastructure

if __name__ == "__main__":
    snake_app = SnakeApplication(Infrastructure())
    snake_app.launch()
