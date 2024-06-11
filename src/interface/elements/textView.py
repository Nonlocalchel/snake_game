import pygame

from src.settings import *
from src.interface.utils import figure_font, get_scale_radius, increase_size, figure_inner_pos


class TextView:
    size: int = figure_font()
    radius = get_scale_radius()

    def __init__(self, text: str, coord: tuple | None = None, color: str = SIMPLE_TEXT_COLOR) -> None:
        self.color = color
        self._text = text
        self._coord = coord
        self.__view = self.get_text_surf()

    @property
    def geom(self) -> pygame.Rect:
        x, y = self._coord
        return self.view.get_rect(centerx=x, centery=y)

    def get_text_surf(self) -> pygame.Surface:
        font = pygame.font.SysFont('Calibri', self.size)
        text_surf = font.render(self._text, 1, self.color)
        return text_surf

    @property
    def view(self):
        return self.__view

    @view.setter
    def view(self, state: str) -> None:
        if not state:
            return

        if state == 'hover':
            self.set_hover_view()

        if state == 'click':
            self.set_active_view()

        if state == 'unfocus':
            self.set_unfocused_view()

    def set_hover_view(self) -> None:
        self.color = HOVER_TEXT_COLOR
        self.__view = self.get_text_surf()

    def set_active_view(self) -> None:
        self.set_hover_view()

    def set_unfocused_view(self):
        self.color = UNFOCUSED_TEXT_COLOR
        self.__view = self.get_text_surf()

    def scale_view(self):
        size = self.geom.size
        new_size = increase_size(size)
        pos = figure_inner_pos(size, new_size)
        new_surf = pygame.Surface(new_size, pygame.SRCALPHA)
        new_surf.fill((0, 0, 0, 0))
        new_surf.blit(
            self.__view,
            pos
        )
        self.__view = new_surf
