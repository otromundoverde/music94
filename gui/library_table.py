from PySide6.QtCore import Signal

from PySide6.QtWidgets import (
    QAbstractItemView,
    QHeaderView,
    QTableWidget,
    QTableWidgetItem,
)


class LibraryTable(QTableWidget):

    song_selected = Signal(list)

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

        self.setAlternatingRowColors(True)

        self.verticalHeader().setVisible(False)

        self.itemSelectionChanged.connect(
            self.selection_changed
        )

    # ====================================================

    def load_library(self, songs):

        self.setRowCount(len(songs))

        for row, song in enumerate(songs):

            for column, value in enumerate(song):

                item = QTableWidgetItem(str(value))

                self.setItem(
                    row,
                    column,
                    item,
                )

    # ====================================================

    def selection_changed(self):

        row = self.currentRow()

        if row < 0:
            return

        song = []

        for column in range(self.columnCount()):

            item = self.item(row, column)

            if item:

                song.append(item.text())

            else:

                song.append("")

        self.song_selected.emit(song)

    # ====================================================

    def clear_library(self):

        self.setRowCount(0)