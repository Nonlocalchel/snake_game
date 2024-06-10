from src.interface.infrastructure import Infrastructure

from src.logic.pages.display import Display

from ..actions import Action
from .handler import Handler
from .utils import get_clickable_elements, draw_container

from src.logic.app_elements.elements.container import Container
from src.logic.player import Player


class Menu(Display):
    """Контролирует цикл меню"""

    def __init__(self, infrastructure: Infrastructure) -> None:
        self.infrastructure = infrastructure
        self.handler = Handler(infrastructure)
        self.menu = Container(Action.menu_actions(), (-0.05, 0.2), offset=(0.02, 0))
        self.start_config = Container(Action.conf_actions(), (0.25, 0.25), (0.5, 0.4))
        self.player = Player('default_user', 0, None)
        self.is_running = True
        self.action = None
        self.name = 'menu'

    def process_events(self) -> None:
        """Обработка ввода от пользователя"""
        if self.infrastructure.is_quit_event():
            self.is_running = False

        handler = self.handler

        key = self.infrastructure.get_pressed_key()
        if self.action is None:
            handler.handle_menu_input(key)

        container = self.menu
        if container.get_lock:
            container = self.start_config
            name_input = container.elements['input']
            if key:
                handler.handle_input(name_input, key)
                handler.handle_conf_input(key)

            if not name_input.is_empty:
                self.player.name = name_input.text

        elements = get_clickable_elements(container.elements)
        for element in elements:
            handler.handle_hover(element, container)
            if element.is_hover:
                handler.handle_click(element)

        self.action = handler.action

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

        action_value = self.action.value
        if action_value.startswith('go-to'):
            self.name = action_value.split('_')[1]

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
