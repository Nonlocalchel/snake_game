from src.logic.pages.actions import Action

from .configurationBox import ConfigurationBox
from .menuBox import MenuBox

page_boxs = ConfigurationBox | MenuBox

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


def choose_box_action(key: str, state: page_boxs) -> Action | None:
    match state:
        case MenuBox():
            box_key = 'menu'

        case ConfigurationBox() | _:
            box_key = 'game_conf'

    if box_key:
        return action_config[box_key].get(key)
