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

    # render methods
    # for bg
    def fill_bg(self, image: str) -> None:
        if image:
            bg_pic = self.load_image(image)
            bg_pic = self.fix_image_size(bg_pic)
            self.screen.blit(bg_pic, (-43, 0))
        else:
            self.screen.fill(SCREEN_COLOR)

    def draw_shadow(self):
        pass

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

        text_views = [TextView(elem, elem_params[elem]) for elem in elem_params]
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
        pass
        self.screen.blit(
            score.text,
            (5, 5),
        )

    def draw_game_over(self) -> None:
        messages = []

        messages += [TextView('GAME OVER', (0, -25))]
        messages += [TextView('SPACE-играть еще раз', (0, 20))]
        messages += [TextView('ESC-меню', (0, 50))]

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
    def load_image(name):
        path = concatenation_path(IMG_PATH, name)
        return pygame.image.load(path)

    @staticmethod
    def play_sound(path):
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(0)

    # update methods
    def update_and_tick(self) -> None:
        pygame.display.update()
        self.clock.tick(FPS)

    # process_events methods
    # check mouse event
    @staticmethod
    def check_mouse(text, elem_pos) -> None | bool:
        mouse_pos = pygame.mouse.get_pos()

        view = TextView(text, elem_pos)

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
        pass

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
