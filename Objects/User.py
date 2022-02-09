import consts.general as consts
import pickle
import typing

def load_user(id):
    return {}


class User:
    id: str
    name: str
    is_premium: bool
    playlists: typing.Dict[str, str]  # playlist name to playlist id

    def __init__(self, _id: str, name: str, is_premium: bool, playlists: typing.Dict[str, str]):
        self.id = _id
        self.name = name
        self.is_premium = is_premium
        self.playlists = playlists


