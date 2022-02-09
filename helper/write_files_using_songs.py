import typing
from os import listdir
from os.path import isfile, join
import objects.song as song


def get_songs():
    songs_list: typing.List[song.Song] = []
    songs_folder_path = "C:\\Users\\User\\Desktop\\learn process\\2022-02\\9.2\\SpotiPy\\Resources\\songs"
    song_files_paths = [join(songs_folder_path, f) for f in listdir(songs_folder_path) if isfile(join(songs_folder_path, f))]
    try:
        for song_path in song_files_paths:

            songs_list.append(song.load(song_path))
    except Exception as e:
        print(e)

    return songs_list


print(get_songs())
