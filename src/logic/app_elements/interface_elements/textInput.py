from src.logic.app_elements.interface_elements.base.element import Element


class Input(Element):
    def __init__(self, text: str, position: tuple = (0, 0)) -> None:
        super().__init__(position)
        self._text = ''
        self.__default_text = text
        self.state = 'unfocus'

    @property
    def is_empty(self) -> bool:
        return False if self._text else True

    @property
    def is_valid_length(self) -> bool:
        return len(self._text) < 10

    @property
    def text(self) -> str:
        return self._text or self.__default_text

    @text.setter
    def text(self, value):
        if self.is_empty:
            value = value[-1]

        if self.is_valid_length or len(self._text) > len(value):
            self._text = value

    def focus(self):
        self.state = 'focus'

    def unfocus(self):
        self.state = 'unfocus'

    def clear(self) -> None:
        if self.is_empty:
            return

        self.text = ''

    def remove_char(self) -> None:
        self.text = self.text[:-1]
