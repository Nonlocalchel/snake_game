from dataclasses import dataclass


@dataclass
class Player:
    name: str = 'default_user'
    score: int = 0
    time: any = None
