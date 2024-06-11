import time
from dataclasses import astuple

from .player import Player


class PlayerHandle:
    def __init__(self, *args):
        self.__player = Player(*args)

    @property
    def name(self):
        return self.__player.name

    @name.setter
    def name(self, value):
        self.__player.name = value

    def get_as_tuple(self):
        return astuple(self.__player)

    def record_death_time(self):
        seconds = time.time()
        self.__player.time = time.localtime(seconds)

    def set_default_state(self):
        self.__player.time = None
        self.__player.score = 0

    def set_score(self, value):
        self.__player.score = value
