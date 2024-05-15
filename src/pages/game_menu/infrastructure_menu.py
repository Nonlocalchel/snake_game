import pygame

from src.interface.infrastructure import Infrastructure
from src.interface.button import Button

from src.pages.actions import *

from src.constant import *

from .utils import *


class InfrastructureMenu(Infrastructure):
    def __init__(self) -> None:
        super().__init__()
        self.elements = {'buttons': {}, 'input': {}}

    def draw_menu(self) -> None:
        menu_surf = self.get_brd_box(3, SCREEN_COLOR)
        self.draw_buttons(menu_surf, ['Играть', 'Cтатистика', 'Выход'])
        self.screen.blit(
            menu_surf,
            (-get_scale_radius(), scale(HEIGHT, 1 - 0.2 * 3) // 2)
        )

    def draw_buttons(self, surface: pygame.Surface, params: list) -> None:
        padding = figure_padding(surface.get_rect().height, params)
        counter = -1
        for i in params:
            button = Button(i, surface, 10, counter * padding)
            self.elements['buttons'][i] = button
            button.draw()
            counter += 1

    @staticmethod
    def get_brd_box(items_count: int, bg_color: str = SCREEN_COLOR) -> pygame.Surface:
        menu_surf = pygame.Surface((scale(WIDTH, 0.5), scale(HEIGHT, 0.2 * items_count)), pygame.SRCALPHA)
        menu_surf.fill((0, 0, 0, 0))
        menu_rect = menu_surf.get_rect(left=0, centery=scale(HEIGHT, 0.3))
        pygame.draw.rect(menu_surf, bg_color, menu_rect, border_radius=get_scale_radius())
        pygame.draw.rect(menu_surf, SIMPLE_TEXT_COLOR, menu_rect, True, border_radius=get_scale_radius())
        return menu_surf

    @staticmethod
    def check_mouse() -> bool:
        return pygame.mouse.get_pressed()[0]==1

    def check_position(self) -> None:
        position = pygame.mouse.get_pos()
        rel_position = (position[0]+get_scale_radius(),position[1]-scale(HEIGHT, 1 - 0.2 * 3) // 2)
        buttons = self.elements['buttons']

        for i in buttons:
            if buttons[i].rect.collidepoint(rel_position):
                buttons[i].onclick(say_hello)

    def quit(self) -> None:
        pygame.quit()
