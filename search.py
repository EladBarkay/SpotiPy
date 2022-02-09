import typing
import objects.song as song
from helper.write_them_all import get_songs


class Searcher:
    songs: typing.List[song.Song]

    def __init__(self):
        self.songs = get_songs()

    
