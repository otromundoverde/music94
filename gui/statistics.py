from gui.library_data import SONGS


class Statistics:

    @staticmethod
    def total_songs():
        return len(SONGS)

    @staticmethod
    def total_artists():
        artistas = {song[1] for song in SONGS}
        return len(artistas)

    @staticmethod
    def total_albums():
        albumes = {song[2] for song in SONGS}
        return len(albumes)

    @staticmethod
    def total_genres():
        generos = {song[4] for song in SONGS}
        return len(generos)