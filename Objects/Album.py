import typing
from Song import Song
from Artist import Artist


class Album:
    id: str
    name: str
    songs: typing.List[str]  # list of song id's
    artists: typing.List[Artist]  # list of artist id's
