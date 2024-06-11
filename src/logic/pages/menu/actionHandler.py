from src.interface.infrastructure import Infrastructure

from ..actions import Action

from src.logic.app_elements.elements.input import Input


class ActionHandler:
    def __init__(self, infrastructure: Infrastructure) -> None:
        self.infrastructure = infrastructure
        self.handle_element = None
        self.__action = None

    @property
    def action(self) -> Action | None:
        return self.__action

    @action.setter
    def action(self, new_action: Action | None) -> None:
        self.__action = new_action

        if new_action:
            self.pre_handle_action(new_action)

    def pre_handle_action(self, action: Action | None) -> None:
        if action in [Action.SHOW_CONF, Action.SHOW_MENU]:
            self.infrastructure.play_popup_bubble_sound()

        if action == Action.SHOW_MENU:
            self.action = None

        if action == Action.QUIT:
            self.infrastructure.play_popup_bubble_sound()

    def handle_menu_input(self, key: str) -> None:
        action = None
        if key == 'return':
            action = Action.SHOW_CONF

        if key == 'escape':
            action = Action.QUIT

        self.action = action

    def handle_conf_input(self, text_input: Input, key: str) -> None:
        text_input.change(key)

        action = Action.SHOW_CONF
        if key == 'escape':
            action = Action.SHOW_MENU
            text_input.clear()

        if key == 'return':
            action = Action.GO_TO_PLAY

        if action == Action.SHOW_CONF:
            return

        self.action = action
