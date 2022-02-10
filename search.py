import operator
import typing

import consts.general
import objects.song as Song
from objects.spotipy_generic_obj import SpotipyGenericObj
from helper.write_them_all import get_songs
import consts.custom_exceptions as ex


class Searcher:
    songs: typing.List[Song.Song]

    def __init__(self):
        self.songs = get_songs()

    def artists(self):
        artists: typing.List[SpotipyGenericObj] = []
        for song in self.songs:
            for artist in song.artists:
                if artist not in artists:
                    artists.append(artist)
        return artists

    def artist_albums(self, artist_id: str):
        albums: typing.List[SpotipyGenericObj] = []
        for song in self.songs:
            if artist_id in [artist.id for artist in song.artists]:
                if song.album not in albums:
                    albums.append(song.album)
        return albums

    def artist_songs(self, artist_id: str):
        return [song for song in self.songs if artist_id in [artist.id for artist in song.artists]]

    def artist_top_songs(self, artist_id: str, countToShow=10):
        all_songs = self.artist_songs(artist_id)
        all_songs.sort(key=operator.attrgetter(consts.general.POPULARITY), reverse=True)
        # git commit -m "func for all songs of an artist, and a func for artist to"
        return all_songs[:countToShow]

    def album_songs(self, album_id):
        return [song for song in self.songs if song.album.id == album_id]

    def get(self, search_type, **search_params):
        func = getattr(self, search_type)
        if func is None:
            raise ex.InvalidSearchOption(f"search module has no {search_type} option")
        return func(**search_params)
