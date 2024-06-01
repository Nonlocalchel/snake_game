import pygame

from src.constant import *
from src.interface.utils import figure_font, scale


class TextView:
    def __init__(self, text: str, pos: tuple | None = (0, 0), color: str = SIMPLE_TEXT_COLOR) -> None:
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

    def set_view(self, coord: tuple) -> pygame.Rect | None:
        if not coord:
            return

        text = self.text
        text_view = text.get_rect(centerx=scale(WIDTH, coord[0]), centery=scale(HEIGHT, coord[1]))
        return text_view

    def is_match(self, pos: tuple) -> bool:
        return self.__view.collidepoint(pos)

    def draw(self, surf: pygame.Surface, center: bool = False) -> None:
        surf.blit(
            self.text,
            center or self.__view,
        )
