from src.logic.pages.display import Display

from .utils import get_clickable_elements, draw_container
from ..actions import Action

from src.interface.infrastructure import Infrastructure

from src.logic.elements_handlers.mouseHandle import MouseHandle
from .actionHandle import ActionHandle

from src.logic.app_elements.elements.container import Container
from src.logic.playerHandle import PlayerHandle


class Menu(Display):
    """Контролирует цикл меню"""

    def __init__(self, infrastructure: Infrastructure) -> None:
        self.infrastructure = infrastructure
        self.action_handler = ActionHandle(infrastructure)
        self.mouse_handler = MouseHandle(infrastructure)
        self.menu = Container(Action.menu_actions(), (-0.05, 0.2), offset=(0.02, 0))
        self.start_config = Container(Action.conf_actions(), (0.25, 0.25), (0.5, 0.4))
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
            action_handler.set_menu_action(key)

        container = self.menu
        if container.get_lock:
            container = self.start_config
            action_handler.set_conf_action(key)
            name_input = container.elements['input']
            name_input.change(key)

        for element in get_clickable_elements(container.elements):
            mouse_handler.handle_pos(element, container)
            if element.is_hover:
                mouse_handler.handle_click(element)

            if element.state == 'click':
                action_handler.action = element.action

        self.action = action_handler.action

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
            self.start_config.elements['input'].clear()
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
