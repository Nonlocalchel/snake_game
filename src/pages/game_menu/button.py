class Button:
    def __init__(self, name: str, action: str, position: tuple) -> None:
        self.text = name
        self.__action = action
        self.state = None
        self.__mouse_on = None
        self.pos = position

    @property
    def mouseon(self):
        if self.__mouse_on:
            self.mouse_over()
            return True

        return False

    def mouse_on(self):
        self.state = 'hover'
        self.__mouse_on = True

    def mouse_over(self):
        self.state = None
        self.__mouse_on = False

    @property
    def is_hover(self):
        return self.state == 'hover'

    @property
    def is_click(self):
        return self.state in ['hover', 'click']

    def click(self):
        self.state = None
        return self.__action
