from src.interface.infrastructure import Infrastructure
from src.pages.display import Display

from src.pages.actions import *


class Menu(Display):
    """Контролирует главный цикл игры"""

    def __init__(self, infrastructure: Infrastructure) -> None:
        self.infrastructure = infrastructure
        self.is_running = True
        self.elements = {'buttons': {}, 'inputs': {}}

    def process_events(self) -> None:
        """Обработка ввода от пользователя"""
        if self.infrastructure.is_quit_event():
            self.is_running = False
        if self.elements:
            self.infrastructure.check_position(self.elements)

    def update_state(self) -> None:
        self.infrastructure.update_and_tick()

    def render(self) -> None:
        """Обновление экрана: перерисовка меню"""
        self.infrastructure.fill_bg(image='gold_snake.jpg')

        buttons = self.elements['buttons']
        if not buttons:
            buttons = self.elements['buttons'] = self.infrastructure.get_buttons(
                {'Играть': say_hello, 'Cтатистика': say_hello, 'Выход': quit}
            )
        self.infrastructure.draw_menu(buttons)

    def loop(self):
        """Цикл меню"""
        while self.is_running:
            self.process_events()
            self.update_state()
            self.render()
        self.infrastructure.quit()
