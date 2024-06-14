from src.interface.infrastructure import Infrastructure

from src.logic.pages.actions import Action


class ActionHandle:
    def __init__(self, infrastructure: Infrastructure, start_action: Action) -> None:
        self.infrastructure = infrastructure
        self.__action = start_action

    @property
    def action(self) -> Action | None:
        return self.__action

    @action.setter
    def action(self, new_action: Action | None) -> None:
        if new_action in [self.__action, None]:
            return

        self.handle_action(new_action)
        if new_action != Action.INPUT:
            self.__action = new_action

    def handle_action(self, action: Action) -> None:
        if action == Action.SHOW_CONF:
            self.infrastructure.play_popup_bubble_sound()

        if action == Action.SHOW_MENU:
            self.handle_action(Action.SHOW_CONF)

        if action == Action.INPUT:
            pass

        if action == Action.QUIT:
            self.infrastructure.play_popup_bubble_sound()
