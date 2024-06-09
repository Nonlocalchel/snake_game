from src.interface.infrastructure import Infrastructure
from src.logic.pages.display import Display

from .utils import *

from src.logic.app_elements.elements.container import Container
from src.logic.app_elements.elements.button import Button


class Menu(Display):
    """Контролирует цикл меню"""

    def __init__(self, infrastructure: Infrastructure) -> None:
        self.infrastructure = infrastructure
        self.is_running = True
        self.menu = Container(Action.menu_actions(), (-0.05, 0.2), offset=(0.02, 0))
        self.start_config = Container(Action.start_actions(), (0.25, 0.25), (0.5, 0.4))
        self.action = None
        self.name = 'menu'
        self.player_name = 'unknown_user'

    def process_events(self) -> None:
        """Обработка ввода от пользователя"""
        if self.infrastructure.is_quit_event():
            self.is_running = False

        key = self.infrastructure.get_pressed_key()
        if not self.action:
            self.action = select_menu_action(key)

        container = self.menu
        if container.get_lock:
            container = self.start_config
            name_input = container.elements['input']
            if key:
                handle_input(name_input, key)
                self.action = select_conf_action(key)

            self.player_name = name_input.text if not name_input.is_empty else 'unknown'

        elements = container.elements
        for element in elements.values():
            if not type(element) is Button:
                continue

            position = container.get_real_element_pos(element)
            mouse_on = self.infrastructure.check_mouse(element.text, position)
            if mouse_on:
                handle_mouse_on(element, self.infrastructure.play_hover_sound)
            else:
                element.state = None

            if element.is_hover:
                mouse_down = self.infrastructure.is_click()
                if mouse_down:
                    handle_mouse_down(element)

                mouse_up = element.is_click and not mouse_down
                if mouse_up:
                    handle_mouse_up(element, None)

                    self.action = element.click()

    def render(self) -> None:
        """Обновление экрана: перерисовка меню"""
        self.infrastructure.fill_bg(image='gold_snake.jpg')

        draw_container(self.menu,
                       self.infrastructure)

        if self.menu.get_lock:
            self.infrastructure.draw_shadow()
            draw_container(self.start_config,
                           self.infrastructure)

        self.infrastructure.update_and_tick()

    def update_state(self) -> None:
        """Вычисление следующего состояния всех объектов на экране"""
        self.menu.unlock()
        self.start_config.lock()

        if self.action is None:
            return

        if self.action == Action.SHOW_CONF:
            self.menu.lock()
            self.start_config.unlock()


        # action_value = self.action.value
        if self.action.value.startswith('go-to'):
            self.name = self.action.value.split('_')[1]

        if self.action == Action.QUIT:
            self.is_running = False

    def loop(self):
        """Цикл меню"""
        while self.is_running:
            self.process_events()
            self.update_state()
            if self.name != 'menu':
                break

            self.render()
        else:
            self.infrastructure.quit()
