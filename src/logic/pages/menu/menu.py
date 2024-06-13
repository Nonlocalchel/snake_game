from src.logic.pages.display import Display

from .utils import get_clickable_elements, get_menu_params, menu_actions, conf_actions
from src.logic.elements_handlers.mouseHandle import MouseHandle
from src.logic.pages.actionHandle import ActionHandle
from ..actions import Action

from src.interface.infrastructure import Infrastructure

from .menuBox import MenuBox
from .configurationBox import ConfigurationBox

from src.logic.playerHandle import PlayerHandle


class Menu(Display):
    """Контролирует цикл меню"""

    def __init__(self, infrastructure: Infrastructure) -> None:
        self.infrastructure = infrastructure
        self.action_handler = ActionHandle(infrastructure)
        self.mouse_handler = MouseHandle(infrastructure)
        self.menu = MenuBox()
        self.start_config = ConfigurationBox()
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
        if self.action is None:
            action_handler.action = menu_actions.get(key, action_handler.action)

        container = self.menu
        if container.get_lock:
            container = self.start_config
            action_handler.action = conf_actions.get(key, action_handler.action)
            container.elements['Введите имя'].change(key) if key != 'escape' else container.elements['Введите имя'].clear()

        clickable_elements = get_clickable_elements(container.elements)
        for element in clickable_elements:
            position = container.get_real_element_pos(element)
            mouse_handler.handle(element, position)

            if element.state == 'click':
                action_handler.action = element.action

        self.action = action_handler.action

    def render(self) -> None:
        """Обновление экрана: перерисовка меню"""
        self.infrastructure.fill_bg(image='gold_snake.jpg')

        self.infrastructure.draw_container(
            *get_menu_params(self.menu)
        )

        if self.menu.get_lock:
            self.infrastructure.draw_shadow()
            self.infrastructure.draw_container(
                *get_menu_params(self.start_config)
            )

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
            name_input = self.start_config.elements['input']
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
