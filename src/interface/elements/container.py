import pygame

from .utils import *


class Container:
    radius = get_scale_radius()

    def __init__(self, size: tuple, coords: tuple = (0, 0), bg_color: str = SCREEN_COLOR) -> None:
        self.size = size
        self.coords = coords
        self.bg_color = bg_color
        self.surface = pygame.Surface(size, pygame.SRCALPHA)
        self.make_brd_box()

    @property
    def height(self):
        return self.size[1]

    @height.setter
    def height(self, value):
        self.size = [self.size[0], value]
        self.make_brd_box()

    @property
    def width(self):
        return self.size[0]

    @width.setter
    def width(self, value):
        self.size = [value, self.size[1]]
        self.make_brd_box()

    def make_brd_box(self):
        surface = self.surface
        surface.fill((0, 0, 0, 0))
        rect = surface.get_rect(left=0, centery=self.height / 2)
        pygame.draw.rect(surface, self.bg_color, rect, border_radius=self.radius)
        pygame.draw.rect(surface, SIMPLE_TEXT_COLOR, rect, True, border_radius=self.radius)

    def draw_elements(self, elements: dict, offset: tuple = (0, 0)) -> None:
        padding = self.figure_padding(elements)
        counter = 1

        for element in elements.values():
            elem_coords = self.get_elements_coords(counter * padding, offset)
            self.draw_element(element, elem_coords)
            counter += 1

    def draw_element(self, element: any, elem_coords: tuple) -> None:
        element.set_view(elem_coords)
        if hasattr(element, 'is_hover'):
            element.serf_offset = self.coords
        element.draw(self.surface)

    def figure_padding(self, elements: dict) -> int:
        return self.height // (len(elements) + 1)

    def get_elements_coords(self, y: int, offset: tuple = (0, 0)) -> tuple:
        dw, dh = offset
        return (self.width // 2) + dw, y + dh
