from enum import Enum


class Action(Enum):
    SHOW_CONF = 'show_conf'
    SHOW_MENU = 'show_menu'
    GO_TO_PLAY = 'go-to_game'
    GO_TO_RESULT = 'go-to_result'
    GO_TO_MENU = 'go-to_menu'
    QUIT = 'quit'

