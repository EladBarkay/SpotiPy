import typing
import consts.general as consts
import consts.custom_exceptions as ex
import search
from objects.playlist import Playlist
from file_managment import save_and_load as manager
from objects.spotipy_generic_obj import SpotipyGenericObj


class User(SpotipyGenericObj):
    is_premium: bool
    playlists: typing.List[Playlist]  # playlist id to Playlist

    def __init__(self, _id: str, name: str, is_premium: bool = False, playlists: typing.List[Playlist] = None):
        super().__init__(_id, name)
        self.is_premium = is_premium
        self.playlists = playlists if playlists is not None else []

    def _object_path(self):
        return f'{consts.FILES_ROOT_PATH}\\{consts.USERS}\\' \
               f'{consts.USER_FILE_START}{self.name}{consts.PICKLE_FILE_TYPE}'

    def save(self):
        manager.save(self, self._object_path())

    def add_playlist(self, playlist: Playlist):
        if len(self.playlists) >= consts.FREE_ACCOUNT_MAX_PLAYLIST_COUNT and not self.is_premium:
            raise ex.InvalidFreeUserOperation(
                f"Free user cant have more than {consts.FREE_ACCOUNT_MAX_PLAYLIST_COUNT} playlists")
        if playlist.name in [p.name for p in self.playlists]:
            raise ex.PlaylistNameAlreadyExistsError()
        self.playlists.append(playlist)

    def add_song_to_playlist(self, song_id: str, p_name: str):
        if p_name not in [p.name for p in self.playlists]:
            raise ex.PlaylistNotExistsError()
        p_index = [i for i in range(len(self.playlists)) if self.playlists[i].name == p_name][0]

        if len(self.playlists[p_index].songs) >= consts.FREE_ACCOUNT_MAX_SONGS_IN_PLAYLIST_COUNT \
                and not self.is_premium:
            raise ex.InvalidFreeUserOperation(
                f"Free user cant have more than {consts.FREE_ACCOUNT_MAX_SONGS_IN_PLAYLIST_COUNT} songs "
                f"in one playlist")
        self.playlists[p_index].add_song(song_id)

    def search(self, searcher: search.Searcher, search_type, **search_params):
        results = searcher.get(search_type, **search_params)
        if not self.is_premium:
            return results[:consts.FREE_ACCOUNT_MAX_RESULTS_FROM_SEARCH]
        return results
