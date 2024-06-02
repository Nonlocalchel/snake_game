from src.interface.infrastructure import Infrastructure
from src.pages.display import Display

from src.pages.actions import Action

from .utils import figure_real_pos, get_menu_params

from .gameMenu import GameMenu
from .button import Button


class Menu(Display):
    """Контролирует цикл меню"""

    def __init__(self, infrastructure: Infrastructure) -> None:
        self.infrastructure = infrastructure
        self.is_running = True
        self.menu = GameMenu(Action.menu_actions(), (-0.05, 0.2), offset=(0.02, 0))
        self.start_menu = GameMenu(Action.start_actions(), (0.25, 0.25), (0.5, 0.4))
        self.action = None
        self.page = 'menu'

    def process_events(self) -> None:
        """Обработка ввода от пользователя"""
        if self.infrastructure.is_quit_event():
            self.is_running = False

        menu = self.menu
        if menu.get_lock:
            menu = self.start_menu
            name_input = menu.elements['input']

            key = self.infrastructure.get_pressed_key()
            if key:
                if key == 'escape':
                    self.menu.unlock()
                    self.start_menu.lock()
                else:
                    name_input.change(key)

        elements = menu.elements
        for element in elements.values():
            if not type(element) is Button:
                continue

            position = figure_real_pos(menu.pos, element.pos)
            mouse_on = self.infrastructure.check_mouse(element.text, position)
            if mouse_on:
                if not element.is_hover:
                    self.infrastructure.play_hover_sound()

                    element.state = 'hover'
            else:
                element.state = None

            if element.is_hover:
                mouse_down = self.infrastructure.is_click()
                if mouse_down:
                    element.state = 'click'

                if element.is_click:
                    self.action = element.click()

    def render(self) -> None:
        """Обновление экрана: перерисовка меню"""
        self.infrastructure.fill_bg(image='gold_snake.jpg')

        menu_params = get_menu_params(self.menu)
        self.infrastructure.draw_menu(menu_params['frame'], menu_params['elements'])

        if self.menu.get_lock:
            start_menu_params = get_menu_params(self.start_menu)
            self.infrastructure.draw_menu(start_menu_params['frame'], start_menu_params['elements'], shadow=True)

        self.infrastructure.update_and_tick()

    def update_state(self) -> None:
        """Вычисление следующего состояния всех объектов на экране"""
        self.menu.unlock()
        self.start_menu.lock()

        if self.action is None:
            return

        if self.action == Action.PLAY.value:
            self.menu.lock()
            self.start_menu.unlock()

        if self.action.startswith('go-to'):
            self.page = self.action.split('_')[1]
            self.is_running = False

    def loop(self):
        """Цикл меню"""
        while self.is_running:
            self.process_events()
            self.update_state()
            self.render()
        else:
            self.infrastructure.quit()
