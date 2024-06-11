import pygame

from src.interface.utils import *


class BaseView:
    radius = get_scale_radius()

    def __init__(self, coord, size=None):
        self._coord = coord
        self._size = size
        self._view = None

    @property
    def view(self):
        return self._view

    @property
    def coord(self):
        return self._coord

    @property
    def geom(self) -> pygame.Rect:
        x, y = self.coord
        return self.view.get_rect(centerx=x, centery=y)

    @property
    def size(self):
        return self._size or self.geom.size

    @property
    def height(self) -> int | float:
        return self.size[1]

    @property
    def width(self) -> int | float:
        return self.size[0]
