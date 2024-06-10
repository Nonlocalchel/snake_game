from .button import Button
from .input import Input

from src.logic.pages.actions import Action

from src.logic.app_elements.utils import figure_size, figure_positions, figure_real_pos


action_item = Button | Input


class Container:
    def __init__(self, elem_params: dict[action_item:Action | str], position: tuple[float, float],
                 size: tuple[float, float] = None, offset: tuple[float, float] = (0, 0)) -> None:
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

    def get_real_element_pos(self, element: any) -> tuple[float, float]:
        return figure_real_pos(self.pos, element.pos)

    def create_elements(self, elem_params: dict[str, Action | str], offset: tuple) -> dict[str, action_item]:
        elements = {}
        positions = figure_positions(self.size, elem_params, offset)

        for name, position in zip(elem_params, positions):
            if elem_params[name] == 'input':
                elements['input'] = Input('Введите имя', position)
                continue

            elements[name] = Button(name, elem_params[name], position)

        return elements
