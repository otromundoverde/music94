from gui.library_data import SONGS


class LibraryManager:

    def __init__(self):

        self.songs = SONGS.copy()

    def get_songs(self):

        return self.songs

    def filter(

        self,

        text="",

        genre="Todos los géneros",

        decade="Todos los años",

        order="Ordenar por",

    ):

        results = self.songs

        if text:

            text = text.lower()

            results = [

                song

                for song in results

                if any(text in str(value).lower() for value in song)

            ]

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

        if order == "Título":

            results.sort(key=lambda s: s[0])

        elif order == "Artista":

            results.sort(key=lambda s: s[1])

        elif order == "Álbum":

            results.sort(key=lambda s: s[2])

        elif order == "Año":

            results.sort(key=lambda s: s[3])

        return results

    def artists(self):

        artists = []

        for song in self.songs:

            if song[1] not in artists:

                artists.append(song[1])

        return artists

    def albums(self):

        albums = []

        for song in self.songs:

            if song[2] not in albums:

                albums.append(song[2])

        return albums

    def genres(self):

        genres = []

        for song in self.songs:

            if song[4] not in genres:

                genres.append(song[4])

        return genres

    def decades(self):

        decades = []

        for song in self.songs:

            decade = str(song[3])[:3] + "0s"

            if decade not in decades:

                decades.append(decade)

        return decades