from src.logic.app_elements.interface_elements.base.element import Element

from src.logic.pages.actions import Action


class Button(Element):
    def __init__(self, name: str, action: Action, position: tuple = (0, 0)) -> None:
        super().__init__(position)
        self._text = name
        self.__action = action
        self.state = None

    @property
    def text(self) -> str:
        return self._text

    @property
    def is_hover(self) -> bool:
        return self.state is not None

    @property
    def is_action(self) -> bool:
        return self.state in ['click', 'mouse_down']

    @property
    def action(self) -> Action:
        return self.__action
