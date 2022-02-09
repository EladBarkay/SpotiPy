import typing
from objects.spotipy_generic_obj import SpotipyGenericObj


class Playlist(SpotipyGenericObj):
    songs: typing.List[str]  # list of song id's

    def __init__(self, _id: str, name: str, songs: typing.List[str]):
        super().__init__(_id, name)
        self.songs = songs