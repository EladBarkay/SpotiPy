import typing

from User import User


class Artist(User):
    albums: typing.List[str]
    genre: str

    def __init__(self, _id: str, name: str, playlists: typing.Dict[str, str], albums: typing.List[str], genre: str):
        super().__init__(_id, name, True, playlists)
        self.albums = albums
        self.genre = genre
