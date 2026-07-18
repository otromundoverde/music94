from database.database import Database


class QueryEngine:

    def __init__(self):

        self.db = Database()

    # ---------------------------------------------------------

    def execute(self, where="", params=(), order="artist, album, track"):

        cursor = self.db.cursor()

        sql = f"""
            SELECT *
            FROM songs
        """

        if where:

            sql += f"\nWHERE {where}"

        sql += f"\nORDER BY {order}"

        cursor.execute(sql, params)

        return [dict(row) for row in cursor.fetchall()]

    # ---------------------------------------------------------

    def all(self):

        return self.execute()

    # ---------------------------------------------------------

    def artist(self, artist):

        return self.execute(

            "artist = ?",

            (artist,)

        )

    # ---------------------------------------------------------

    def album(self, album):

        return self.execute(

            "album = ?",

            (album,)

        )

    # ---------------------------------------------------------

    def genre(self, genre):

        return self.execute(

            "genre = ?",

            (genre,)

        )

    # ---------------------------------------------------------

    def year_between(self, start, end):

        return self.execute(

            "CAST(year AS INTEGER) BETWEEN ? AND ?",

            (start, end)

        )

    # ---------------------------------------------------------

    def bpm_between(self, minimum, maximum):

        return self.execute(

            "bpm BETWEEN ? AND ?",

            (minimum, maximum)

        )

    # ---------------------------------------------------------

    def key(self, musical_key):

        return self.execute(

            "musical_key = ?",

            (musical_key,)

        )

    # ---------------------------------------------------------

    def label(self, label):

        return self.execute(

            "label = ?",

            (label,)

        )

    # ---------------------------------------------------------

    def country(self, country):

        return self.execute(

            "country = ?",

            (country,)

        )