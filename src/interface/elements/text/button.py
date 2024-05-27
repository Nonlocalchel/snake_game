import pygame

from src.interface.elements.utils import *


class Button:
    def __init__(self, text: str,
                 font: pygame.font.Font, serf_offset: tuple = (0, 0), color: str = SIMPLE_TEXT_COLOR) -> None:
        self.text = font.render(text, 1, color) #view
        self.serf_offset = serf_offset
        self.onclick = None
        self.__access = True
        self.__btn_view = None

    def set_view(self, coord: tuple) -> None:
        button = self.text
        self.__btn_view = button.get_rect(centerx=coord[0], centery=coord[1])

    def draw(self, surf: pygame.surface.Surface) -> None:
        button = self.__btn_view
        surf.blit(
            self.text,
            button
        )

    def is_hover(self, position: tuple) -> bool:
        offset_x, offset_y = self.serf_offset
        rel_position = (position[0] - offset_x, position[1] - offset_y)
        return self.__btn_view.collidepoint(rel_position)

    def is_click(self, position: tuple) -> bool:
        if self.is_hover(position):
            if pygame.mouse.get_pressed()[0] == 1:
                return True
        return False

    def click(self) -> None:
        if self.__access:
            self.onclick()
        self.__access = False
