class Button:
    def __init__(self, name: str, action: str, position: tuple) -> None:
        self.text = name
        self.action = action
        self.state = None
        self.pos = position

    @property
    def is_hover(self):
        return self.state == 'click'

    @property
    def is_click(self):
        return self.state in ['hover', 'click']

    def click(self):
        self.state = None
        return self.action
