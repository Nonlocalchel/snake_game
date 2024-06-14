from src.logic.pages.actions import Action


def choose_menu_action(key, default):
    action = default
    if key == 'return':
        action = Action.SHOW_CONF

    if key == 'escape':
        action = Action.QUIT

    return action


def choose_conf_action(key, default):
    action = default
    if key == 'return':
        action = Action.GO_TO_PLAY

    if key == 'escape':
        action = Action.SHOW_MENU

    if key and len(key) == 1:
        action = Action.INPUT

    return action
