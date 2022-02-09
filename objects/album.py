import typing
from objects.spotipy_generic_obj import SpotipyGenericObj


class Album(SpotipyGenericObj):
    id: str
    name: str
    songs: typing.List[str]  # list of song id's
    artists: typing.List[str]  # list of artist id's

    def __init__(self, _id: str, name: str, songs: typing.List[str], artists: typing.List[str]):
        super().__init__(_id, name)
        self.songs = songs
        self.artists = artists
