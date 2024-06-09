from enum import Enum


class Action(Enum):
    SHOW_CONF = 'show_conf'
    GO_TO_PLAY = 'go-to_game'
    GO_TO_RESULT = 'go-to_result'
    GO_TO_MENU = 'go-to_menu'
    INPUT = 'input'
    QUIT = 'quit'

    @classmethod
    def menu_actions(cls):
        menu_actions = {
            'Играть': cls.SHOW_CONF,
            'Настройки': cls.GO_TO_RESULT,
            'Выйти': cls.QUIT
        }
        return menu_actions

    @classmethod
    def start_actions(cls):
        start_actions = {
            'Введите имя': cls.INPUT.value,
            'Старт': cls.GO_TO_PLAY
        }
        return start_actions
