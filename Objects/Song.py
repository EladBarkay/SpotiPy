import typing
import Album
import Artist


class Song:
    id: str
    name: str
    popularity: int
    # TODO: track: typing.Dict[TRACK_TYPE: str, Track]
    albums: typing.List[Album]
    artists: typing.List[Artist]

