import pygame
from src.constant import *
from src.pages.game.directions import Direction
from src.interface.infrastructure import Infrastructure


class InfrastructureGame(Infrastructure):
    def __init__(self) -> None:
        super().__init__()

    def get_pressed_key(self) -> Direction|None:
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
        self.draw_message('GAME OVER',0,-50)
        self.draw_message("Нажмите SPACE,",0,20)
        self.draw_message("чтобы повторить",0,50)


    def draw_message(self, text: str, dw: int, dh: int) -> None:
        message = self.font.render(text, True, pygame.Color(GAME_OVER_COLOR))
        self.screen.blit(
            message,
            message.get_rect(center=((WIDTH // 2 * SCALE) + dw, (HEIGHT // 2 * SCALE) + dh)),
        )

