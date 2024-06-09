from src.logic.page import pages
from src.interface.infrastructure import Infrastructure

if __name__ == "__main__":
    page_name = 'menu'
    action = 'play'
    player = None

    while True:
        page_class = pages[page_name]
        page = page_class(Infrastructure())
        if hasattr(page, 'player') and player:
            page.player = player

        page.loop()

        if not page.is_running:
            quit()

        page_name = page.name
        if hasattr(page, 'player'):
            player = page.player

