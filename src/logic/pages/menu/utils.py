from src.logic.pages.actions import Action

from src.logic.app_elements.elements.interactionBox import InteractionBox

from .configurationBox import ConfigurationBox
from .menuBox import MenuBox


def choose_menu_action(key: str) -> Action | None:
    match key:
        case 'return':
            return Action.SHOW_CONF

        case 'escape':
            return Action.QUIT


def choose_conf_action(key: str) -> Action | None:
    match key:
        case 'return':
            return Action.GO_TO_PLAY

        case 'escape':
            return Action.SHOW_MENU

        case key if key and len(key) == 1:
            return Action.INPUT


def choose_action(key: str, state: InteractionBox) -> Action | None:
    if type(state) is MenuBox:
        return choose_menu_action(key)
    else:
        return choose_conf_action(key)