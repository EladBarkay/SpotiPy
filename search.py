import typing
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


x = Searcher()
print(x.all_artists())
