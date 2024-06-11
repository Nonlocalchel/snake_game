import pygame

from .baseView import BaseView

from src.settings import *
from src.interface.utils import figure_font, increase_size, figure_inner_pos, get_scale_radius


class TextView(BaseView):
    font_size: int = figure_font()
    radius: int | float = get_scale_radius(1)

    def __init__(self, text: str, coord: tuple[int, int] | None = None, scale: bool = True,
                 color: str = SIMPLE_TEXT_COLOR) -> None:
        super().__init__(coord)
        self.color = color
        self._text = text
        self.__view = self.get_text_surf()
        if scale:
            self.scale_view()

    def get_text_surf(self) -> pygame.Surface:
        font = pygame.font.SysFont('Calibri', self.font_size)
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
        self.scale_view()

        self.draw_border(self.__view, self.color)

    def set_active_view(self) -> None:
        self.color = SIMPLE_TEXT_COLOR

        self.__view = self.get_text_surf()
        self.scale_view()

        self.view.fill('green')

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
