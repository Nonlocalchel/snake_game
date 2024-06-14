from src.logic.app_elements.elements.base.element import Element

from src.logic.app_elements.elements import button, textInput

from src.logic.app_elements.elements.interactionBox import InteractionBox

from src.logic.pages.actions import Action


class ConfigurationBox(InteractionBox):
    def __init__(self, position: tuple[float, float] = (0.25, 0.25)) -> None:
        elements = self.create_elements()
        super().__init__(elements, position, (0.5, 0.4))

    @property
    def selected_input(self) -> textInput.Input:
        return self.elements[0]

    def handle_input(self, key: str) -> None:
        name_input = self.selected_input
        if key != 'escape':
            name_input.change(key)
        else:
            name_input.clear()

    @staticmethod
    def create_elements() -> tuple[Element, ...]:
        elements = ()

        elements += (textInput.Input('Введите имя'),)
        elements += (button.Button('Старт', Action.GO_TO_PLAY),)

        return elements
