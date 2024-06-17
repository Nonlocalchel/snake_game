from .pages_collector import all_pages
from .playerHandle import PlayerHandle

from src.logic.pages.page import Page

from ..interface.infrastructure import Infrastructure


class SnakeApplication:
    def __init__(self, infrastructure: Infrastructure, start_page: str = 'menu') -> None:
        self.page_name = start_page
        self.player = PlayerHandle()
        self.infrastructure = infrastructure

    def launch(self) -> None:
        while True:
            page_class = all_pages[self.page_name]
            page = page_class(self.infrastructure)
            self.launch_page(page)

            if not page.is_running:
                quit()

    def launch_page(self, page: Page) -> None:
        self.set_page_player(page)

        page.loop()

        self.player = self.get_page_player(page)
        self.page_name = page.name

    def get_page_player(self, page: Page) -> PlayerHandle | None:
        if self.page_name == 'menu':
            return page.player

    def set_page_player(self, page: Page) -> None:
        if hasattr(page, 'player') and self.player:
            page.player = self.player
