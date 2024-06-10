from src.interface.infrastructure import Infrastructure

from src.logic.app_elements.elements.container import Container, Button


class MouseHandler:
    def __init__(self, infrastructure: Infrastructure) -> None:
        self.infrastructure = infrastructure

    def hover(self, element: Button, container: Container) -> None:
        position = container.get_real_element_pos(element)
        hover = self.infrastructure.check_mouse(element.text, position)
        if hover:
            self.mouse_on(element)
        else:
            element.state = None

    def click(self, element: Button) -> None:
        mouse_down = self.infrastructure.is_click()
        if mouse_down:
            self.mouse_down(element)

        mouse_up = element.is_click and not mouse_down
        if mouse_up:
            self.mouse_up(element)

    def mouse_on(self, element: Button) -> None:
        if element.is_hover:
            return

        self.infrastructure.play_hover_sound()
        element.state = 'hover'

    @staticmethod
    def mouse_down(element: Button) -> None:
        element.state = 'click'

    @staticmethod
    def mouse_up(element: Button) -> None:
        element.state = None
