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

        self.__action = new_action

    def handle_action(self, action: Action) -> None:
        match action:
            case Action.SHOW_CONF:
                self.infrastructure.play_popup_bubble_sound()

            case Action.SHOW_MENU:
                self.handle_action(Action.SHOW_CONF)

            case Action.GO_TO_PLAY:
                self.infrastructure.play_sound('snake_2.mp3')

            case Action.QUIT:
                self.infrastructure.play_popup_bubble_sound()
