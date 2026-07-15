from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QFrame,
    QVBoxLayout,
    QGridLayout,
    QLineEdit,
)

from gui.statistics import Statistics


class Header(QWidget):

    def __init__(self):
        super().__init__()

        principal = QVBoxLayout()

        titulo = QLabel("MUSIC94")
        titulo.setAlignment(Qt.AlignCenter)

        fuente = titulo.font()
        fuente.setPointSize(18)
        fuente.setBold(True)
        titulo.setFont(fuente)

        subtitulo = QLabel("Tu biblioteca musical personal")
        subtitulo.setAlignment(Qt.AlignCenter)

        buscador = QLineEdit()
        buscador.setPlaceholderText("Buscar canciones, artistas o álbumes...")

        linea1 = QFrame()
        linea1.setFrameShape(QFrame.HLine)

        linea2 = QFrame()
        linea2.setFrameShape(QFrame.HLine)

        estadisticas = QGridLayout()

        estadisticas.addWidget(QLabel("Canciones"), 0, 0)
        estadisticas.addWidget(QLabel(str(Statistics.total_songs())), 0, 1)

        estadisticas.addWidget(QLabel("Artistas"), 1, 0)
        estadisticas.addWidget(QLabel(str(Statistics.total_artists())), 1, 1)

        estadisticas.addWidget(QLabel("Álbumes"), 2, 0)
        estadisticas.addWidget(QLabel(str(Statistics.total_albums())), 2, 1)

        estadisticas.addWidget(QLabel("Géneros"), 3, 0)
        estadisticas.addWidget(QLabel(str(Statistics.total_genres())), 3, 1)

        principal.addWidget(linea1)
        principal.addWidget(titulo)
        principal.addWidget(subtitulo)
        principal.addWidget(buscador)
        principal.addSpacing(10)
        principal.addLayout(estadisticas)
        principal.addWidget(linea2)

        self.setLayout(principal)