from src.constant import *
from math import ceil





def scale(value: int, cof: int | float) -> int:
    return int(value * cof * SCALE)


def figure_font() -> int:
    return ceil(SCALE / 1.2)


def get_scale_radius(scale_cof: int = 4) -> int:
    return RADIUS * scale_cof



