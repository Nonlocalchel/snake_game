from src.logic.app_elements.interface_elements.interactionBox import InteractionBox
from src.logic.app_elements.interface_elements import button

from src.logic.pages.actions import Action


class MenuBox(InteractionBox):
    def __init__(self, position: tuple[float, float] = (-0.05, 0.2)) -> None:
        super().__init__(position, offset=(0.02, 0))
        self.put_elements()

    def handle_input(self, key) -> None:
        pass

    def put_elements(self) -> None:
        elements = ()

        elements += (button.Button('Играть', Action.SHOW_CONF),)
        elements += (button.Button('Настройки', Action.GO_TO_RESULT),)
        elements += (button.Button('Выйти', Action.QUIT),)

        self.add_elements(*elements)
