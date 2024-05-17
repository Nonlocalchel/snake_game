from src.interface.infrastructure import Infrastructure
from src.pages.display import Display

from src.pages.actions import *


class Menu(Display):
    """Контролирует главный цикл игры"""

    def __init__(self, infrastructure: Infrastructure) -> None:
        self.infrastructure = infrastructure
        self.is_running = True

    def process_events(self) -> None:
        """Обработка ввода от пользователя"""
        if self.infrastructure.is_quit_event():
            self.is_running = False
        self.infrastructure.check_position()

    def update_state(self) -> None:
        self.infrastructure.update_and_tick()

    def render(self) -> None:
        """Обновление экрана: перерисовка меню"""
        self.infrastructure.fill_bg(image='gold_snake.jpg')
        self.infrastructure.draw_menu({'Играть': say_hello, 'Cтатистика': say_hello, 'Выход': quit})

    def loop(self):
        """Цикл меню"""
        while self.is_running:
            self.process_events()
            self.update_state()
            self.render()
        self.infrastructure.quit()
