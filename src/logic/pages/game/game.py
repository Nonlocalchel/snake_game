from src.logic.pages.page import Page
from src.interface.infrastructure import Infrastructure
from .utils import *


class Game(Page):
    """Контролирует главный цикл игры"""

    def __init__(self, infrastracture: Infrastructure) -> None:
        self.infrastructure = infrastracture
        self.snake = Snake(get_center_element())
        self.apple = gen_apple(self.snake)
        self.tick_counter = 0
        self.score = 0
        self.snake_speed_delay = INITIAL_SPEED_DELAY
        self.is_running = True
        self.is_game_over = False
        self.player = None
        self.name = 'game'
        self.action = None

    def process_events(self) -> None:
        """Обработка ввода от пользователя"""
        if self.infrastructure.is_quit_event():
            self.is_running = False

        new_direction = self.infrastructure.get_pressed_arrow()
        if new_direction:
            self.snake.set_direction(new_direction)

    def render(self) -> None:
        """Обновление экрана: перерисовка змейки, яблока, баллов и game over"""
        self.infrastructure.fill_bg()
        for e in self.snake.deque:
            self.infrastructure.draw_element(e.x, e.y, SNAKE_COLOR)

        self.infrastructure.draw_element(self.apple.x, self.apple.y, APPLE_COLOR)
        self.infrastructure.draw_score(self.player.name, self.score)

        if self.is_game_over:
            self.infrastructure.draw_game_over()

        self.infrastructure.update_and_tick()

    def update_state(self) -> None:
        """Вычисление следующего состояния всех объектов на экране"""
        if self.is_game_over:
            return

        self.tick_counter += 1
        if not self.tick_counter % self.snake_speed_delay:
            head = self.snake.get_new_head()
            if is_valid_head(head, self.snake):
                self.snake.enqueue(head)
                if head == self.apple:
                    self.score += 1
                    self.apple = gen_apple(self.snake)
                else:
                    self.snake.dequeue()
            else:
                self.is_game_over = True

    def loop(self):
        """Главный цикл игры"""
        while self.is_running:
            self.process_events()
            self.update_state()
            if self.name != 'game':
                break

            self.render()
        else:
            self.infrastructure.quit()
