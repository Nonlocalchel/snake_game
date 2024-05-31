from src.interface.infrastructure import Infrastructure
from src.pages.display import Display

from src.pages.actions import Action

from .utils import figure_real_pos

from .gameMenu import GameMenu
from .button import Button
from .input import Input


class Menu(Display):
    """Контролирует цикл меню"""

    def __init__(self, infrastructure: Infrastructure) -> None:
        self.infrastructure = infrastructure
        self.is_running = True
        self.menu = GameMenu(Action.menu_actions(), (-0.05, 0.2))
        self.start_menu = GameMenu(Action.start_actions(), (0.5, 0.5))
        self.action = None
        self.page = 'menu'

    def process_events(self) -> None:
        """Обработка ввода от пользователя"""
        if self.infrastructure.is_quit_event():
            self.is_running = False

        key = self.infrastructure.check_pressed_key()

        menu = self.menu
        if menu.get_lock:
            menu = self.start_menu
            name_input = menu.elements['input']
            name_input.change(key)

            if key == 'escape':
                self.menu.unlock()
                self.start_menu.lock()

        elements = self.menu.elements
        for element in elements:
            if not type(element) is Button:
                continue

            position = figure_real_pos(menu.pos, element.pos)

            state = self.infrastructure.check_mouse(element.text, position)
            element.state = state

            if element.is_hover:
                self.infrastructure.make_hover_sound()

                new_state = self.infrastructure.is_click(element.text, position)
                element.state = new_state or state

                if element.is_click:
                    self.action = element.click()


    def render(self) -> None:
        """Обновление экрана: перерисовка меню"""
        self.infrastructure.fill_bg(image='gold_snake.jpg')

        menu_params = self.menu.params
        self.infrastructure.draw_menu(menu_params['frame'], menu_params['elements'])

        if self.menu.lock:
            start_menu_params = self.start_menu.params
            self.infrastructure.draw_menu(start_menu_params['frame'], start_menu_params['elements'])

        self.infrastructure.update_and_tick()

    def update_state(self) -> None:
        """Вычисление следующего состояния всех объектов на экране"""
        self.menu.unlock()
        self.start_menu.lock()

        if self.action == Action.GO_TO_PLAY:
            self.menu.lock()
            self.start_menu.unlock()

        if 'go-to' in self.action:
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
