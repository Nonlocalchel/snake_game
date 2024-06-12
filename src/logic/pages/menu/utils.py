from src.logic.app_elements.elements.container import Container, Button, Input
from ..actions import Action

app_element = Input | Button


def get_menu_params(menu: Container) -> dict[str, dict[str, app_element]]:
    elements_list = menu.elements.values()
    params = {
        'frame': {
            'pos': menu.pos,
            'size': menu.size,
        },
        'elements': {element.text: {
            'position': element.pos,
            'state':    element.state if type(element) is not Button else
                        'action' if element.is_action else
                        'hover' if element.is_hover else None
        } for element in elements_list},
    }

    return params


def draw_container(container: Container, tool: any) -> None:
    container_params = get_menu_params(container)
    tool.draw_container(container_params['frame'],
                        container_params['elements'])


def is_clickable(element: any) -> bool:
    return hasattr(element, 'is_hover')


def get_clickable_elements(elements: dict[str, Action | str]) -> filter:
    filtered_iter = filter(is_clickable, elements.values())
    return filtered_iter
