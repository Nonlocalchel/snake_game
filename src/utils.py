from src.constant import *
from math import ceil


def figure_padding(height, collection):
    items_count = len(collection)
    return int((height - 45) / items_count)


def scale(value, cof):
    return int(value * cof * SCALE)


def figure_font():
    return ceil(SCALE / 1.2)


def get_scale_radius(scale_coef=4):
    return RADIUS * scale_coef


def get_center(offset, size) -> tuple:
    dw, dh = offset
    width, height = size[0], size[1]
    return (width // 2) + dw, (height // 2) + dh


