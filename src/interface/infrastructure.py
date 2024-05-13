import pygame
from src.constant import *
from abc import abstractmethod


class Infrastructure:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode([WIDTH * SCALE, HEIGHT * SCALE])
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, SCALE)

    @staticmethod
    def is_quit_event() -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('quit event')
                return True
        return False

    def fill_screen(self):
        self.screen.fill(SCREEN_COLOR)

    def update_and_tick(self) -> None:
        pygame.display.update()
        self.clock.tick(FPS)

    @staticmethod
    def quit() -> None:
        pygame.quit()
