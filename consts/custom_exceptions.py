class PlaylistNameAlreadyExistsError(Exception):
    def __init__(self, msg: str = "Playlist name already exists in this users library"):
        super().__init__(msg)


class InvalidFreeUserOperation(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class PlaylistAlreadyContainsThisSong(Exception):
    def __init__(self, msg: str = None):
        super().__init__(msg)


class PlaylistDoNotContainThisSong(Exception):
    def __init__(self, msg: str = None):
        super().__init__(msg)


class PlaylistNotExistsError(Exception):
    def __init__(self, msg: str = None):
        super().__init__(msg)


class InvalidSearchOption(Exception):
    def __init__(self, msg: str = None):
        super().__init__(msg)


class NotAUserException(Exception):
    def __init__(self, msg: str = None):
        super().__init__(msg)