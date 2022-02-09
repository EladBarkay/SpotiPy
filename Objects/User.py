import typing
import Playlist


class User:
    id: str
    name: str
    password: str
    is_premium: bool
    playlists: typing.Dict[str, Playlist]

