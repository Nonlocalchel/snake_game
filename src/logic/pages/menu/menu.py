from src.logic.pages.page import Page

from src.logic.elements_handlers.mouseHandle import MouseHandle

from src.logic.pages.actionHandle import ActionHandle
from src.logic.pages.actions import Action

from src.logic.playerHandle import PlayerHandle

from .menuBox import MenuBox
from .configurationBox import ConfigurationBox
from .utils import choose_conf_action, choose_menu_action

from src.interface.infrastructure import Infrastructure


class Menu(Page):
    """Контролирует цикл меню"""

    def __init__(self, infrastructure: Infrastructure) -> None:
        self.infrastructure = infrastructure
        self.action_handler = ActionHandle(infrastructure)
        self.mouse_handler = MouseHandle(infrastructure)
        self.start_config = ConfigurationBox()
        self.menu = MenuBox()
        self.player = PlayerHandle()
        self.is_running = True
        self.action = None
        self.name = 'menu'

    def process_events(self) -> None:
        """Обработка ввода от пользователя"""
        if self.infrastructure.is_quit_event():
            self.is_running = False

        action_handler = self.action_handler
        mouse_handler = self.mouse_handler

        key = self.infrastructure.get_pressed_key()
        box = self.menu

        action_handler.action = choose_menu_action(key, action_handler.action)

        if box.get_lock:
            box = self.start_config
            action_handler.action = choose_conf_action(key, action_handler.action)
            box.handle_input(key)

        for element in box.clickable_elements:
            position = box.get_real_element_pos(element)
            mouse_handler.handle(element, position)

            if element.state == 'click':
                action_handler.action = element.action

        self.action = action_handler.action

    def render(self) -> None:
        """Обновление экрана: перерисовка меню"""
        self.infrastructure.fill_bg(image='gold_snake.jpg')

        self.infrastructure.draw_box(self.menu.params)

        if self.menu.get_lock:
            self.infrastructure.draw_shadow()
            self.infrastructure.draw_box(self.start_config.params)

        self.infrastructure.update_and_tick()

    def update_state(self) -> None:
        """Вычисление следующего состояния всех объектов на экране"""
        self.menu.unlock()
        self.start_config.lock()

        if self.action is None:
            return

        action_value = self.action.value
        if action_value.startswith('go-to'):
            self.name = action_value.split('_')[1]

        if self.action == Action.SHOW_CONF:
            self.menu.lock()
            self.start_config.unlock()

        if self.action == Action.GO_TO_PLAY:
            name_input = self.start_config.selected_input
            if not name_input.is_empty:
                self.player.name = name_input.text

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
