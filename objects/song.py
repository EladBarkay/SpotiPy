import typing
import json
import consts.general as consts
from objects.spotipy_generic_obj import SpotipyGenericObj


def load(song_path):
    file = open(song_path, 'r')
    decoded_file = json.JSONDecoder().decode(file.read())[consts.TRACK]
    _id = decoded_file[consts.ID]
    name = decoded_file[consts.NAME]
    popularity = decoded_file[consts.POPULARITY]
    album = SpotipyGenericObj(decoded_file[consts.ALBUM][consts.ID], decoded_file[consts.ALBUM][consts.NAME])
    artists: typing.List[SpotipyGenericObj] = \
        [SpotipyGenericObj(i[consts.ID], i[consts.NAME]) for i in decoded_file[consts.ARTISTS]]
    return Song(_id, name, popularity, album, artists)


class Song(SpotipyGenericObj):
    popularity: int
    album: SpotipyGenericObj
    artists: typing.List[SpotipyGenericObj]  # list of artist id's

    def __init__(self, _id: str, name: str, popularity: int, album: SpotipyGenericObj,
                 artists: typing.List[SpotipyGenericObj]):
        super().__init__(_id, name)
        self.popularity = popularity
        self.album = album
        self.artists = artists


