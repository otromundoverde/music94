from gui.library_data import SONGS


class LibraryManager:

    def __init__(self):

        self.songs = []

        self.load_demo_library()

    # ---------------------------------------------------------

    def load_demo_library(self):

        self.songs = []

        for song in SONGS:

            self.songs.append({

                "title": song[0],
                "artist": song[1],
                "album": song[2],
                "year": str(song[3]),
                "genre": song[4],
                "duration": song[5],
                "path": "",

            })

    # ---------------------------------------------------------

    def load_library(self, library):

        self.songs = list(library)

    # ---------------------------------------------------------

    def clear(self):

        self.songs = []

    # ---------------------------------------------------------

    def add_song(self, song):

        self.songs.append(song)

    # ---------------------------------------------------------

    def get_library(self):

        return list(self.songs)

    # ---------------------------------------------------------

    def query(

        self,

        text="",

        genre="Todos los géneros",

        decade="Todos los años",

        order="Ordenar por",

    ):

        results = list(self.songs)

        if text:

            text = text.lower()

            results = [

                song

                for song in results

                if (

                    text in song["title"].lower()

                    or text in song["artist"].lower()

                    or text in song["album"].lower()

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

                if song["year"].isdigit()

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

        return {

            "songs": len(self.songs),

            "artists": len(set(song["artist"] for song in self.songs)),

            "albums": len(set(song["album"] for song in self.songs)),

            "genres": len(set(song["genre"] for song in self.songs)),

        }