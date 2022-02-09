import typing
import json
import consts.general as consts


def load(song_path):
    file = open(song_path, 'r')
    decoded_file = json.JSONDecoder().decode(file.read())[consts.TRACK]
    _id = decoded_file[consts.ID]
    name = decoded_file[consts.NAME]
    popularity = decoded_file[consts.POPULARITY]
    album = decoded_file[consts.ALBUMS]
    albums: list = [i[consts.ID] for i in dict(decoded_file[consts.ALBUMS]).values()]

    return


class Song:
    id: str
    name: str
    popularity: int
    album: str  # list of album id's
    artists: typing.List[str]  # list of artist id's

    def __init__(self, _id: str, name: str, popularity: int, album: str, artists: typing.List[str]):
        self.id = _id
        self.name = name
        self.popularity = popularity
        self.album = album
        self.artists = artists


