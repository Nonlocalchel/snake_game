class Button:
    def __init__(self, name: str, action: str, position: tuple) -> None:
        self.text = name
        self.__action = action
        self.state = None
        self.pos = position

    @property
    def is_hover(self):
        return self.state == 'hover'

    @property
    def is_click(self):
        return self.state == 'click'

    def click(self):
        self.state = 'hover'
        return self.__action
