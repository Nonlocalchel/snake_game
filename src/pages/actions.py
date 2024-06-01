from enum import Enum


class Action(Enum):
    PLAY = 'show_conf'
    GO_TO_PLAY = 'go-to_game'
    GO_TO_RESULT = 'go-to_result'
    GO_TO_MENU = 'go-to_menu'
    INPUT = 'input'
    QUIT = 'quit'

    @staticmethod
    def get_values(actions):
        return {name: actions[name].value for name in actions}

    @classmethod
    def menu_actions(cls):
        menu_actions = {
            'Играть': cls.GO_TO_PLAY,
            'Настройки': cls.GO_TO_RESULT,
            'Выйти': cls.QUIT
        }
        return cls.get_values(menu_actions)

    @classmethod
    def start_actions(cls):
        start_actions = {
            'Старт': cls.PLAY,
            'Введите имя': cls.INPUT
        }
        return cls.get_values(start_actions)
