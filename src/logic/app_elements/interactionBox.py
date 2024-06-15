from abc import abstractmethod

from src.logic.app_elements.base import Lock
from src.logic.app_elements.base import Box


class InteractionBox(Box, Lock):
    def __init__(self, *args, access=True, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        Lock.__init__(self, access=access)

    @property
    def clickable_elements(self):
        filtered_iter = filter(self.is_clickable, self.elements)
        return list(filtered_iter)

    @abstractmethod
    def handle_input(self, key) -> None:
        pass

    @abstractmethod
    def put_elements(self) -> None:
        pass

    @staticmethod
    def is_clickable(element: any) -> bool:
        return hasattr(element, 'is_hover')