import pygame

from src.interface.infrastructure import Infrastructure
from src.interface.message import Message

from src.constant import *
from src.pages.game.directions import Direction


class InfrastructureGame(Infrastructure):
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def get_pressed_key() -> Direction | None:
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            return Direction.DOWN
        if key[pygame.K_RIGHT]:
            return Direction.RIGHT
        if key[pygame.K_DOWN]:
            return Direction.UP
        if key[pygame.K_LEFT]:
            return Direction.LEFT
        return None

    def fill_screen(self):
        self.screen.fill(SCREEN_COLOR)

    def draw_element(self, x, y, color):
        pygame.draw.rect(
            self.screen,
            pygame.Color(color),
            (x * SCALE, y * SCALE, ELEMENT_SIZE, ELEMENT_SIZE),
            0,
            RADIUS,
        )

    def draw_score(self, score: int) -> None:
        self.screen.blit(
            self.font.render(f"Score: {score}", True, pygame.Color(SCORE_COLOR)),
            (5, 5),
        )

    def draw_game_over(self) -> None:
        Message('GAME OVER', self.screen,0,-25).draw()
        Message('Нажмите SPACE,', self.screen, 0, 20).draw()
        Message('чтобы играть снова', self.screen, 0, 50).draw()