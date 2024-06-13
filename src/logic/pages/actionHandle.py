from src.interface.infrastructure import Infrastructure

from src.logic.pages.actions import Action


class ActionHandle:
    def __init__(self, infrastructure: Infrastructure) -> None:
        self.infrastructure = infrastructure
        self.__action = None

    @property
    def action(self) -> Action | None:
        return self.__action

    @action.setter
    def action(self, new_action: Action | None) -> None:
        self.__action = new_action

        if new_action:
            self.handle_action(new_action)

    def handle_action(self, action: Action | None) -> None:
        if action in [Action.SHOW_CONF, Action.SHOW_MENU]:
            self.infrastructure.play_popup_bubble_sound()

        if action == Action.SHOW_MENU:
            self.action = None

        if action == Action.QUIT:
            self.infrastructure.play_popup_bubble_sound()

