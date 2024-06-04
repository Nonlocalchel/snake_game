from src.constant import *
from math import ceil

symbols = []


def scale(value: int, cof: int | float) -> int:
    return int(value * cof * SCALE)


def figure_font() -> int:
    return ceil(SCALE / 1.2)


def get_scale_radius(scale_cof: int = 4) -> int:
    return RADIUS * scale_cof


def scale_coord(x, y):
    return scale(WIDTH, x), scale(HEIGHT, y)


def figure_center(dx: int, dy: int) -> tuple:
    center_x, center_y = scale_coord(0.5, 0.5)
    return center_x + dx, center_y + dy

pressed_cash = []

def filter_key(const_dict: dict) -> dict:
    filter_storage = filter(lambda x: x[0].startswith('K_'), const_dict.items())
    return dict(filter_storage)

def is_tab_number(key: str) -> bool:
    return key.startswith('[') and key.endswith(']')

def correct_input(pressed_keys: list) -> str | list:

    if 'escape' in pressed_keys:
        symbol = 'esc'
    elif 'backspace' in pressed_keys:
        symbol = 'backspace'
    elif 'left shift' in pressed_cash:
        # shift_index = pressed_keys.index('left shift')
        # del pressed_keys[shift_index]

        symbol = pressed_keys[0].upper()
    else:
        print('pressed_keys', pressed_keys)
        symbol = pressed_keys[0]

    return symbol



