import pygame
from src.constant import *


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

    def update_and_tick(self) -> None:
        pygame.display.update()
        self.clock.tick(FPS)

    @staticmethod
    def quit() -> None:
        pygame.quit()
