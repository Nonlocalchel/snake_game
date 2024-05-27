class Button:
    def __init__(self, name: str, action: str, position: tuple) -> None:
        self.text = name
        self.action = action
        self.state = None
        self.__position = position
        self.__access = True

    @property
    def pos(self):
        return self.__position

    @property
    def is_hover(self):
        return self.state in ['hover', 'click']

    @property
    def is_click(self):
        return self.state == 'click'

    def figure_rel_pos(self, outer: tuple) -> tuple:
        outer_x, outer_y = outer
        return outer_x + self.pos[0], outer_y + self.pos[1]

    def click(self):
        if self.__access:
            self.__access = False
            return self.action
