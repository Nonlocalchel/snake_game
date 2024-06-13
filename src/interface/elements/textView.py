import pygame

from .baseView import BaseView

from src.settings import *
from src.interface.utils import figure_font, increase_size, figure_inner_pos, get_scale_radius, digit


class TextView(BaseView):
    font_size: int = figure_font()
    radius: int = get_scale_radius(1.4)

    def __init__(self, text: str, coord: tuple[int, int] | None = None,
                 color: str = SIMPLE_TEXT_COLOR) -> None:
        super().__init__(coord)
        self.color = color
        self._text = text
        self.__view = self.get_text_surf()
        self.scale = (1.11, 1.21)

    def get_text_surf(self) -> pygame.Surface:
        font = pygame.font.SysFont('Calibri', self.font_size)
        text_surf = font.render(self._text, 1, self.color)
        return text_surf

    def set_colored_and_scaled_view(self, color: str = SIMPLE_TEXT_COLOR, scale: None | tuple[digit, digit] = None):
        self.color = color

        self.__view = self.get_text_surf()
        scale = scale or self.scale
        self.scale_view(scale)

    @property
    def view(self) -> pygame.Surface:
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
        self.set_colored_and_scaled_view(HOVER_TEXT_COLOR)
        self.fill_view_with_rect(self.color, is_border=True)

    def set_active_view(self) -> None:
        self.set_colored_and_scaled_view(SIMPLE_TEXT_COLOR)
        self.fill_view_with_rect(HOVER_TEXT_COLOR)

        text_view = self.get_text_surf()
        pos = figure_inner_pos(text_view.get_rect().size, self.size)
        self.view.blit(
            text_view,
            pos
        )

    def set_unfocused_view(self) -> None:
        self.color = UNFOCUSED_TEXT_COLOR
        self.__view = self.get_text_surf()

    def scale_view(self, scale: None | tuple[digit, digit] = None) -> None:
        size = self.size
        width_cof, height_cof = scale or self.scale
        new_size = increase_size(size, width_cof=width_cof, height_cof=height_cof)
        pos = figure_inner_pos(size, new_size)
        new_surf = pygame.Surface(new_size, pygame.SRCALPHA)
        new_surf.fill((0, 0, 0, 0))
        new_surf.blit(
            self.__view,
            pos
        )

        self.__view = new_surf
