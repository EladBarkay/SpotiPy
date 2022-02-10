import typing
from objects.spotipy_generic_obj import SpotipyGenericObj
import consts.custom_exceptions as ex


class Playlist(SpotipyGenericObj):
    songs: typing.List[str]  # list of song id's

    def __init__(self, _id: str, name: str, songs: typing.List[str]):
        super().__init__(_id, name)
        self.songs = songs

    def add_song(self, song_id: str):
        if song_id in self.songs:
            raise ex.PlaylistAlreadyContainsThisSong()
        self.songs.append(song_id)

    def remove_song(self, song_id: str):
        if song_id not in self.songs:
            raise ex.PlaylistDoNotContainThisSong()
        self.songs.remove(song_id)
