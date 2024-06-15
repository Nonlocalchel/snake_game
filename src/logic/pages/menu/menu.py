from src.logic.pages.page import Page

from .menuBox import MenuBox
from .configurationBox import ConfigurationBox
from src.logic.pages.actions import Action
from src.logic.playerHandle import PlayerHandle

from src.logic.elements_handlers.mouseHandle import MouseHandle
from src.logic.pages.actionHandle import ActionHandle
from .action_config import choose_alt_action, choose_box_action
from .utils import get_available_box

from src.interface.infrastructure import Infrastructure


class Menu(Page):
    """Контролирует цикл меню"""

    def __init__(self, infrastructure: Infrastructure) -> None:
        self.infrastructure = infrastructure
        self.action = Action.SHOW_MENU
        self.action_handler = ActionHandle(infrastructure, self.action)
        self.mouse_handler = MouseHandle(infrastructure)
        self.start_config = ConfigurationBox()
        self.menu = MenuBox()
        self.player = PlayerHandle()
        self.is_running = True
        self.name = 'menu'

    def process_events(self) -> None:
        """Обработка ввода от пользователя"""
        if self.infrastructure.is_quit_event():
            self.is_running = False

        action_handler = self.action_handler
        mouse_handler = self.mouse_handler

        box = get_available_box(self.menu, self.start_config)

        key = self.infrastructure.get_pressed_key()
        if key:
            action_handler.action = choose_box_action(key, box) or choose_alt_action(key)
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

        if self.menu.is_lock:
            self.infrastructure.draw_shadow()
            self.infrastructure.draw_box(self.start_config.params)

        self.infrastructure.update_and_tick()

    def update_state(self) -> None:
        """Вычисление следующего состояния всех объектов на экране"""
        self.start_config.unlock()
        self.menu.unlock()

        match self.action:
            case Action.SHOW_CONF:
                self.menu.lock()

            case Action.GO_TO_PLAY:
                name_input = self.start_config.selected_input
                if not name_input.is_empty:
                    self.player.name = name_input.text

            case Action.QUIT:
                self.is_running = False

            case _:
                self.start_config.lock()

        action_value = self.action.value
        if action_value.startswith('go-to'):
            self.name = action_value.split('_')[1]

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
