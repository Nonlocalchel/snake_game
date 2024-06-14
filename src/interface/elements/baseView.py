import pygame

from src.interface.utils import *


class BaseView:
    radius = get_scale_radius()

    def __init__(self, coord: tuple[int, int], size=None):
        self._coord = coord
        self._size = size
        self._view = None

    @property
    def view(self) -> pygame.Surface:
        return self._view

    @property
    def coord(self) -> tuple[int, int]:
        return self._coord

    @coord.setter
    def coord(self, value) -> None:
        self._coord = value

    @property
    def geom(self) -> pygame.Rect:
        x, y = self.coord
        return self.view.get_rect(centerx=x, centery=y)

    @property
    def size(self) -> tuple[digit, digit]:
        return self._size or self.geom.size

    @property
    def height(self) -> int | float:
        return self.size[1]

    @property
    def width(self) -> int | float:
        return self.size[0]

    @property
    def rect_to_draw(self) -> pygame.Rect:
        surf = self.view
        height = fix_height(self.height)

        return surf.get_rect(left=0, centery=(height / 2))

    def fill_view_with_rect(self, color: str = SIMPLE_TEXT_COLOR, is_border: bool = False) -> None:
        rect = self.rect_to_draw
        surf = self.view
        radius = self.radius
        pygame.draw.rect(surf, color, rect, is_border, border_radius=radius)
