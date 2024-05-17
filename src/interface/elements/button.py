import pygame

from src.utils import *


class Button:
    def __init__(self, text: str, serf: pygame.Surface,
                 offset: tuple = (0, 0), serf_offset: tuple = (0, 0),
                 color: str = SIMPLE_TEXT_COLOR) -> None:
        self.font = pygame.font.SysFont('Calibri', figure_font())
        self.text = text
        self.color = color
        self.serf = serf
        self.rect = None
        self.center = get_center(offset, serf.get_rect()[2:])
        self.offset = offset
        self.serf_offset = serf_offset
        self.action = None
        self.draw()

    def draw(self) -> None:
        text = self.font.render(self.text, 1, self.color)
        self.rect = text.get_rect(center=self.center)
        self.serf.blit(
            text,
            self.rect
        )

    def onclick(self, action):
        self.action = action

    def is_hover(self, position):
        offset_x, offset_y = self.serf_offset
        rel_position = (position[0] - offset_x, position[1] - offset_y)
        return self.rect.collidepoint(rel_position)

    def is_click(self,position):
        if self.is_hover(position):
            if pygame.mouse.get_pressed()[0] == 1:
                return True
        return False

    def click(self,delay=120):
        self.action()
        pygame.time.wait(delay)