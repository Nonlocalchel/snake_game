from .logic.page import pages
from .logic.playerHandle import PlayerHandle

from .interface.infrastructure import Infrastructure


class SnakeApplication:
    def __init__(self, start_page: str = 'menu', player: PlayerHandle = PlayerHandle()) -> None:
        self.infrastructure = Infrastructure()
        self.page_name = start_page
        self.player = player

    def launch(self):
        while True:
            page_class = pages[self.page_name]
            page = page_class(self.infrastructure)
            self.launch_page(page)

            if not page.is_running:
                quit()

    def launch_page(self, page):
        self.set_page_player(page)

        page.loop()

        self.player = self.get_page_player(page)
        self.page_name = page.name

    def get_page_player(self, page):
        if self.page_name == 'menu':
            return page.player
        else:
            return

    def set_page_player(self, page):
        if hasattr(page, 'player') and self.player:
            page.player = self.player
