import pygame
from src.interface.utils import *

from .elements.containerView import ContainerView
from .elements.textView import TextView

from src.logic.pages.game.directions import Direction
from ..services.pathFinder import concatenation_path


class Infrastructure:
    pygame.locals = filter_key(vars(pygame.constants))

    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode([WIDTH * SCALE, HEIGHT * SCALE])
        pygame.display.set_caption('Ssssnake')
        self.clock = pygame.time.Clock()

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
    def draw_container(self, menu_params: dict, elem_params: dict, shadow: bool = False) -> None:
        cont_view = ContainerView(
            figure_abs_params(*menu_params['size'])
        )

        cont_view._coord = figure_abs_params(*menu_params['pos'])

        cont_surf = cont_view.surface
        for elem_name, elem_data in elem_params.items():
            elem_coord = figure_abs_params(
                *elem_data['position']
            )
            text_view = TextView(elem_name, elem_coord)
            text_view.view = elem_data['state']
            cont_surf.blit(
                text_view.view,
                text_view.geom
            )

        self.screen.blit(
            cont_surf,
            cont_view.coord
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

    def draw_score(self, player_name: str, score: int) -> None:
        score = TextView(f"{player_name}: {score}")
        self.screen.blit(
            score.view,
            (5, 5),
        )

    def draw_game_over(self) -> None:
        messages = []

        messages += [TextView('GAME OVER', figure_center(0, -25), color=GAME_OVER_COLOR)]
        messages += [TextView('SPACE-играть еще раз', figure_center(0, 20), color=GAME_OVER_COLOR)]
        messages += [TextView('ESC-меню', figure_center(0, 60), color=GAME_OVER_COLOR)]

        for message in messages:
            self.screen.blit(
                message.view,
                message.geom
            )

    def play_hover_sound(self) -> None:
        path = concatenation_path(SOUND_PATH, 'button_state/hover_3.mp3')
        self.play_sound(path)

    # help methods
    @staticmethod
    def fix_image_size(image: pygame.Surface) -> pygame.Surface:
        width, height = image.get_size()
        size = figure_image_size(height, width)
        return pygame.transform.scale(image, size)

    @staticmethod
    def load_image(name: str) -> pygame.Surface:
        path = concatenation_path(IMG_PATH, name)
        return pygame.image.load(path)

    @staticmethod
    def play_sound(path: str) -> None:
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(0)

    # update methods
    def update_and_tick(self) -> None:
        pygame.display.update()
        self.clock.tick(FPS)

    # process_events methods
    # check mouse event
    @staticmethod
    def check_mouse(elem, elem_pos) -> None | bool:
        mouse_pos = pygame.mouse.get_pos()

        elem = TextView(elem, figure_abs_params(*elem_pos))

        if elem.geom.collidepoint(mouse_pos):
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
    def get_pressed_key() -> str | None:
        keys = pygame.key.get_pressed()

        if not any(keys) or (keys[pygame.K_LSHIFT] and keys.count(True) == 1):
            pressed_cash.clear()

        pressed_keys = []

        for key in pygame.locals.values():
            if keys[key]:
                pressed_key = pygame.key.name(key)

                if pressed_key not in pressed_cash:
                    pressed_keys += [pressed_key]

        pressed_cash.extend(pressed_keys)

        if pressed_keys:
            to_up = keys[pygame.K_LSHIFT]  # shift_in(pressed_cash)

            if not shift_in(pressed_keys):
                return correct_input(pressed_keys, to_up=to_up)

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
