from src.interface.infrastructure import Infrastructure
from src.pages.display import Display

from src.pages.actions import Action


class Statistic(Display):
    """Контролирует главный цикл игры"""

    def __init__(self, infrastracture: Infrastructure) -> None:
        pass

    def process_events(self) -> None:
        """Обработка ввода от пользователя"""
        pass

    def render(self) -> None:
        """Обновление экрана: перерисовка """
        pass

    def update_state(self) -> None:
        """Вычисление следующего состояния всех объектов на экране"""
        pass

    def loop(self):
        """Главный цикл игры"""
        pass
