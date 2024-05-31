from .button import Button
from .input import Input

from .utils import figure_size, figure_positions


class GameMenu:
    def __init__(self, elem_params: dict, position: tuple, size: tuple = None, offset: tuple = (0, 0)) -> None:
        self.size = size or figure_size(elem_params)
        self.elements = self.__create_elements(elem_params, offset)
        self.__position = position
        self.__access = True

    @property
    def pos(self):
        return self.__position

    @property
    def params(self):
        params = {
                    'frame': {
                        'position': self.pos,
                        'size': self.size
                    },
                    'elements': {element.text: element.pos for element in self.elements}
                }
        return params

    @property
    def get_lock(self) -> bool:
        return not self.__access

    def lock(self) -> None:
        self.__access = False

    def unlock(self) -> None:
        self.__access = True

    def __create_elements(self, elem_params: dict, offset: tuple) -> dict:
        elements = {}
        positions = figure_positions(self.size, elem_params, offset)

        for name, position in zip(elem_params, positions):
            if elem_params[name] == 'input':
                elements[name] = Input(name, position)
                continue

            elements[name] = Button(name, elem_params[name], position)

        return elements
