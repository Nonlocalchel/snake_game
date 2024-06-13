from src.logic.pages.actions import Action

menu_actions = {
    'return': Action.SHOW_CONF,
    'escape': Action.QUIT
}

conf_actions = {
    'return': Action.GO_TO_PLAY,
    'escape': Action.SHOW_MENU
}
