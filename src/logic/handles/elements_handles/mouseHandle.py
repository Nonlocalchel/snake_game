from src.logic.app_elements.interface_elements.button import Button

from src.interface.infrastructure import Infrastructure


class MouseHandle:
    def __init__(self, infrastructure: Infrastructure) -> None:
        self.infrastructure = infrastructure
        self.handle_element = None

    @property
    def state(self):
        return self.handle_element.state

    @state.setter
    def state(self, new_state):
        if new_state == self.state:
            return

        if new_state:
            self.handle_state(new_state)

        self.handle_element.state = new_state

    def handle(self, element: Button, elem_position: tuple[float, float]) -> None:
        self.handle_element = element

        mouse_on_element = self.infrastructure.check_mouse(element.text, elem_position)
        if mouse_on_element:
            self.handle_mouse_over()
        else:
            self.handle_mouse_out()
            self.state = None

        if element.is_hover:
            self.handle_click()

    def handle_mouse_over(self) -> None:
        if self.handle_element.is_hover:
            return

        self.state = 'mouse_over'

    def handle_mouse_out(self) -> None:
        if self.state in ['mouse_up', 'mouse_over']:
            self.state = 'mouse_out'

    def handle_click(self) -> None:
        if self.state == 'click':
            self.handle_mouse_up()

        is_click = self.infrastructure.is_click()
        if is_click:
            self.handle_mouse_down()

        mouse_up = self.state == 'mouse_down' and not is_click
        if mouse_up:
            self.handle_mouse_up()

    def handle_mouse_down(self) -> None:
        self.state = 'mouse_down'

    def handle_mouse_up(self) -> None:
        if self.state == 'mouse_down':
            self.state = 'click'
            return

        self.state = 'mouse_up'

    def handle_state(self, state: str) -> None:
        match state:
            case 'mouse_over':
                self.infrastructure.play_hover_sound()
