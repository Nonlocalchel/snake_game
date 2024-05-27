class Input:
    def __init__(self, text: str, position: tuple) -> None:
        self.text = text
        self.position = position
        self.__default_text = text

    def change(self, char: str) -> None:
        if char == 'remove':
            self.text = self.text[:-1]
        self.text += char


