import typing
from Song import Song
from Artist import Artist


class Album:
    id: str
    name: str
    songs: typing.List[Song]
    artists: typing.List[Artist]
