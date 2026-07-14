from PySide6.QtWidgets import QTableWidget
from PySide6.QtWidgets import QTableWidgetItem

from gui.library_data import SONGS


class LibraryTable(QTableWidget):

    def __init__(self):
        super().__init__()

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

        self.load_songs()

    def load_songs(self):

        self.setRowCount(len(SONGS))

        for row, song in enumerate(SONGS):

            for column, value in enumerate(song):

                self.setItem(row, column, QTableWidgetItem(value))