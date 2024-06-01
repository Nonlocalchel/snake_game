import pygame

from src.constant import *


class TextView:
    def __init__(self, text: str, font: pygame.font.Font, pos: tuple,
                 color: str = SIMPLE_TEXT_COLOR, ) -> None:
        self.text = font.render(text, 1, color)
        self.__view = self.set_view(pos)

    @property
    def get_view(self) -> pygame.Rect:
        return self.__view

    def set_view(self, coord) -> pygame.Rect:
        text = self.text
        text_view = text.get_rect(centerx=coord[0], centery=coord[1])
        return text_view

    def is_match(self, pos) -> bool:
        return self.__view.collidepoint(pos)

    def draw(self, surf: pygame.Surface) -> None:
        surf.blit(
            self.text,
            self.__view,
        )
