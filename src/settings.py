from .services.pathFinder import get_proj_path, get_media_path, concatenation_path

# SIZE
WIDTH = 10
HEIGHT = 10
SCALE = 40
RADIUS = 5
ELEMENT_SIZE = 38
# SPEED
FPS = 60
INITIAL_SPEED_DELAY = FPS // 2
# COLORS
SNAKE_COLOR = "yellow"
APPLE_COLOR = "red"
SCORE_COLOR = "white"
SCREEN_COLOR = "black"
GAME_OVER_COLOR = "red"
SIMPLE_TEXT_COLOR = 'white'
UNFOCUSED_TEXT_COLOR = 'grey'
HOVER_TEXT_COLOR = (229, 167, 13)
# PATH
ROOT_PATH = get_proj_path()
MEDIA_PATH = get_media_path(ROOT_PATH)
IMG_PATH = concatenation_path(MEDIA_PATH, 'img')
SOUND_PATH = concatenation_path(MEDIA_PATH, 'sounds')
