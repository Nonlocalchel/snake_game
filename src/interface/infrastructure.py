import pygame
from src.constant import *
from src.utils import *


class Infrastructure:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode([WIDTH * SCALE, HEIGHT * SCALE])
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, SCALE)

    @staticmethod
    def is_quit_event() -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('quit event')
                return True
        return False

    def fill_bg(self, image: str = None) -> None:
        if image:
            bg_pic = pygame.image.load(image)
            bg_pic = self.fix_image_size(bg_pic)
            self.screen.blit(bg_pic, (-43, 0))
        else:
            self.screen.fill(SCREEN_COLOR)

    @staticmethod
    def fix_image_size(image: pygame.Surface) -> pygame.Surface:
        height, width = image.get_height(), image.get_width()
        if height > width:
            coef = height / width
            return pygame.transform.scale(image, (WIDTH * SCALE, HEIGHT * coef * SCALE))
        else:
            coef = width / height
            return pygame.transform.scale(image, (WIDTH * coef * SCALE, HEIGHT * SCALE))

    @staticmethod
    def get_brd_box(size, bg_color: str = SCREEN_COLOR) -> pygame.Surface:
        menu_surf = pygame.Surface(size, pygame.SRCALPHA)
        menu_surf.fill((0, 0, 0, 0))
        menu_rect = menu_surf.get_rect(left=0, centery=HEIGHT * SCALE * 0.3)
        pygame.draw.rect(menu_surf, bg_color, menu_rect, border_radius=get_scale_radius())
        pygame.draw.rect(menu_surf, SIMPLE_TEXT_COLOR, menu_rect, True, border_radius=get_scale_radius())
        return menu_surf

    def update_and_tick(self) -> None:
        pygame.display.update()
        self.clock.tick(FPS)

    @staticmethod
    def quit() -> None:
        pygame.quit()
