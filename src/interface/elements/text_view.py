import pygame

from src.settings import *
from src.interface.utils import figure_font


class TextView:
    def __init__(self, text: str, pos: tuple | None = None, color: str = SIMPLE_TEXT_COLOR) -> None:
        self._descr = text
        self.text = self.set_text(text, color) #getter and setter
        self.__view = self.set_view(pos)

    def get_text(self, color: str, size: int = figure_font()) -> pygame.Surface:
        font = pygame.font.SysFont('Calibri', size)
        text_surf = font.render(self._descr, 1, color)
        return text_surf

    @property
    def get_view(self) -> pygame.Rect:
        return self.__view

    def set_view(self, coord: tuple, state: str | None = None) -> pygame.Rect | None:
        if not coord:
            return

        text = self.get_text()
        text_view = text.get_rect(centerx=coord[0], centery=coord[1])
        return text_view

    def is_match(self, pos: tuple) -> bool:
        return self.__view.collidepoint(pos)

    def draw(self, surf: pygame.Surface, coord: tuple | None = None, state: str ='') -> None:
        position = coord if coord is not None else self.__view
        surf.blit(
            self.text,
            position,
        )
