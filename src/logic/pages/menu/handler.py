from src.interface.infrastructure import Infrastructure

from ..actions import Action

from src.logic.app_elements.elements.input import Input
from src.logic.app_elements.elements.button import Button
from src.logic.app_elements.elements.container import Container


class Handler:
    def __init__(self, infrastructure: Infrastructure) -> None:
        self.infrastructure = infrastructure
        self.handle_action = None

    def handle_menu_action(self, key: str) -> None:
        if key:
            self.infrastructure.play_hover_sound()

        action = None
        if key == 'return':
            action = Action.SHOW_CONF

        if key == 'escape':
            action = Action.QUIT

        self.handle_action = action

    def handle_conf_action(self, key: str) -> None:
        # if key:
        #     self.infrastructure.play_hover_sound()

        action = Action.SHOW_CONF
        if key == 'escape':
            action = None

        if key == 'return':
            action = Action.GO_TO_PLAY

        self.handle_action = action

    def handle_mouse_on(self, element: Button) -> None:
        if element.is_hover:
            return

        self.infrastructure.play_hover_sound()
        element.state = 'hover'

    def handle_mouse_down(self, element: Button) -> None:
        element.state = 'click'

    def handle_mouse_up(self, element: Button) -> None:
        self.handle_action = element.click()

    @staticmethod
    def handle_input(text_input: Input, key: str) -> None:
        if key == 'escape':
            text_input.clear()
        else:
            text_input.change(key)

        text_input.unfocus() if text_input.is_empty else text_input.focus()
