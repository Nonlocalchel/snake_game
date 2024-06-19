from src.logic.snakeApp import SnakeApp
from src.interface.infrastructure import Infrastructure

if __name__ == "__main__":
    snake_app = SnakeApp(Infrastructure())
    snake_app.launch()
