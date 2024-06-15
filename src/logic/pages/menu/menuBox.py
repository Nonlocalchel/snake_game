from src.logic.app_elements.elements.base.element import Element

from src.logic.app_elements.elements import button

from src.logic.app_elements.elements.interactionBox import InteractionBox

from src.logic.pages.actions import Action


class MenuBox(InteractionBox):
    def __init__(self, position: tuple[float, float] = (-0.05, 0.2)) -> None:
        elements = self.add_elements()
        super().__init__(elements, position, offset=(0.02, 0))

    def handle_input(self, key) -> None:
        pass

    @staticmethod
    def add_elements() -> tuple[Element, ...]:
        elements = ()

        elements += (button.Button('Играть', Action.SHOW_CONF),)
        elements += (button.Button('Настройки', Action.GO_TO_RESULT),)
        elements += (button.Button('Выйти', Action.QUIT),)

        return elements
