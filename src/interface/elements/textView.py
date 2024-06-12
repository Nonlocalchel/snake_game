import pygame

from .baseView import BaseView

from src.settings import *
from src.interface.utils import figure_font, increase_size, figure_inner_pos, get_scale_radius


class TextView(BaseView):
    font_size: int = figure_font()
    radius: int | float = get_scale_radius(1)

    def __init__(self, text: str, coord: tuple[int, int] | None = None,
                 color: str = SIMPLE_TEXT_COLOR) -> None:
        super().__init__(coord)
        self.color = color
        self._text = text
        self.__view = self.get_text_surf()
        self.scale = (1.11,  1.21)

    def get_text_surf(self) -> pygame.Surface:
        font = pygame.font.SysFont('Calibri', self.font_size)
        text_surf = font.render(self._text, 1, self.color)
        return text_surf

    @property
    def view(self):
        return self.__view

    @view.setter
    def view(self, state: str) -> None:
        if state is None:
            return

        if state == 'hover':
            self.set_hover_view()

        if state == 'action':
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
        width_cof, height_cof = self.scale
        new_size = increase_size(size, width_cof=width_cof, height_cof=height_cof)
        pos = figure_inner_pos(size, new_size)
        new_surf = pygame.Surface(new_size, pygame.SRCALPHA)
        new_surf.fill((0, 0, 0, 0))
        new_surf.blit(
            self.__view,
            pos
        )

        self.__view = new_surf
