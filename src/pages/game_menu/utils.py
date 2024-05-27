from .gameMenu import GameMenu
from .button import Button


def figure_size(elements: dict):
    el_count = len(elements)
    height = el_count * 0.2
    width = (el_count * 0.2) - 0.1
    return width, height


def figure_padding(size, elements: dict) -> int | float:
    height = size[1]
    return height // (len(elements) + 1)


def figure_pos(size, y: int | float, offset: tuple) -> tuple:
    width = size[0]
    dw, dh = offset
    return (width // 2) + dw, y + dh


