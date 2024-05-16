import pygame

from src.interface.infrastructure import Infrastructure
from src.interface.button import Button

from src.constant import *

from src.utils import *

from .actions_alias import actions_alias


class InfrastructureMenu(Infrastructure):
    def __init__(self) -> None:
        super().__init__()
        self.elements = {'buttons': {}, 'input': {}}

    def draw_menu(self) -> None:
        menu_surf = self.get_brd_box((scale(WIDTH, 0.5), scale(HEIGHT, 0.6)), SCREEN_COLOR)
        rel_position = (-get_scale_radius(), scale(HEIGHT, 0.4) // 2)
        self.draw_buttons(menu_surf, ['Играть', 'Cтатистика', 'Выход'], rel_position)
        self.screen.blit(
            menu_surf,
            rel_position
        )

    def draw_buttons(self, surface: pygame.Surface, params: list, serf_offset: tuple) -> None:
        padding = figure_padding(surface.get_rect().height, params)
        counter = -1
        for i in params:
            button = Button(i, surface, (10, counter * padding), serf_offset=serf_offset)
            self.elements['buttons'][i] = button
            counter += 1

    def check_position(self) -> None:
        position = pygame.mouse.get_pos()
        buttons = self.elements['buttons']

        for i in buttons:
            if buttons[i].match(position):
                buttons[i].onclick(actions_alias[i])
