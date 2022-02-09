class PlaylistNameAlreadyExistsError(Exception):

    def __init__(self, msg: str = "Playlist name already exists in this users library"):
        super().__init__(msg)
