from PySide6.QtCore import Qt

from PySide6.QtGui import QAction

from PySide6.QtWidgets import (
    QToolBar,
)


class Music94ToolBar(QToolBar):

    def __init__(self):
        super().__init__("Toolbar")

        self.setMovable(False)

        self.setFloatable(False)

        self.setToolButtonStyle(Qt.ToolButtonTextOnly)

        self.build_actions()

        self.build_toolbar()

    def build_actions(self):

        self.action_update = QAction("Actualizar", self)
        self.action_import = QAction("Importar", self)
        self.action_sync = QAction("Sincronizar", self)

        self.action_scan = QAction("Analizar", self)

        self.action_export = QAction("Exportar", self)

        self.action_settings = QAction("Configuración", self)

        self.action_update.setToolTip(
            "Actualizar la biblioteca"
        )

        self.action_import.setToolTip(
            "Importar música o carpetas"
        )

        self.action_sync.setToolTip(
            "Sincronizar Spotify"
        )

        self.action_scan.setToolTip(
            "Analizar biblioteca"
        )

        self.action_export.setToolTip(
            "Exportar datos"
        )

        self.action_settings.setToolTip(
            "Configuración general"
        )

    def build_toolbar(self):

        self.addAction(self.action_update)

        self.addAction(self.action_import)

        self.addAction(self.action_sync)

        self.addSeparator()

        self.addAction(self.action_scan)

        self.addSeparator()

        self.addAction(self.action_export)

        self.addSeparator()

        self.addAction(self.action_settings)