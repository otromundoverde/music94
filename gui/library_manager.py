from database.song_repository import SongRepository


class LibraryManager:

    def __init__(self):

        self.repository = SongRepository()

        self.songs = self.repository.load_library()

    # ---------------------------------------------------------

    def load_library(self, library):

        self.repository.insert_library(library)

        self.songs = self.repository.load_library()

    # ---------------------------------------------------------

    def clear(self):

        self.repository.clear()

        self.songs = []

    # ---------------------------------------------------------

    def get_library(self):

        self.songs = self.repository.load_library()

        return list(self.songs)

    # ---------------------------------------------------------

    def query(

        self,

        text="",

        genre="Todos los géneros",

        decade="Todos los años",

        order="Ordenar por",

    ):

        self.songs = self.repository.load_library()

        results = list(self.songs)

        if text:

            text = text.lower()

            results = [

                song

                for song in results

                if (

                    text in str(song["title"]).lower()

                    or text in str(song["artist"]).lower()

                    or text in str(song["album"]).lower()

                )

            ]

        if genre != "Todos los géneros":

            results = [

                song

                for song in results

                if song["genre"] == genre

            ]

        if decade != "Todos los años":

            start = int(decade[:4])

            end = start + 9

            results = [

                song

                for song in results

                if str(song["year"]).isdigit()

                and start <= int(song["year"]) <= end

            ]

        if order == "Título":

            results.sort(key=lambda s: s["title"])

        elif order == "Artista":

            results.sort(key=lambda s: s["artist"])

        elif order == "Álbum":

            results.sort(key=lambda s: s["album"])

        elif order == "Año":

            results.sort(key=lambda s: s["year"])

        return results

    # ---------------------------------------------------------

    def statistics(self):

        self.songs = self.repository.load_library()

        return {

            "songs": len(self.songs),

            "artists": len(set(song["artist"] for song in self.songs)),

            "albums": len(set(song["album"] for song in self.songs)),

            "genres": len(set(song["genre"] for song in self.songs)),

        }