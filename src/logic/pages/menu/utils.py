from src.logic.pages.actions import Action

from src.logic.app_elements.elements.interactionBox import InteractionBox

from .configurationBox import ConfigurationBox
from .menuBox import MenuBox

action_config = {
    'menu': {
        'escape': Action.QUIT,
        'return': Action.SHOW_CONF
    },
    'game_conf': {
        'escape': Action.SHOW_MENU,
        'return': Action.GO_TO_PLAY
    }
}


def choose_alt_action(key: str) -> Action | None:
    match key:
        case key if key and len(key) == 1:
            return Action.INPUT


def choose_action(key: str, state: InteractionBox) -> Action | None:
    box_key = 'menu' if type(state) is MenuBox else 'game_conf'
    if box_key:
        box_conf = action_config.get(box_key)
        if box_conf:
            return box_conf.get(key)
    else:
        return choose_alt_action(key)


def get_available_box(*boxs) -> InteractionBox:
    for box in boxs:
        if box.is_lock:
            continue

        return box
