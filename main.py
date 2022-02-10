import objects.artist
import objects.user
import search


def main():
    s = search.Searcher()
    artists = s.artists()
    for a in artists:
        user = objects.artist.Artist(a.id, a.name)
        user.albums = s.artist_albums(artist_id=a.id)
        user.save()

    artist = objects.user.load("Avihu Pinchasov Rhythm Club")
    print(artist)


if __name__ == '__main__':
    main()
