import pygame
from src.constant import *
from src.utils import *


class Message:
    def __init__(self, text, screen, dw=0, dh=0, color=GAME_OVER_COLOR):
        self.text = text
        self.color = color
        self.width = (WIDTH // 2 * SCALE) + dw
        self.height = (HEIGHT // 2 * SCALE) + dh
        self.screen = screen
        self.font = pygame.font.Font(None, figure_font())

    def draw(self) -> None:
        message = self.font.render(self.text, True, pygame.Color(GAME_OVER_COLOR))
        self.screen.blit(
            message,
            message.get_rect(center=(self.width, self.height)),
        )
