from src.logic.app_elements.interface_elements.interactionBox import InteractionBox
from src.logic.app_elements.interface_elements import button, textInput

app_element = textInput.Input | button.Button


def get_box_params(box: InteractionBox) -> dict[str, dict]:
    box_params = {
        'pos': box.pos,
        'size': box.size,
    }

    elements_params = {}
    for element in box.elements:
        if type(element) is InteractionBox:
            box = element
            elements_params['box'] = get_box_params(box)

        elements_params[element.text] = {
            'position': element.pos,
            'state': element.state
        }

    return {'box_params': box_params, 'elements_params': elements_params}


def get_available_box(boxs: any) -> InteractionBox:
    for box in boxs:
        if box.is_lock:
            continue

        return box


def get_input(box: InteractionBox) -> textInput.Input:
    for element in box.elements:
        if type(element) is textInput.Input:
            return element


def set_default_lock(boxs: any) -> None:
    for box in boxs:
        box.unlock()
