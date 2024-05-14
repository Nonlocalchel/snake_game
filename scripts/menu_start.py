from src.pages.game_menu.menu import Menu
from src.pages.game_menu.infrastructure_menu import InfrastructureMenu

if __name__ == "__main__":
    menu = Menu(InfrastructureMenu())
    menu.loop()
