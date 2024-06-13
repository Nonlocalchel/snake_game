from src.logic.app_elements.elements.base.element import Element


class Button(Element):
    def __init__(self, name: str, action: str, position: tuple) -> None:
        super().__init__(position)
        self._text = name
        self.__action = action
        self.state = None

    @property
    def text(self):
        return self._text

    @property
    def is_hover(self) -> bool:
        return self.state is not None

    @property
    def is_action(self) -> bool:
        return self.state in ['click', 'mouse_down']

    @property
    def action(self) -> str:
        return self.__action
