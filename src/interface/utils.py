from src.settings import *
from math import ceil

digit = int | float


def scale(value: int, cof: int | float = 1) -> int:
    return int(value * cof * SCALE)


def figure_font() -> int:
    return ceil(SCALE / 1.2)


def get_scale_radius(scale_cof: int = 4) -> int:
    return RADIUS * scale_cof


def figure_abs_params(x: digit, y: digit) -> tuple[digit, digit]:
    return scale(WIDTH, x), scale(HEIGHT, y)


def figure_center(dx: int, dy: int) -> tuple[digit, digit]:
    center_x, center_y = figure_abs_params(0.5, 0.5)
    return center_x + dx, center_y + dy


def figure_image_size(image_h: int, image_w: int) -> tuple[digit, digit]:
    if image_h > image_w:
        cof = image_h / image_w
        return scale(WIDTH), scale(HEIGHT, cof)
    else:
        cof = image_w / image_h
        return scale(WIDTH, cof), scale(HEIGHT)


def filter_key(const_dict: dict) -> dict:
    filter_storage = filter(lambda x: x[0].startswith('K_'), const_dict.items())
    return dict(filter_storage)


def increase_size(size: tuple[int, int]) -> tuple[digit, digit]:
    width, height = size
    return width + 20, height + 20


def figure_inner_pos(inner_size: tuple[int, int], outer_size: tuple[int, int]) -> tuple[int, int]:
    new_width, new_height = outer_size
    width, height = inner_size
    return (new_width-width)//2, (new_height-height)//2


pressed_cash = []


def is_tab_number(key: str) -> bool:
    return key.startswith('[') and key.endswith(']')


def shift_in(place):
    return 'left shift' in place


def correct_input(pressed_keys: list[str], to_up=False) -> str:
    symbol = pressed_keys[0]

    if to_up and len(symbol) == 1:
        symbol = pressed_keys[-1].upper()

    if symbol and is_tab_number(symbol):
        symbol = symbol[1]

    return symbol
