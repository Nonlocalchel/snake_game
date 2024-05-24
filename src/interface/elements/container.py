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

    @property
    def coords(self):
        return self.__coords

    @coords.setter
    def coords(self, value):
        self.__coords = value

    def make_brd_box(self):
        surface = self.surface
        surface.fill((0, 0, 0, 0))
        rect = surface.get_rect(left=0, centery=self.height / 2)
        pygame.draw.rect(surface, self.bg_color, rect, border_radius=self.radius)
        pygame.draw.rect(surface, SIMPLE_TEXT_COLOR, rect, True, border_radius=self.radius)

    def draw_elements(self, buttons: dict, offset: tuple = (0, 0)) -> None:
        padding = self.figure_padding(self.height, buttons)
        counter = 1

        for button in buttons.values():
            elem_coords = self.get_elements_coords(counter * padding, self.width, offset)
            self.draw_element(button, elem_coords)
            counter += 1

    def draw_element(self, element: any, elem_coords: tuple) -> None:
        element.set_view(elem_coords)
        element.serf_offset = self.coords
        element.draw(self.surface)

    @staticmethod
    def figure_padding(surf_height: int, elements: dict) -> int:
        return surf_height // (len(elements) + 1)

    @staticmethod
    def get_elements_coords(center_y: int, center_x: int, offset: tuple = (0, 0)) -> tuple:
        dw, dh = offset
        return (center_x // 2) + dw, center_y + dh