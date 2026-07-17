def create_schema(connection):

    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS songs (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            title TEXT,
            artist TEXT,
            album TEXT,
            album_artist TEXT,

            genre TEXT,

            year TEXT,

            track TEXT,
            disc TEXT,

            composer TEXT,

            label TEXT,

            country TEXT,

            duration REAL,

            bitrate INTEGER,

            sample_rate INTEGER,

            channels INTEGER,

            bpm REAL,

            musical_key TEXT,

            camelot TEXT,

            energy REAL,

            danceability REAL,

            acousticness REAL,

            instrumentalness REAL,

            speechiness REAL,

            loudness REAL,

            dynamic_range REAL,

            replaygain REAL,

            mood TEXT,

            filename TEXT,

            extension TEXT,

            folder TEXT,

            path TEXT UNIQUE,

            filesize INTEGER,

            cover_path TEXT,

            date_added TEXT,

            last_modified TEXT

        )
        """
    )

    connection.commit()