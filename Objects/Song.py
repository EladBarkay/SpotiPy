import typing
from Album import Album
from Artist import Artist


class Song:
    id: str
    name: str
    popularity: int
    # TODO: track: typing.Dict[TRACK_TYPE: str, Track]
    albums: typing.List[Album]
    artists: typing.List[Artist]

