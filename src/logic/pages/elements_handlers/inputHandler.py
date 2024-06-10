from src.interface.infrastructure import Infrastructure

from src.logic.app_elements.elements.container import Input


class InputHandler:
    def __init__(self, infrastructure: Infrastructure) -> None:
        self.infrastructure = infrastructure

    @staticmethod
    def input(text_input: Input, key: str) -> None:
        if key == 'escape':
            text_input.clear()
        else:
            text_input.change(key)

        text_input.unfocus() if text_input.is_empty else text_input.focus()
