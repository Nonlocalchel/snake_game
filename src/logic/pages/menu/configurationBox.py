from src.logic.app_elements.interface_elements.interactionBox import InteractionBox
from src.logic.app_elements.interface_elements import button, textInput

from src.logic.pages.actions import Action


class ConfigurationBox(InteractionBox):
    def __init__(self, position: tuple[float, float] = (0.25, 0.25)) -> None:
        super().__init__(position, size=(0.5, 0.4))
        self.put_elements()

    def handle_input(self, key) -> None:
        pass

    def put_elements(self) -> None:
        elements = ()

        elements += (textInput.Input('Введите имя'),)
        elements += (button.Button('Старт', Action.GO_TO_PLAY),)

        self.add_elements(*elements)
