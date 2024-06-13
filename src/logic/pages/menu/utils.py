from src.logic.app_elements.elements.base.container import Container

from src.logic.app_elements.elements import textInput, button

from src.logic.pages.actions import Action

app_element = textInput.Input | button.Button


def get_element_state_for_draw(element: app_element) -> str:
    state = None
    if type(element) is button.Button:
        if element.is_hover:
            state = 'hover'

        if element.is_action:
            state = 'action'

    if type(element) is textInput.Input:
        state = element.state

    return state


def get_menu_params(menu: Container) -> tuple[any, any]:
    frame_params = {
        'pos': menu.pos,
        'size': menu.size,
    }

    elements_params = {}
    for element in menu.elements:
        state = get_element_state_for_draw(element)

        elements_params[element.text] = {
            'position': element.pos,
            'state': state
        }

    return frame_params, elements_params


def is_clickable(element: any) -> bool:
    return hasattr(element, 'is_hover')


def get_clickable_elements(elements: tuple[app_element]) -> filter:
    filtered_iter = filter(is_clickable, elements)
    return filtered_iter


menu_actions = {
    'return': Action.SHOW_CONF,
    'escape': Action.QUIT
}

conf_actions = {
    'return': Action.GO_TO_PLAY,
    'escape': Action.SHOW_MENU
}
