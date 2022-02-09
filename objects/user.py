import typing
import consts.general as consts
import consts.custom_exceptions as ex
from file_managment import save_and_load as manager
from spotipy_generic_obj import SpotipyGenericObj


class User(SpotipyGenericObj):
    is_premium: bool
    playlists: typing.Dict[str, str]  # playlist name to playlist id

    def __init__(self, _id: str, name: str, is_premium: bool, playlists: typing.Dict[str, str]):
        super().__init__(_id, name)
        self.is_premium = is_premium
        self.playlists = playlists

    def _object_path(self):
        return f'{consts.FILES_ROOT_PATH}\\{consts.SONGS}\\{consts.SONG_FILE_START}{self.id}{consts.JSON_FILE_TYPE}'

    def save(self):
        manager.save(self, self._object_path())

    def add_playlist(self, p_name, p_id):
        if p_id in self.playlists.keys():
            raise ex.PlaylistNameAlreadyExistsError()
        self.playlists[p_name] = p_id
