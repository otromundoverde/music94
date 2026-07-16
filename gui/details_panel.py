from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QFormLayout,
)


class DetailsPanel(QWidget):

    def __init__(self):
        super().__init__()

        layout = QFormLayout()

        self.song = QLabel("-")
        self.artist = QLabel("-")
        self.album = QLabel("-")
        self.year = QLabel("-")
        self.genre = QLabel("-")
        self.duration = QLabel("-")
        self.path = QLabel("-")

        layout.addRow("Canción", self.song)
        layout.addRow("Artista", self.artist)
        layout.addRow("Álbum", self.album)
        layout.addRow("Año", self.year)
        layout.addRow("Género", self.genre)
        layout.addRow("Duración", self.duration)
        layout.addRow("Ruta", self.path)

        self.setLayout(layout)

    def update_song(self, song):

        self.song.setText(song[0])
        self.artist.setText(song[1])
        self.album.setText(song[2])
        self.year.setText(song[3])
        self.genre.setText(song[4])
        self.duration.setText(song[5])
        self.path.setText("No disponible")