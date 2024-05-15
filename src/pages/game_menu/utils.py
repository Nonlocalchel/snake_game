from src.constant import *


def figure_padding(height, collection):
    items_count = len(collection)
    return int((height - 45) / items_count)


def get_scale_radius(scale_coef=4):
    return RADIUS * scale_coef


def scale(value, coef):
    return int(value * coef * SCALE)
