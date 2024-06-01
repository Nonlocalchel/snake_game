import pygame

from src.interface.utils import *


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
