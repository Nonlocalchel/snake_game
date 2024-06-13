from src.logic.app_elements.elements.base.element import Element

from src.logic.app_elements.elements import button, input

from .interactionBox import InteractionContainer

from ..actions import Action


class ConfigurationBox(InteractionContainer):
    def __init__(self, position: tuple[float, float] = (0.25, 0.25)) -> None:
        elements = self.create_elements()
        super().__init__(elements, position, (0.5, 0.4))

    def handle_input(self, key):
        pass

    @staticmethod
    def create_elements() -> tuple[Element, ...]:
        elements = ()

        elements += (input.Input('Введите имя'),)
        elements += (button.Button('Старт', Action.GO_TO_PLAY),)

        return elements
