from PySide6.QtWidgets import (
    QAbstractItemView,
    QHeaderView,
    QTableWidget,
    QTableWidgetItem,
)

from gui.library_data import SONGS


class LibraryTable(QTableWidget):

    def __init__(self):
        super().__init__()

        self.setColumnCount(6)

        self.setHorizontalHeaderLabels([
            "Canción",
            "Artista",
            "Álbum",
            "Año",
            "Género",
            "Duración",
        ])

        self.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )

        self.setSelectionBehavior(
            QAbstractItemView.SelectRows
        )

        self.setEditTriggers(
            QAbstractItemView.NoEditTriggers
        )

        self.load_songs()

    def load_songs(self):

        self.setRowCount(len(SONGS))

        for fila, cancion in enumerate(SONGS):

            for columna, valor in enumerate(cancion):

                self.setItem(
                    fila,
                    columna,
                    QTableWidgetItem(valor),
                )