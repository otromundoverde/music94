from pathlib import Path

from gui.metadata_reader import MetadataReader


class MusicImporter:

    SUPPORTED_EXTENSIONS = (
        ".mp3",
        ".flac",
        ".wav",
        ".ogg",
        ".m4a",
        ".aac",
        ".aiff",
        ".ape",
        ".opus",
        ".wma",
    )

    def __init__(self):

        self.files = []

        self.library = []

        self.reader = MetadataReader()

    # ---------------------------------------------------

    def clear(self):

        self.files.clear()

        self.library.clear()

    # ---------------------------------------------------

    def scan_folder(self, folder):

        self.clear()

        folder = Path(folder)

        if not folder.exists():

            return []

        for file in folder.rglob("*"):

            if (
                file.is_file()
                and file.suffix.lower() in self.SUPPORTED_EXTENSIONS
            ):

                self.files.append(file)

        self.files.sort()

        return self.files

    # ---------------------------------------------------

    def build_library(self):

        self.library.clear()

        for file in self.files:

            metadata = self.reader.read(file)

            if metadata is not None:

                self.library.append(metadata)

        return self.library

    # ---------------------------------------------------

    def import_folder(self, folder):

        self.scan_folder(folder)

        return self.build_library()

    # ---------------------------------------------------

    def total_files(self):

        return len(self.files)

    # ---------------------------------------------------

    def total_songs(self):

        return len(self.library)

    # ---------------------------------------------------

    def get_files(self):

        return self.files.copy()

    # ---------------------------------------------------

    def get_library(self):

        return self.library.copy()