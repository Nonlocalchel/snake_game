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
        self.draw()

    def draw(self) -> None:
        text = self.font.render(self.text, 1, self.color)
        self.rect = text.get_rect(center=self.center)
        self.serf.blit(
            text,
            self.rect
        )

    def match(self, position):
        offset_x, offset_y = self.serf_offset
        rel_position = (position[0] - offset_x, position[1] - offset_y)
        return self.rect.collidepoint(rel_position)

    @staticmethod
    def onclick(func):
        if pygame.mouse.get_pressed()[0] == 1:
            func()
            pygame.time.wait(120)
