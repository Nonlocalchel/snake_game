import pygame

from src.interface.utils import *

from .baseView import BaseView


class ContainerView(BaseView):

    def __init__(self, size: tuple[int, int], coord: tuple[int, int] = (0, 0), bg_color: str = SCREEN_COLOR) -> None:
        super().__init__(coord)
        self._size = size
        self.bg_color = bg_color
        self.__view = pygame.Surface(size, pygame.SRCALPHA)
        self.make_brd_box()

    @property
    def view(self):
        return self.__view

    def make_brd_box(self) -> None:
        surface = self.view
        surface.fill((0, 0, 0, 0))
        rect = self.rect_to_draw
        pygame.draw.rect(surface, self.bg_color, rect, border_radius=self.radius)
        self.draw_border(surface)
