class Input:
    def __init__(self, text: str, position: tuple) -> None:
        self._text = ''
        self.pos = position
        self.__default_text = text

    @property
    def is_empty(self) -> bool:
        return False if self._text else True

    @property
    def text(self):
        return self._text or self.__default_text

    @text.setter
    def text(self, char):
        self._text += char

    def change(self, char: str) -> None:
        remove = char == 'remove'

        if self.is_empty and remove:
            return

        if remove:
            self.__remove_char()
            return

        self._text += char

    def __remove_char(self):
        self._text = self._text[:-1]
