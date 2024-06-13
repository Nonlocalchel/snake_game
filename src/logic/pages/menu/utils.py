from src.logic.app_elements.elements.container import Container, Button, Input

from src.logic.pages.actions import Action

app_element = Input | Button


def get_menu_params(menu: Container) -> tuple[dict, dict]:  # dict[str, dict[str, app_element]]
    elements_list = menu.elements.values()
    params = {
        'frame': {
            'pos': menu.pos,
            'size': menu.size,
        },
        'elements': {element.text: {
            'position': element.pos,
            'state': element.state if type(element) is not Button else
            'action' if element.is_action else
            'hover' if element.is_hover else None
        } for element in elements_list},
    }

    return params['frame'], params['elements']


def is_clickable(element: any) -> bool:
    return hasattr(element, 'is_hover')


def get_clickable_elements(elements: dict[str, Action | str]) -> filter:
    filtered_iter = filter(is_clickable, elements.values())
    return filtered_iter


menu_action = {
    'return': Action.SHOW_CONF,
    'escape': Action.QUIT
}

conf_action = {
    'escape': Action.SHOW_MENU,
    'return': Action.GO_TO_PLAY
}

