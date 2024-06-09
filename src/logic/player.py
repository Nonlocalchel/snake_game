import time

from dataclasses import dataclass


@dataclass
class Player:
    name: str
    score: int
    date: time.struct_time | None
