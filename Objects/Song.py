import typing
from Album import Album
from Artist import Artist


class Song:
    id: str
    name: str
    popularity: int
    # TODO: track: typing.Dict[TRACK_TYPE: str, Track]
    albums: typing.List[str]  # list of album id's
    artists: typing.List[str]  # list of artist id's

    def __init__(self, _id: str, name: str, popularity: int, albums: typing.List[str], artists: typing.List[str]):
        self.id = _id
        self.name = name
        self.popularity = popularity
        self.albums = albums
        self.artists = artists


