import typing
from objects.user import User
from objects.playlist import Playlist


class Artist(User):
    albums: typing.List[str]
    genre: str

    def __init__(self, _id: str, name: str,
                 playlists: typing.List[Playlist] = None, albums: typing.List[str] = None, genre: str = None):
        playlists = playlists if playlists is not None else []
        albums = albums if albums is not None else []
        super().__init__(_id, name, True, playlists)
        self.albums = albums
        self.genre = genre
