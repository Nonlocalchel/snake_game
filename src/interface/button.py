import pygame
from src.constant import *


class Button:
    def __init__(self, text,screen, dw=0, dh=0, font='Arial', color=GAME_OVER_COLOR):
        self.text = text
        self.color = color
        self.width = (WIDTH // 2 * SCALE) + dw
        self.height = (HEIGHT // 2 * SCALE) + dh
        self.screen=screen
        self.font=pygame.font.Font(font, SCALE)

    def draw_message(self, text: str, dw: int, dh: int) -> None:
        message = self.font.render(text, True, pygame.Color(GAME_OVER_COLOR))
        self.screen.blit(
            message,
            message.get_rect(center=(self.width, self.height)),
        )