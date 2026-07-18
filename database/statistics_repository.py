from database.database import Database


class StatisticsRepository:

    def __init__(self):

        self.db = Database()

    # ---------------------------------------------------------

    def total_songs(self):

        cursor = self.db.cursor()

        cursor.execute("SELECT COUNT(*) FROM songs")

        return cursor.fetchone()[0]

    # ---------------------------------------------------------

    def total_artists(self):

        cursor = self.db.cursor()

        cursor.execute("SELECT COUNT(DISTINCT artist) FROM songs")

        return cursor.fetchone()[0]

    # ---------------------------------------------------------

    def total_albums(self):

        cursor = self.db.cursor()

        cursor.execute("SELECT COUNT(DISTINCT album) FROM songs")

        return cursor.fetchone()[0]

    # ---------------------------------------------------------

    def total_genres(self):

        cursor = self.db.cursor()

        cursor.execute("SELECT COUNT(DISTINCT genre) FROM songs")

        return cursor.fetchone()[0]

    # ---------------------------------------------------------

    def total_duration(self):

        cursor = self.db.cursor()

        cursor.execute("SELECT SUM(duration) FROM songs")

        seconds = cursor.fetchone()[0]

        return seconds if seconds else 0