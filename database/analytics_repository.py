from database.database import Database


class AnalyticsRepository:

    def __init__(self):

        self.db = Database()

    # ---------------------------------------------------------

    def top_artists(self, limit=10):

        cursor = self.db.cursor()

        cursor.execute(
            """
            SELECT artist,
                   COUNT(*) AS total
            FROM songs
            GROUP BY artist
            ORDER BY total DESC, artist ASC
            LIMIT ?
            """,
            (limit,),
        )

        return [dict(row) for row in cursor.fetchall()]

    # ---------------------------------------------------------

    def top_albums(self, limit=10):

        cursor = self.db.cursor()

        cursor.execute(
            """
            SELECT album,
                   COUNT(*) AS total
            FROM songs
            GROUP BY album
            ORDER BY total DESC, album ASC
            LIMIT ?
            """,
            (limit,),
        )

        return [dict(row) for row in cursor.fetchall()]

    # ---------------------------------------------------------

    def top_genres(self, limit=10):

        cursor = self.db.cursor()

        cursor.execute(
            """
            SELECT genre,
                   COUNT(*) AS total
            FROM songs
            GROUP BY genre
            ORDER BY total DESC, genre ASC
            LIMIT ?
            """,
            (limit,),
        )

        return [dict(row) for row in cursor.fetchall()]

    # ---------------------------------------------------------

    def top_labels(self, limit=10):

        cursor = self.db.cursor()

        cursor.execute(
            """
            SELECT label,
                   COUNT(*) AS total
            FROM songs
            WHERE label <> ''
            GROUP BY label
            ORDER BY total DESC, label ASC
            LIMIT ?
            """,
            (limit,),
        )

        return [dict(row) for row in cursor.fetchall()]

    # ---------------------------------------------------------

    def top_countries(self, limit=10):

        cursor = self.db.cursor()

        cursor.execute(
            """
            SELECT country,
                   COUNT(*) AS total
            FROM songs
            WHERE country <> ''
            GROUP BY country
            ORDER BY total DESC, country ASC
            LIMIT ?
            """,
            (limit,),
        )

        return [dict(row) for row in cursor.fetchall()]