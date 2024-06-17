import time
from dataclasses import astuple

from src.logic.app_elements.player import Player


class PlayerHandle:
    def __init__(self, *args):
        self._player = Player(*args)

    @property
    def name(self):
        return self._player.name

    @name.setter
    def name(self, value):
        self._player.name = value

    def get_as_tuple(self):
        return astuple(self._player)

    def record_death_time(self):
        seconds = time.time()
        self._player.time = time.localtime(seconds)

    def set_default_state(self):
        self._player.time = None
        self._player.score = 0

    def set_score(self, value):
        self._player.score = value
