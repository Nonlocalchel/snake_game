from src.logic.app_elements.elements.base.element import Element

from src.logic.app_elements.elements import button

from .interactionBox import InteractionContainer

from ..actions import Action


class MenuContainer(InteractionContainer):
    def __init__(self, position) -> None:  # position = (-0.05, 0.2)
        elem_params = self.create_elements()
        super().__init__(elem_params, position, offset=(0.02, 0))

    def handle_input(self, key):
        pass

    @staticmethod
    def create_elements() -> tuple[Element, ...]:
        elements = ()

        elements += button.Button('Играть', Action.SHOW_CONF)
        elements += button.Button('Настройки', Action.GO_TO_RESULT)
        elements += button.Button('Выйти', Action.QUIT)

        return elements
