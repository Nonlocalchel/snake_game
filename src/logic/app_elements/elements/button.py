class Button:
    def __init__(self, name: str, action: str, position: tuple) -> None:
        self.text = name
        self.__action = action
        self.state = None
        self.pos = position

    @property
    def is_hover(self) -> bool:
        return self.state in ['hover', 'click']

    @property
    def is_click(self) -> bool:
        return self.state == 'click'

    @property
    def action(self) -> str:
        return self.__action

    def click(self) -> str:
        self.state = 'hover'
        return self.__action
