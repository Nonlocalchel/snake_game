import os

from pathlib import Path


def passage(dir_name: str, folder: str):
    for element in os.scandir(folder):
        if element.is_dir():
            if element.name == dir_name:
                yield folder
            else:
                yield from passage(dir_name, element.path)


def get_proj_path() -> str | bytes:
    path = Path().resolve()
    path_parts = path.parts
    return os.path.join(*path_parts[:path_parts.index('snake_game') + 1])


def get_media_path(proj_path: str) -> str:
    media_path = next(passage('media', proj_path))
    return os.path.join(media_path, 'media')


def concatenation_path(path: str, element: str) -> str | bytes | None:
    new_path = os.path.join(path, element)
    if os.path.exists(path):
        return new_path
    else:
        return
