from src.pages.game_menu.infrastructure_menu import InfrastructureMenu

class Menu:
    """Контролирует главный цикл игры"""
    def __init__(self, infrastructureMenu: InfrastructureMenu) -> None:
        self.infrastructure = infrastructureMenu
        self.is_running=True

    def process_events(self) -> None:
        """Обработка ввода от пользователя"""
        if self.infrastructure.is_quit_event():
            self.is_running = False

    def update_state(self) -> None:
        self.infrastructure.update_display()

    def render(self) -> None:
        """Обновление экрана: перерисовка меню"""
        self.infrastructure.fill_screen()
        self.infrastructure.draw_menu()

    def loop(self):
        """Цикл меню"""
        while self.is_running:
            self.process_events()
            self.update_state()
            self.render()
        self.infrastructure.quit()