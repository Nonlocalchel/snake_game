import pygame
from src.interface.elements.utils import *

from .elements.text.button import Button
from .elements.text.message import Message
from .elements.container import Container


from .directions import Direction


class Infrastructure:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode([WIDTH * SCALE, HEIGHT * SCALE])
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('Calibri', figure_font())

    # render methods
    # for bg
    def fill_bg(self, image: str = None) -> None:
        if image:
            bg_pic = pygame.image.load(image)
            bg_pic = self.fix_image_size(bg_pic)
            self.screen.blit(bg_pic, (-43, 0))
        else:
            self.screen.fill(SCREEN_COLOR)

    # for menu
    def draw_menu(self, buttons: dict) -> None:
        menu_surf = Container((scale(WIDTH, 0.5), scale(HEIGHT, 0.6)))
        menu_surf.coords = (-menu_surf.radius, scale(HEIGHT, 0.4) // 2)
        menu_surf.draw_elements(buttons, offset=(10, 0))
        self.screen.blit(
            menu_surf.surface,
            menu_surf.coords
        )

    # for game
    def draw_element(self, x: int, y: int, color: str) -> None:
        pygame.draw.rect(
            self.screen,
            pygame.Color(color),
            (x * SCALE, y * SCALE, ELEMENT_SIZE, ELEMENT_SIZE),
            0,
            RADIUS,
        )

    def draw_score(self, score: int) -> None:
        self.screen.blit(
            self.font.render(f"Score: {score}", True, pygame.Color(SCORE_COLOR)),
            (5, 5),
        )

    def draw_game_over(self) -> None:
        Message('GAME OVER', self.screen, 0, -25).draw()
        Message('SPACE-играть еще раз', self.screen, 0, 20).draw()
        Message('ESC-меню', self.screen, 0, 50).draw()

    def get_buttons(self, btn_params: dict):
        buttons = {}
        for i in btn_params:
            button = Button(i, self.font)
            button.onclick = btn_params[i]
            buttons[i] = button

        return buttons

    # help methods
    @staticmethod
    def fix_image_size(image: pygame.Surface) -> pygame.Surface:
        height, width = image.get_height(), image.get_width()
        if height > width:
            cof = height / width
            return pygame.transform.scale(image, (WIDTH * SCALE, HEIGHT * cof * SCALE))
        else:
            cof = width / height
            return pygame.transform.scale(image, (WIDTH * cof * SCALE, HEIGHT * SCALE))

    # update methods
    def update_and_tick(self) -> None:
        pygame.display.update()
        self.clock.tick(FPS)

    # process_events methods
    # check onclick event
    @staticmethod
    def check_position(elements) -> None:
        position = pygame.mouse.get_pos()
        buttons = elements['buttons']

        for button in buttons.values():
            if button.is_click(position):
                button.click()

    # check keyboard events(snake)
    @staticmethod
    def get_pressed_key() -> Direction | None:
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            return Direction.DOWN
        if key[pygame.K_RIGHT]:
            return Direction.RIGHT
        if key[pygame.K_DOWN]:
            return Direction.UP
        if key[pygame.K_LEFT]:
            return Direction.LEFT
        return None

    # check quit event
    @staticmethod
    def is_quit_event() -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('quit event')
                return True
        return False

    # quit game
    @staticmethod
    def quit() -> None:
        pygame.quit()
