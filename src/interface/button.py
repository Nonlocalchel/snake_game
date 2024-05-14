import pygame
from src.constant import *


class Button:
    def __init__(self, text, screen, dw=0, dh=0, font=None, color=SIMPLE_TEXT_COLOR):
        self.text = text
        self.color = color
        self.font = pygame.font.SysFont('Calibri', 32)
        self.screen = screen
        self.center = self.get_serf_center(dw, dh)  # ((WIDTH // 2 * SCALE) + dw, (HEIGHT // 2 * SCALE) + dh)

    def get_serf_center(self, dw=0, dh=0):
        rect = self.screen.get_rect()
        rect.w = rect[2]
        rect.h = rect[3]
        return ((rect.w // 2) + dw, (rect.h // 2) + dh)

    def draw(self) -> None:
        buttonText = self.font.render(self.text, 1, self.color)
        self.screen.blit(
            buttonText,
            buttonText.get_rect(center=self.center),
        )
