import pygame
from src.constant import *

from .utils import *

class Button:
    def __init__(self, text: str, screen: pygame.Surface, dw: int = 0, dh: int = 0, color: str = SIMPLE_TEXT_COLOR) -> None:
        self.font = pygame.font.SysFont('Calibri', figure_font())
        self.text = text
        self.color = color
        self.screen = screen
        self.rect = None
        self.center = self.get_serf_center(dw, dh)
        self.clicked = False

    def get_serf_center(self, dw: int = 0, dh: int = 0) -> tuple:
        rect = self.screen.get_rect()
        rect.w = rect[2]
        rect.h = rect[3]
        return (rect.w // 2) + dw, (rect.h // 2) + dh

    def draw(self) -> None:
        text = self.font.render(self.text, 1, self.color)
        self.rect=text.get_rect(center=self.center)
        self.screen.blit(
            text,
            self.rect
        )

    @staticmethod
    def onclick(func):
        func()
        pygame.time.wait(60)
