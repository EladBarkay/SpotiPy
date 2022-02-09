import typing


class Album:
    id: str
    name: str
    songs: typing.List[str]  # list of song id's
    artists: typing.List[str]  # list of artist id's

    def __init__(self, _id: str, name: str, songs: typing.List[str], artists: typing.List[str]):
        self.id = _id
        self.name = name
        self.songs = songs
        self.artists = artists
