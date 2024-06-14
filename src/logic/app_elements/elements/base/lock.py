class Lock:
    def __init__(self, access=True) -> None:
        super().__init__()
        self._access = access

    @property
    def is_lock(self) -> bool:
        return not self._access

    def lock(self) -> None:
        self._access = False

    def unlock(self) -> None:
        self._access = True
