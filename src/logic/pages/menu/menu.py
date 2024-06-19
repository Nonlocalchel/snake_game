from src.logic.pages.page import Page

from .menuBox import MenuBox
from .configurationBox import ConfigurationBox
from src.logic.pages.actions import Action
from src.logic.app_elements.playerHandle import PlayerHandle

from src.logic.handles.elements_handles.mouseHandle import MouseHandle
from src.logic.handles.elements_handles.inputHandle import InputHandle

from src.logic.handles.actionHandle import ActionHandle
from .interface_config import choose_box_action
from .utils import get_available_box, get_box_params, get_input, set_default_lock

from src.interface.infrastructure import Infrastructure


class Menu(Page):
    """Контролирует цикл меню"""

    def __init__(self, infrastructure: Infrastructure) -> None:
        self.infrastructure = infrastructure
        self.action = Action.SHOW_MENU
        self.action_handler = ActionHandle(infrastructure, self.action)
        self.mouse_handler = MouseHandle(infrastructure)
        self.input_handler = InputHandle(infrastructure)
        self.interface = {'menu': MenuBox(), 'start_conf': ConfigurationBox()}
        self.player = PlayerHandle()
        self.is_running = True
        self.name = 'menu'

    def process_events(self) -> None:
        """Обработка ввода от пользователя"""
        if self.infrastructure.is_quit_event():
            self.is_running = False

        action_handler = self.action_handler

        box = get_available_box(self.interface.values())

        key = self.infrastructure.get_pressed_key()
        if key:
            action_handler.action = choose_box_action(key, box)
            box_input = get_input(box)
            if box_input:
                self.input_handler.handle(box_input, key)

        for element in box.clickable_elements:
            position = box.get_real_element_pos(element)
            self.mouse_handler.handle(element, position)

            if element.state == 'click':
                action_handler.action = element.action

        self.action = action_handler.action

    def render(self) -> None:
        """Обновление экрана: перерисовка меню"""
        self.infrastructure.fill_bg(image='gold_snake.jpg')

        menu = self.interface['menu']
        self.infrastructure.draw_box(get_box_params(menu))

        available_box = get_available_box(self.interface.values())
        if available_box != menu:
            self.infrastructure.draw_shadow()
            self.infrastructure.draw_box(
                get_box_params(available_box)
            )

        self.infrastructure.update_and_tick()

    def update_state(self) -> None:
        """Вычисление следующего состояния всех объектов на экране"""
        boxs = self.interface.values()
        set_default_lock(boxs)

        match self.action:
            case Action.SHOW_CONF:
                menu = self.interface['menu']
                menu.lock()

            case Action.GO_TO_PLAY:
                name_input = get_input(self.interface['start_conf'])
                if not name_input.is_empty:
                    self.player.name = name_input.text

            case Action.QUIT:
                self.is_running = False

            case _:
                start_conf = self.interface['start_conf']
                self.input_handler.handle(get_input(start_conf), 'delete')
                start_conf.lock()

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
