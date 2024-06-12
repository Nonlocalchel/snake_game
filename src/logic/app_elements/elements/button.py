class Button:
    def __init__(self, name: str, action: str, position: tuple) -> None:
        self.text = name
        self.__action = action
        self.state = None
        self.pos = position

    @property
    def is_hover(self) -> bool:
        return self.state is not None

    @property
    def is_action(self) -> bool:
        return self.state in ['click', 'mouse_down']

    @property
    def action(self) -> str:
        return self.__action
