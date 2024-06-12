from src.interface.infrastructure import Infrastructure

from src.logic.app_elements.elements.container import Container, Button


class MouseHandle:
    def __init__(self, infrastructure: Infrastructure) -> None:
        self.infrastructure = infrastructure

    def handle_pos(self, element: Button, container: Container) -> None:
        position = container.get_real_element_pos(element)
        hover = self.infrastructure.check_mouse(element.text, position)
        if hover:
            self.mouse_over(element)
        else:
            element.state = None

    def mouse_over(self, element: Button) -> None:
        if element.is_hover:
            return

        self.infrastructure.play_hover_sound()
        element.state = 'hover'

    def handle_click(self, element: Button) -> None:
        if element.state == 'click':
            self.mouse_up(element)

        is_click = self.infrastructure.is_click()
        if is_click:
            self.mouse_down(element)

        mouse_up = element.state == 'mouse_down' and not is_click
        if mouse_up:
            self.mouse_up(element)

    @staticmethod
    def mouse_down(element: Button) -> None:
        element.state = 'mouse_down'

    @staticmethod
    def mouse_up(element: Button) -> None:
        if element.state == 'mouse_down':
            element.state = 'click'
            return

        element.state = 'mouse_up'

