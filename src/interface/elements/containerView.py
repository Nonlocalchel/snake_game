import pygame

from src.interface.utils import *


class ContainerView:
    radius = get_scale_radius()

    def __init__(self, size: tuple[int, int], coord: tuple = (0, 0), bg_color: str = SCREEN_COLOR) -> None:
        self.size = size
        self._coord = coord
        self.bg_color = bg_color
        self.__view = pygame.Surface(size, pygame.SRCALPHA)
        self.make_brd_box()

    @property
    def height(self) -> int | float:
        return self.size[1]

    @property
    def coord(self):
        return self._coord

    @property
    def view(self):
        return self.__view

    def make_brd_box(self) -> None:
        surface = self.view
        surface.fill((0, 0, 0, 0))
        rect = surface.get_rect(left=0, centery=self.height / 2)
        pygame.draw.rect(surface, self.bg_color, rect, border_radius=self.radius)
        pygame.draw.rect(surface, SIMPLE_TEXT_COLOR, rect, True, border_radius=self.radius)
