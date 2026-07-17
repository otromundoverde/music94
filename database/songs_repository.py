from database.database import Database


class SongRepository:

    def __init__(self):

        self.db = Database()

    # ---------------------------------------------------------

    def clear(self):

        cursor = self.db.cursor()

        cursor.execute("DELETE FROM songs")

        self.db.commit()

    # ---------------------------------------------------------

    def insert_song(self, song):

        cursor = self.db.cursor()

        cursor.execute(
            """
            INSERT INTO songs(

                title,
                artist,
                album,
                album_artist,
                genre,
                year,
                track,
                disc,
                composer,
                label,
                country,
                duration,
                bitrate,
                sample_rate,
                channels,
                bpm,
                musical_key,
                camelot,
                energy,
                danceability,
                acousticness,
                instrumentalness,
                speechiness,
                loudness,
                dynamic_range,
                replaygain,
                mood,
                filename,
                extension,
                folder,
                path,
                filesize,
                cover_path,
                date_added,
                last_modified

            )
            VALUES(

                :title,
                :artist,
                :album,
                :album_artist,
                :genre,
                :year,
                :track,
                :disc,
                :composer,
                :label,
                :country,
                :duration,
                :bitrate,
                :sample_rate,
                :channels,
                :bpm,
                :musical_key,
                :camelot,
                :energy,
                :danceability,
                :acousticness,
                :instrumentalness,
                :speechiness,
                :loudness,
                :dynamic_range,
                :replaygain,
                :mood,
                :filename,
                :extension,
                :folder,
                :path,
                :filesize,
                :cover_path,
                :date_added,
                :last_modified

            )
            """,
            song,
        )

    # ---------------------------------------------------------

    def insert_library(self, library):

        self.clear()

        for song in library:

            self.insert_song(song)

        self.db.commit()

    # ---------------------------------------------------------

    def load_library(self):

        cursor = self.db.cursor()

        cursor.execute(
            """
            SELECT *
            FROM songs
            ORDER BY artist, album, track
            """
        )

        rows = cursor.fetchall()

        return [dict(row) for row in rows]