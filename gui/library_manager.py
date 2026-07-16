from gui.library_data import SONGS


class LibraryManager:

    def __init__(self):
        self.library = SONGS.copy()

    # ======================================================
    # BIBLIOTECA
    # ======================================================

    def get_library(self):
        return self.library

    def song_count(self):
        return len(self.library)

    def clear(self):
        self.library = []

    def add_song(self, song):

        if len(song) != 6:
            return False

        self.library.append(song)
        return True

    def remove_song(self, index):

        if 0 <= index < len(self.library):
            del self.library[index]
            return True

        return False

    def update_song(self, index, song):

        if 0 <= index < len(self.library):
            self.library[index] = song
            return True

        return False

    # ======================================================
    # BÚSQUEDA
    # ======================================================

    def search(self, text):

        if not text:
            return self.library

        text = text.lower()

        results = []

        for song in self.library:

            if any(text in str(value).lower() for value in song):
                results.append(song)

        return results

    # ======================================================
    # FILTROS
    # ======================================================

    def filter(
        self,
        songs=None,
        genre="Todos los géneros",
        decade="Todos los años",
    ):

        if songs is None:
            songs = self.library

        results = songs

        if genre != "Todos los géneros":

            results = [
                song
                for song in results
                if song[4] == genre
            ]

        if decade != "Todos los años":

            if decade == "1970s":

                results = [
                    song
                    for song in results
                    if 1970 <= int(song[3]) <= 1979
                ]

            elif decade == "1980s":

                results = [
                    song
                    for song in results
                    if 1980 <= int(song[3]) <= 1989
                ]

            elif decade == "1990s":

                results = [
                    song
                    for song in results
                    if 1990 <= int(song[3]) <= 1999
                ]

            elif decade == "2000s":

                results = [
                    song
                    for song in results
                    if 2000 <= int(song[3]) <= 2009
                ]

        return results

    # ======================================================
    # ORDENAMIENTO
    # ======================================================

    def sort(self, songs=None, order="Ordenar por"):

        if songs is None:
            songs = self.library

        results = songs.copy()

        if order == "Título":
            results.sort(key=lambda s: s[0])

        elif order == "Artista":
            results.sort(key=lambda s: s[1])

        elif order == "Álbum":
            results.sort(key=lambda s: s[2])

        elif order == "Año":
            results.sort(key=lambda s: s[3])

        return results

    # ======================================================
    # CONSULTAS
    # ======================================================

    def artists(self):

        return sorted(
            list(
                {
                    song[1]
                    for song in self.library
                }
            )
        )

    def albums(self):

        return sorted(
            list(
                {
                    song[2]
                    for song in self.library
                }
            )
        )

    def genres(self):

        return sorted(
            list(
                {
                    song[4]
                    for song in self.library
                }
            )
        )

    def decades(self):

        decades = []

        for song in self.library:

            decade = str(song[3])[:3] + "0s"

            if decade not in decades:
                decades.append(decade)

        decades.sort()

        return decades

    # ======================================================
    # ESTADÍSTICAS
    # ======================================================

    def statistics(self):

        return {

            "songs": len(self.library),

            "artists": len(self.artists()),

            "albums": len(self.albums()),

            "genres": len(self.genres()),

            "decades": len(self.decades()),
        }