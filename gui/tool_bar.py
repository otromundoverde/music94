from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QToolBar


class Music94ToolBar(QToolBar):
    def __init__(self):
        super().__init__("Herramientas")

        self.setMovable(False)
        self.setToolButtonStyle(Qt.ToolButtonTextOnly)

        actualizar = QAction("Actualizar", self)
        buscar = QAction("Buscar", self)
        sincronizar = QAction("Sincronizar", self)
        exportar = QAction("Exportar", self)
        configuracion = QAction("Configuración", self)

        self.addAction(actualizar)
        self.addSeparator()
        self.addAction(buscar)
        self.addSeparator()
        self.addAction(sincronizar)
        self.addSeparator()
        self.addAction(exportar)
        self.addSeparator()
        self.addAction(configuracion)