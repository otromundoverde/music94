from database.database import Database


class AnalyticsRepository:

    def __init__(self):

        self.db = Database()

    # ---------------------------------------------------------

    def _query(self, sql, params=()):

        cursor = self.db.cursor()

        cursor.execute(sql, params)

        return [dict(row) for row in cursor.fetchall()]

    # ---------------------------------------------------------

    def top_artists(self, limit=10):

        return self._query(
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

    # ---------------------------------------------------------

    def top_albums(self, limit=10):

        return self._query(
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

    # ---------------------------------------------------------

    def top_genres(self, limit=10):

        return self._query(
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

    # ---------------------------------------------------------

    def top_labels(self, limit=10):

        return self._query(
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

    # ---------------------------------------------------------

    def top_countries(self, limit=10):

        return self._query(
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

    # ---------------------------------------------------------

    def songs_by_year(self):

        return self._query(
            """
            SELECT year,
                   COUNT(*) AS total
            FROM songs
            WHERE year <> ''
            GROUP BY year
            ORDER BY year
            """
        )

    # ---------------------------------------------------------

    def songs_by_decade(self):

        return self._query(
            """
            SELECT
                (CAST(year AS INTEGER)/10)*10 AS decade,
                COUNT(*) AS total
            FROM songs
            WHERE year GLOB '[0-9][0-9][0-9][0-9]'
            GROUP BY decade
            ORDER BY decade
            """
        )

    # ---------------------------------------------------------

    def songs_by_extension(self):

        return self._query(
            """
            SELECT extension,
                   COUNT(*) AS total
            FROM songs
            GROUP BY extension
            ORDER BY total DESC
            """
        )

    # ---------------------------------------------------------

    def songs_by_samplerate(self):

        return self._query(
            """
            SELECT sample_rate,
                   COUNT(*) AS total
            FROM songs
            GROUP BY sample_rate
            ORDER BY sample_rate
            """
        )

    # ---------------------------------------------------------

    def songs_by_bitrate(self):

        return self._query(
            """
            SELECT bitrate,
                   COUNT(*) AS total
            FROM songs
            GROUP BY bitrate
            ORDER BY bitrate
            """
        )