from abc import abstractmethod

from src.logic.app_elements.elements.base.lock import Lock
from src.logic.app_elements.elements.base.element import Element

from src.logic.app_elements.elements.base.box import Box

from .utils import get_box_params, get_clickable_elements


class InteractionBox(Box, Lock):
    def __init__(self, *args, access=True, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        Lock.__init__(self, access=access)

    @abstractmethod
    def handle_input(self, key) -> None:
        pass

    @staticmethod
    @abstractmethod
    def add_elements() -> tuple[Element, ...]:
        pass

    @property
    def params(self):
        return get_box_params(self)

    @property
    def clickable_elements(self):
        return get_clickable_elements(self.elements)
