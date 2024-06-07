from src.settings import *
from math import ceil

symbols = []


def scale(value: int, cof: int | float = 1) -> int:
    return int(value * cof * SCALE)


def figure_font() -> int:
    return ceil(SCALE / 1.2)


def get_scale_radius(scale_cof: int = 4) -> int:
    return RADIUS * scale_cof


def figure_abs_params(x, y):
    return scale(WIDTH, x), scale(HEIGHT, y)


def figure_center(dx: int, dy: int) -> tuple:
    center_x, center_y = figure_abs_params(0.5, 0.5)
    return center_x + dx, center_y + dy


def figure_image_size(image_h: int, image_w: int) -> tuple:
    if image_h > image_w:
        cof = image_h / image_w
        return scale(WIDTH), scale(HEIGHT, cof)
    else:
        cof = image_w / image_h
        return scale(WIDTH, cof), scale(HEIGHT)


def filter_key(const_dict: dict) -> dict:
    filter_storage = filter(lambda x: x[0].startswith('K_'), const_dict.items())
    return dict(filter_storage)


pressed_cash = []


def is_tab_number(key: str) -> bool:
    return key.startswith('[') and key.endswith(']')


def shift_in(place):
    return 'left shift' in place


def correct_input(pressed_keys: list, to_up=False) -> str:
    symbol = pressed_keys[0]

    if to_up:
        symbol = pressed_keys[-1].upper()

    if symbol and is_tab_number(symbol):
        symbol = symbol[1]

    return symbol

