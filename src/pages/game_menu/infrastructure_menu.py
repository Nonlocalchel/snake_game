import pygame

from src.interface.infrastructure import Infrastructure
from src.interface.button import Button

from src.constant import *


class InfrastructureMenu(Infrastructure):
    def __init__(self) -> None:
        super().__init__()

    def fill_screen(self) -> None:
        self.fill_bg(image='gold_snake.jpg')
        self.draw_menu()

    def fill_bg(self, bg_color=SCREEN_COLOR, image=None) -> None:
        if image:
            bg_pic = pygame.image.load(image)
            coef = bg_pic.get_width() / bg_pic.get_height()
            bg_pic = pygame.transform.scale(bg_pic, (WIDTH * SCALE * coef, HEIGHT * SCALE))
            self.screen.blit(bg_pic, (-45, 0))
        else:
            self.screen.fill(bg_color)

    def draw_menu(self) -> None:
        menu_surf = self.get_menu_surf(3, SCREEN_COLOR)
        Button('Играть',menu_surf,10,-65).draw()
        Button('Статистика', menu_surf, 10, 0).draw()
        Button('Выход', menu_surf, 10, 65).draw()
        self.screen.blit(menu_surf, (-RADIUS * 4, HEIGHT * (1 - 0.2 * (3)) / 2 * SCALE))


    def get_menu_surf(self, items_count, bg_color=SCREEN_COLOR):
        menu_surf = pygame.Surface((WIDTH * 0.5 * SCALE, (HEIGHT * 0.2 * (items_count)) * SCALE),pygame.SRCALPHA)
        menu_surf.fill((0,0,0,0))
        menu_rect = menu_surf.get_rect(left=0,centery=HEIGHT*0.3*SCALE)
        pygame.draw.rect(menu_surf, bg_color, menu_rect, border_radius=RADIUS*4)
        pygame.draw.rect(menu_surf, 'white', menu_rect,1, border_radius=RADIUS * 4)
        return menu_surf

    def quit(self) -> None:
        pygame.quit()
