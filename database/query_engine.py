from database.database import Database


class QueryEngine:

    def __init__(self):

        self.db = Database()

    # ---------------------------------------------------------

    def execute(self, where="", params=(), order="artist, album, track"):

        cursor = self.db.cursor()

        sql = """
            SELECT *
            FROM songs
        """

        if where:

            sql += "\nWHERE " + where

        sql += "\nORDER BY " + order

        cursor.execute(sql, params)

        return [dict(row) for row in cursor.fetchall()]

    # ---------------------------------------------------------

    def search(

        self,

        artist=None,
        album=None,
        genre=None,
        year_min=None,
        year_max=None,
        bpm_min=None,
        bpm_max=None,
        musical_key=None,
        label=None,
        country=None,

    ):

        where = []

        params = []

        if artist:

            where.append("artist = ?")
            params.append(artist)

        if album:

            where.append("album = ?")
            params.append(album)

        if genre:

            where.append("genre = ?")
            params.append(genre)

        if year_min is not None:

            where.append("CAST(year AS INTEGER) >= ?")
            params.append(year_min)

        if year_max is not None:

            where.append("CAST(year AS INTEGER) <= ?")
            params.append(year_max)

        if bpm_min is not None:

            where.append("bpm >= ?")
            params.append(bpm_min)

        if bpm_max is not None:

            where.append("bpm <= ?")
            params.append(bpm_max)

        if musical_key:

            where.append("musical_key = ?")
            params.append(musical_key)

        if label:

            where.append("label = ?")
            params.append(label)

        if country:

            where.append("country = ?")
            params.append(country)

        return self.execute(

            " AND ".join(where),

            tuple(params)

        )

    # ---------------------------------------------------------

    def all(self):

        return self.execute()