import operator
import typing

import consts.general
import objects.song as Song
from objects.spotipy_generic_obj import SpotipyGenericObj
from helper.write_them_all import get_songs


class Searcher:
    songs: typing.List[Song.Song]

    def __init__(self):
        self.songs = get_songs()

    def all_artists(self):
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

    def all_artist_songs(self, artist_id: str):
        artist_songs: typing.List[Song.Song] = []
        for song in self.songs:
            if artist_id in [artist.id for artist in song.artists]:
                artist_songs.append(song)
        return sorted(artist_songs, key=operator.attrgetter(consts.general.POPULARITY), reverse=True)

    def artist_top_songs(self, artist_id: str, countToShow=10):
        all_songs = self.all_artist_songs(artist_id)
        return all_songs[:countToShow]


x = Searcher()
for i in x.artist_top_songs("3MZsBdqDrRTJihTHQrO6Dq"):
    print(i.__dict__)
