from src.interface.infrastructure import Infrastructure

from ..actions import Action


class ActionHandler:
    def __init__(self, infrastructure: Infrastructure) -> None:
        self.infrastructure = infrastructure
        self.tracker = None
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

    def set_menu_action(self, key: str) -> None:
        action = None
        if key == 'return':
            action = Action.SHOW_CONF

        if key == 'escape':
            action = Action.QUIT

        self.action = action

    def set_conf_action(self, key: str) -> None:
        action = Action.SHOW_CONF
        if key == 'escape':
            action = Action.SHOW_MENU

        if key == 'return':
            action = Action.GO_TO_PLAY

        if action == Action.SHOW_CONF:
            return

        self.action = action

    def check_tracker(self, element):
        if self.tracker is None:
            return

        if not self.tracker.is_trackable_element(element):
            return

        return self.tracker.check_action()

    def handle_trackable_action(self, method):
        self.action = method()
        self.tracker = None
