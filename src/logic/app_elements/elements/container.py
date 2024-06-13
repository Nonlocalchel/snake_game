from .base.element import Element
from .base.lock import Lock

from src.logic.app_elements.utils import figure_size, figure_positions, figure_real_pos

from .button import Button
from .input import Input
from src.logic.pages.actions import Action

action_item = Button | Input


class Container(Element, Lock):
    def __init__(self, elem_params: dict[action_item:Action | str], position: tuple[float, float],
                 size: tuple[float, float] = None, offset: tuple[float, float] = (0, 0)) -> None:

        super().__init__(position)
        self.size = size or figure_size(elem_params)
        self.elements = self.set_elements_pos(elem_params, offset)
        self.pos = position

    def get_real_element_pos(self, element: any) -> tuple[float, float]:
        return figure_real_pos(self.pos, element.pos)

    def set_elements_pos(self, elements, offset):
        elements_dict = {}
        positions = figure_positions(self.size, elements, offset)

        for element, position in zip(elements, positions):
            elements_dict[element.text] = element
            elements_dict[element.text].pos = position

        return elements_dict
