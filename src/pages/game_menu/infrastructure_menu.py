import pygame
from src.constant import *


class InfrastructureMenu:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode([WIDTH * SCALE, HEIGHT * SCALE])
        self.font = pygame.font.Font(None, SCALE)

    def is_quit_event(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('quit event')
                return True
        return False

    def fill_screen(self):
        self.screen.fill(SCREEN_COLOR)

    def draw_menu(self) -> None:
        self.draw_message('GAME OVER',0,-50)
        self.draw_message("Нажмите SPACE,",0,20)
        self.draw_message("чтобы повторить",0,50)

    def draw_message(self, text: str, dw: int, dh: int) -> None:
        message = self.font.render(text, True, pygame.Color(GAME_OVER_COLOR))
        self.screen.blit(
            message,
            message.get_rect(center=((WIDTH // 2 * SCALE) + dw, (HEIGHT // 2 * SCALE) + dh)),
        )

    def update_display(self) -> None:
        pygame.display.update()

    def quit(self) -> None:
        pygame.quit()

