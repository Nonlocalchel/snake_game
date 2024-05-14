from abc import ABC, abstractmethod
from src.interface.infrastructure import Infrastructure


class Display(ABC):
    """Контролирует главный цикл игры"""

    @abstractmethod
    def __init__(self, infrastracture: Infrastructure) -> None:
        pass

    @abstractmethod
    def process_events(self) -> None:
        """Обработка ввода от пользователя"""
        pass

    @abstractmethod
    def render(self) -> None:
        """Обновление экрана: перерисовка змейки, яблока, баллов и game over"""
        pass

    @abstractmethod
    def update_state(self) -> None:
        """Вычисление следующего состояния всех объектов на экране"""
        pass

    @abstractmethod
    def loop(self):
        """Главный цикл игры"""
        pass
