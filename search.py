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

    def artist_albums(self, artist_id: str):
        albums: typing.List[SpotipyGenericObj] = []
        for song in self.songs:
            if artist_id in [artist.id for artist in song.artists]:
                if song.album not in albums:
                    albums.append(song.album)
        return albums


x = Searcher()
for i in x.artist_albums("3MZsBdqDrRTJihTHQrO6Dq"):
    print(i.__dict__)
