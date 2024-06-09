class Input:
    def __init__(self, text: str, position: tuple) -> None:
        self._text = ''
        self.pos = position
        self.__default_text = text
        self.state = 'unfocus'

    @property
    def is_empty(self) -> bool:
        return False if self._text else True

    @property
    def is_valid_length(self) -> bool:
        return len(self._text) <= 12

    @staticmethod
    def is_symbol(char: str) -> bool:
        return len(char) == 1

    @property
    def text(self) -> str:
        return self._text or self.__default_text

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
            self._text += char if self.is_valid_length else ''

    def clear(self) -> None:
        self._text = ''

    def __remove_char(self) -> None:
        self._text = self._text[:-1]
