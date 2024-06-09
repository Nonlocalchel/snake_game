from src.interface.infrastructure import Infrastructure

from ..actions import Action

from src.logic.app_elements.elements.input import Input
from src.logic.app_elements.elements.button import Button
from src.logic.app_elements.elements.container import Container


class Handler:
    def __init__(self, infrastructure: Infrastructure) -> None:
        self.infrastructure = infrastructure
        self.__action = None

    @property
    def action(self) -> Action | None:
        return self.__action

    @action.setter
    def action(self, new_action):
        self.__action = new_action

        if new_action:
            self.handle_action(new_action)

    def handle_action(self, action):
        if action in [Action.SHOW_CONF, Action.SHOW_MENU]:
            self.infrastructure.play_popup_bubble_sound()

        if action == Action.SHOW_MENU:
            self.action = None

        if action == Action.QUIT:
            self.infrastructure.play_hover_sound()

    def handle_menu_action(self, key: str) -> None:
        action = None

        if key == 'return':
            action = Action.SHOW_CONF

        if key == 'escape':
            action = Action.QUIT

        self.action = action

    def handle_conf_action(self, key: str) -> None:
        action = Action.SHOW_CONF
        if key == 'escape':
            action = Action.SHOW_MENU

        if key == 'return':
            action = Action.GO_TO_PLAY

        if action == Action.SHOW_CONF:
            return

        self.action = action

    def handle_hover(self, element: Button) -> None:
        if element.is_hover:
            return

        self.infrastructure.play_hover_sound()
        element.state = 'hover'

    def handle_click(self, element: Button):
        mouse_down = self.infrastructure.is_click()
        if mouse_down:
            self.handle_mouse_down(element)

        mouse_up = element.is_click and not mouse_down
        if mouse_up:
            self.handle_mouse_up(element)

            self.action = element.click()

    @staticmethod
    def handle_mouse_down(element: Button) -> None:
        element.state = 'click'

    @staticmethod
    def handle_mouse_up(element: Button) -> None:
        element.state = None

    @staticmethod
    def handle_input(text_input: Input, key: str) -> None:
        if key == 'escape':
            text_input.clear()
        else:
            text_input.change(key)

        text_input.unfocus() if text_input.is_empty else text_input.focus()
