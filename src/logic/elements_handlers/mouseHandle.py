from src.interface.infrastructure import Infrastructure

from src.logic.app_elements.interface_elements.button import Button


class MouseHandle:
    def __init__(self, infrastructure: Infrastructure) -> None:
        self.infrastructure = infrastructure
        self.handle_element = None

    def handle(self, element: Button, elem_position: tuple[float, float]) -> None:
        self.handle_element = element

        self.handle_pos(elem_position)
        if element.is_hover:
            self.handle_click()

        self.handle_state()

    def handle_pos(self, position: tuple[float, float]) -> None:
        element = self.handle_element

        hover = self.infrastructure.check_mouse(element.text, position)
        if hover:
            self.handle_mouse_over()
        else:
            element.state = None

    def handle_mouse_over(self) -> None:
        element = self.handle_element

        if element.is_hover:
            return

        self.infrastructure.play_hover_sound()
        element.state = 'hover'

    def handle_click(self) -> None:
        element = self.handle_element

        if element.state == 'click':
            self.handle_mouse_up()

        is_click = self.infrastructure.is_click()
        if is_click:
            self.handle_mouse_down()

        mouse_up = element.state == 'mouse_down' and not is_click
        if mouse_up:
            self.handle_mouse_up()

    def handle_mouse_down(self) -> None:
        self.handle_element.state = 'mouse_down'

    def handle_mouse_up(self) -> None:
        element = self.handle_element

        if element.state == 'mouse_down':
            element.state = 'click'
            return

        element.state = 'mouse_up'

    def handle_state(self):
        if self.handle_element.state == 'hover':
            print('heandle_hover')

