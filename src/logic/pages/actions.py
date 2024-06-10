from enum import Enum


class Action(Enum):
    SHOW_CONF = 'show_conf'
    SHOW_MENU = 'show_menu'
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
    def conf_actions(cls):
        conf_actions = {
            'Введите имя': cls.INPUT.value,
            'Старт': cls.GO_TO_PLAY
        }
        return conf_actions
