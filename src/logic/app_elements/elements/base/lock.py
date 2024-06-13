class Lock:
    def __init__(self):
        super().__init__()
        self._access = True

    @property
    def get_lock(self) -> bool:
        return not self._access

    def lock(self) -> None:
        self._access = False

    def unlock(self) -> None:
        self._access = True
