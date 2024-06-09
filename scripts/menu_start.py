from src.logic.pages.menu.menu import Menu
from src.interface.infrastructure import Infrastructure

if __name__ == "__main__":
    menu = Menu(Infrastructure())
    menu.loop()