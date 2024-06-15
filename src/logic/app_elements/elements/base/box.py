from src.logic.app_elements.elements.base.element import Element
from src.logic.app_elements.elements.base.lock import Lock

from src.logic.app_elements.elements.base.utils import figure_size, figure_positions, figure_real_pos

from src.logic.pages.actions import Action


class Box(Element, Lock):
    def __init__(self, position: tuple[float, float], elements: tuple = (),
                 size: tuple[float, float] = None, offset: tuple[float, float] = (0, 0)) -> None:
        super().__init__(position)
        self.size = size or figure_size(elements)
        self.elements = elements
        self.offset = offset
        self.set_elements_pos()

    def add_elements(self, *new_elements: Element) -> None:
        self.elements += tuple(new_elements)

        if not self.size:
            self.size = figure_size(self.elements)

        self.set_elements_pos()

    def set_elements_pos(self) -> None:
        offset = self.offset
        elements = self.elements
        size = self.size
        positions = figure_positions(size, elements, offset)

        for element, position in zip(elements, positions):
            element.pos = position

    def get_real_element_pos(self, element: any) -> tuple[float, float]:
        return figure_real_pos(self.pos, element.pos)
