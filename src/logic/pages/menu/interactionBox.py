from abc import abstractmethod

from src.logic.app_elements.elements.base.lock import Lock
from src.logic.app_elements.elements.base.element import Element

from src.logic.app_elements.elements.base.container import Container


class InteractionContainer(Container, Lock):
    def __init__(self, *args, access=True, **kwargs):
        super().__init__(*args, **kwargs)
        Lock.__init__(self, access=access)

    @abstractmethod
    def handle_input(self, key):
        pass

    @staticmethod
    @abstractmethod
    def create_elements() -> tuple[Element, ...]:
        pass
