from src.logic.app_elements.elements.container import Container
from src.logic.app_elements.elements.input import Input
from src.logic.app_elements.elements.button import Button

from src.logic.actions import Action


def get_menu_params(menu: Container) -> dict:
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


def handle_input(text_input: Input, key: str) -> None:
    if key == 'escape':
        text_input.clear()
    else:
        text_input.change(key)

    text_input.unfocus() if text_input.is_empty else text_input.focus()


def select_conf_action(key: str) -> Action | None:
    if key == 'escape':
        return None
    elif key == 'return':
        return Action.GO_TO_PLAY
    else:
        return Action.SHOW_CONF


def select_menu_action(key: str) -> Action | None:
    if key == 'return':
        return Action.SHOW_CONF
    elif key == 'escape':
        return Action.QUIT
    else:
        return None


def handle_mouse_on(element: Button, action: ()) -> None:
    if not element.is_hover:
        action()
        element.state = 'hover'


def handle_mouse_down(element: Button) -> None:
    element.state = 'click'


def handle_mouse_up(element: Button, action: ()) -> None:
    if action:
        action()
    else:
        print(f'click on {element.text}')
