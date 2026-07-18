from models.song import Song


class SongFactory:

    @staticmethod
    def empty():

        return Song()

    @staticmethod
    def from_metadata(metadata):

        song = Song()

        if metadata is None:
            return song

        for field in song.__dataclass_fields__:

            if field in metadata:

                setattr(song, field, metadata[field])

        return song

    @staticmethod
    def to_dict(song):

        return song.__dict__.copy()