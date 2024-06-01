import pygame

from src.constant import *
from .utils import figure_font


class TextView:
    def __init__(self, text: str, pos: tuple, color: str = SIMPLE_TEXT_COLOR) -> None:
        self.text = self.set_text(text, color)
        self.__view = self.set_view(pos)

    @staticmethod
    def set_text(text: str, color: str, size: int = figure_font()) -> pygame.Surface:
        font = pygame.font.SysFont('Calibri', size)
        text_surf = font.render(text, 1, color)
        return text_surf

    @property
    def get_view(self) -> pygame.Rect:
        return self.__view

    def set_view(self, coord: tuple) -> pygame.Rect:
        text = self.text
        text_view = text.get_rect(centerx=coord[0], centery=coord[1])
        return text_view

    def is_match(self, pos: tuple) -> bool:
        return self.__view.collidepoint(pos)

    def draw(self, surf: pygame.Surface) -> None:
        surf.blit(
            self.text,
            self.__view,
        )
