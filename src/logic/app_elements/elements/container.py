from .button import Button
from .input import Input

from src.logic.app_elements.utils import figure_size, figure_positions, figure_real_pos


class Container:
    def __init__(self, elem_params: dict, position: tuple, size: tuple = None, offset: tuple = (0, 0)) -> None:
        self.size = size or figure_size(elem_params)
        self.elements = self.create_elements(elem_params, offset)
        self.pos = position
        self.__access = True

    @property
    def get_lock(self) -> bool:
        return not self.__access

    def lock(self) -> None:
        self.__access = False

    def unlock(self) -> None:
        self.__access = True

    def get_real_element_pos(self,element):
        return figure_real_pos(self.pos, element.pos)

    def create_elements(self, elem_params: dict, offset: tuple) -> dict:
        elements = {}
        positions = figure_positions(self.size, elem_params, offset)

        for name, position in zip(elem_params, positions):
            if elem_params[name] == 'input':
                elements['input'] = Input('Введите имя', position)
                continue

            elements[name] = Button(name, elem_params[name], position)

        return elements
