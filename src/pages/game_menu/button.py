class Button:
    def __init__(self, name: str, action: str, position: tuple) -> None:
        self.text = name
        self.action = action
        self.state = None
        self.__position = position

    @property
    def pos(self):
        return self.__position

    @property
    def is_hover(self):
        return self.state in ['hover', 'click']

    @property
    def is_click(self):
        return self.state == 'click'

    def click(self):
        self.state = None
        return self.action
