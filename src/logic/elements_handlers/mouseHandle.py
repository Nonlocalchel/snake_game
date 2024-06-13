from src.interface.infrastructure import Infrastructure

from src.logic.app_elements.elements.button import Button


class MouseHandle:
    def __init__(self, infrastructure: Infrastructure) -> None:
        self.infrastructure = infrastructure

    def handle(self, element: Button, elem_position: tuple[float, float]) -> None:
        self.handle_pos(element, elem_position)
        if element.is_hover:
            self.handle_click(element)

    def handle_pos(self, element: Button, position: tuple[float, float]) -> None:
        hover = self.infrastructure.check_mouse(element.text, position)
        if hover:
            self.handle_mouse_over(element)
        else:
            element.state = None

    def handle_mouse_over(self, element: Button) -> None:
        if element.is_hover:
            return

        self.infrastructure.play_hover_sound()
        element.state = 'hover'

    def handle_click(self, element: Button) -> None:
        if element.state == 'click':
            self.handle_mouse_up(element)

        is_click = self.infrastructure.is_click()
        if is_click:
            self.handle_mouse_down(element)

        mouse_up = element.state == 'mouse_down' and not is_click
        if mouse_up:
            self.handle_mouse_up(element)

    @staticmethod
    def handle_mouse_down(element: Button) -> None:
        element.state = 'mouse_down'

    @staticmethod
    def handle_mouse_up(element: Button) -> None:
        if element.state == 'mouse_down':
            element.state = 'click'
            return

        element.state = 'mouse_up'

