from random import randrange
from .snake import Snake
from .element import Element
from src.constant import *

def gen_random_element() -> Element:
    return Element(
        randrange(0,WIDTH),
        randrange(0,HEIGHT)
    )

def gen_apple(snake: Snake):
    candidate=None
    while candidate is None:
        candidate = gen_random_element()
        if snake.is_contains(candidate):
            candidate=None
    return candidate

def get_center_element() -> Element:
    return Element(WIDTH // 2, HEIGHT // 2)

def is_field_contains(e:Element) -> bool:
    return 0<=e.x<WIDTH and 0<=e.y<HEIGHT

def is_valid_head(head:Element,snake:Snake) -> bool:
    return is_field_contains(head) and not snake.is_contains(head)
