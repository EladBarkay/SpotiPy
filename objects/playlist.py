import typing


class Playlist:
    id: str
    name: str
    songs: typing.List[str]  # list of song id's

    def __init__(self, _id: str, name: str, songs: typing.List[str]):
        self.id = _id
        self.name = name
        self.songs = songs