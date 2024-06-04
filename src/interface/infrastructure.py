import pygame
from src.interface.utils import *

from .elements.container import Container
from .elements.text_view import TextView

from src.pages.game.directions import Direction


class Infrastructure:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode([WIDTH * SCALE, HEIGHT * SCALE])
        pygame.display.set_caption('Ssssnake')
        self.clock = pygame.time.Clock()
        pygame.locals = filter_key(vars(pygame.constants))

    # render methods
    # for bg
    def fill_bg(self, image: str = '') -> None:
        if image:
            bg_pic = self.load_image(image)
            bg_pic = self.fix_image_size(bg_pic)
            self.screen.blit(bg_pic, (-43, 0))
        else:
            self.screen.fill(SCREEN_COLOR)

    def draw_shadow(self) -> None:
        size = (
            scale(WIDTH, 1),
            scale(HEIGHT, 1)
        )
        shadow = pygame.Surface(size, pygame.SRCALPHA)
        shadow.fill((0, 0, 0, 150))
        self.screen.blit(
            shadow,
            (0, 0)
        )

    # for menu
    def draw_menu(self, menu_params: dict, elem_params: dict, shadow: bool = False) -> None:
        if shadow:
            self.draw_shadow()

        menu_view = Container(
            (scale(WIDTH, menu_params['size'][0]), scale(HEIGHT, menu_params['size'][1]))
        )

        menu_view.coords = (
            scale(WIDTH, menu_params['pos'][0]),
            scale(HEIGHT, menu_params['pos'][1])
        )

        text_views = [TextView(elem, scale_coord(*elem_params[elem])) for elem in elem_params]
        menu_surf = menu_view.surface
        for text_view in text_views:
            text_view.draw(menu_surf)

        self.screen.blit(
            menu_surf,
            menu_view.coords
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
        score = TextView(f"Score: {score}", None)
        self.screen.blit(
            score.text,
            (5, 5),
        )

    def draw_game_over(self) -> None:
        messages = []

        messages += [TextView('GAME OVER', figure_center(0, -25), color=GAME_OVER_COLOR)]
        messages += [TextView('SPACE-играть еще раз', figure_center(0, 20), color=GAME_OVER_COLOR)]
        messages += [TextView('ESC-меню', figure_center(0, 60), color=GAME_OVER_COLOR)]

        for message in messages:
            message.draw(self.screen)

    def play_hover_sound(self) -> None:
        path = concatenation_path(SOUND_PATH, 'button_state/hover.mp3')
        self.play_sound(path)

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

    @staticmethod
    def load_image(name: str) -> pygame.Surface:
        path = concatenation_path(IMG_PATH, name)
        return pygame.image.load(path)

    @staticmethod
    def play_sound(path: str) -> None:
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(0)

    @staticmethod
    def delay_input(time=120):
        pygame.time.wait(time)

    # update methods
    def update_and_tick(self) -> None:
        pygame.display.update()
        self.clock.tick(FPS)

    # process_events methods
    # check mouse event
    @staticmethod
    def check_mouse(text, elem_pos) -> None | bool:
        mouse_pos = pygame.mouse.get_pos()

        view = TextView(text, scale_coord(*elem_pos))

        if view.is_match(mouse_pos):
            return True
        return False

    @staticmethod
    def is_click():
        if pygame.mouse.get_pressed()[0] == 1:
            return True
        return False

    # check keyboard events
    # menu
    @staticmethod
    def get_pressed_key():
        """
        надо проверять диапозон counter  в зависимости от условий прибавлять определенную дельту
        также нужно не забывать, о том то может быть зажата не одна клавиша и индексы хажатых коавиж собирать
        не забывать про SHIFT при нем буквы будут большие
        """
        keys = pygame.key.get_pressed()
        if not any(keys):
            pressed_cash.clear()

        pressed_keys = []

        for key in pygame.locals.values():
            if keys[key]:
                pressed_key = pygame.key.name(key)

                pressed_key = pressed_key[1] if is_tab_number(pressed_key) else pressed_key

                if pressed_key not in pressed_cash:
                    pressed_keys += [pressed_key]

                    pressed_cash.extend(pressed_keys)

        if pressed_keys:
            print(correct_input(pressed_keys))

    # game
    @staticmethod
    def get_pressed_arrow() -> Direction | None:
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
