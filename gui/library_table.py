from PySide6.QtWidgets import (
    QTableWidget,
    QTableWidgetItem,
)

from gui.library_manager import LibraryManager


class LibraryTable(QTableWidget):

    def __init__(self):

        super().__init__()

        self.library = LibraryManager()

        self.show_library()

    def show_library(self):

        self.setColumnCount(6)

        self.setHorizontalHeaderLabels(

            [

                "Canción",

                "Artista",

                "Álbum",

                "Año",

                "Género",

                "Duración",

            ]

        )

        self.load(self.library.get_songs())

    def show_list(self, title, values):

        self.clear()

        self.setColumnCount(1)

        self.setHorizontalHeaderLabels([title])

        self.setRowCount(len(values))

        for row, value in enumerate(values):

            self.setItem(

                row,

                0,

                QTableWidgetItem(value)

            )

    def load(self, songs):

        self.clearContents()

        self.setRowCount(len(songs))

        for row, song in enumerate(songs):

            for column, value in enumerate(song):

                self.setItem(

                    row,

                    column,

                    QTableWidgetItem(str(value))

                )