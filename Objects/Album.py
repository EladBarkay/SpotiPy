import typing
import Song
from Objects import Artist


class Album:
    id: str
    name: str
    songs: typing.List[Song]
    artists: typing.List[Artist]
    