import pygame
from src.interface.utils import *

from .elements.containerView import ContainerView
from .elements.textView import TextView

from src.logic.pages.game.directions import Direction

from ..services.pathFinder import concatenation_path
from ..services.dumpLoader.jsonMaster import JsonMaster


class Infrastructure:

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
            self.screen.set_alpha(255)
        else:
            self.screen.fill(SCREEN_COLOR)

    def draw_shadow(self) -> None:
        size = (
            scale(WIDTH, 1),
            scale(HEIGHT, 1)
        )
        shadow = pygame.Surface(size)
        shadow.set_alpha(150)
        self.screen.blit(
            shadow,
            (0, 0)
        )

    # for menu
    def draw_box(self, params: dict[str, dict], surf_to_draw: pygame.Surface | None = None) -> None:
        box_params = params['box_params']
        elem_params = params['elements_params']
        if not len(elem_params):
            return

        cont_view = ContainerView(figure_abs_params(*box_params['size']))
        cont_view.coord = figure_abs_params(*box_params['pos'])
        cont_surf = cont_view.view
        for elem_name, elem_data in elem_params.items():
            if elem_name == 'box':
                self.draw_box(elem_params, cont_surf)

            elem_coord = figure_abs_params(
                *elem_data['position']
            )

            text_view = TextView(elem_name, elem_coord)
            text_view.view = transfer_state(elem_data['state'])
            text_view.scale_view()
            cont_surf.blit(
                text_view.view,
                text_view.geom
            )

        surf_to_draw = surf_to_draw or self.screen
        surf_to_draw.blit(
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

    def play_popup_bubble_sound(self) -> None:
        self.play_sound('pop_up_notification.mp3')

    def play_hover_sound(self) -> None:
        self.play_sound('button_state/hover.mp3')

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
        path = concatenation_path(SOUND_PATH, path)
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(0)

    # update methods
    def update_and_tick(self) -> None:
        pygame.display.update()
        self.clock.tick(FPS)

    # process_events methods
    # check mouse event
    @staticmethod
    def check_mouse(elem_text: str, elem_pos: tuple[float, float]) -> bool:
        mouse_pos = pygame.mouse.get_pos()

        elem = TextView(elem_text, figure_abs_params(*elem_pos))
        elem.scale_view()

        if elem.geom.collidepoint(mouse_pos):
            return True
        return False

    @staticmethod
    def is_click() -> bool:
        if pygame.mouse.get_pressed()[0] == 1:
            return True
        return False

    # check keyboard events
    # menu
    @staticmethod
    def get_pressed_key() -> str | None:
        keys = pygame.key.get_pressed()

        to_up = keys[pygame.K_LSHIFT]
        if to_up and keys.count(True) == 1:
            pressed_cash.clear()

        pressed_keys = []
        
        keys_constant = JsonMaster.read_file('../src/interface/keys_constant')
        for key in keys_constant.values():
            selected_key = pygame.key.name(key)
            if keys[key]:
                pressed_keys += [selected_key] if not pressed_cash.count(selected_key) else []
                continue

            if selected_key in pressed_cash:
                pressed_cash.remove(selected_key)

        if pressed_keys:
            pressed_cash.extend(pressed_keys)
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
