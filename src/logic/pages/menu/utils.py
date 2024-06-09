from typing import Callable

from src.logic.app_elements.elements.container import Container
from src.logic.app_elements.elements.input import Input
from src.logic.app_elements.elements.button import Button

from src.logic.pages.actions import Action


def get_menu_params(menu: Container) -> dict[str, dict[str, any]]:
    elements_list = menu.elements.values()
    params = {
        'frame': {
            'pos': menu.pos,
            'size': menu.size,
        },
        'elements': {element.text: {
            'position': element.pos,
            'state': element.state
        } for element in elements_list},
    }

    return params


def draw_container(container: Container, tool: any) -> None:
    container_params = get_menu_params(container)
    tool.draw_container(container_params['frame'],
                        container_params['elements'])

