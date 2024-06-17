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

    @staticmethod
    def is_symbol(char: str) -> bool:
        return type(char) is str and len(char) == 1

    @property
    def text(self) -> str:
        return self._text or self.__default_text

    @text.setter
    def text(self, value):
        if self.is_empty:
            value = value[-1]

        if self.is_valid_length or len(self._text) > len(value):
            self._text = value

        self.switch_focus()

    def switch_focus(self):
        self.focus()

        if self.is_empty:
            self.unfocus()

    def focus(self):
        self.state = 'focus'

    def unfocus(self):
        self.state = 'unfocus'

    def change(self, char: str) -> None:
        remove = char == 'backspace'

        if self.is_empty and remove:
            return

        if remove:
            self.__remove_char()
            return

        if char == 'delete':
            self.clear()
            return

        if self.is_symbol(char):
            self.text += char

    def clear(self) -> None:
        if self.is_empty:
            return

        self.text = ''

    def __remove_char(self) -> None:
        self.text = self.text[:-1]
