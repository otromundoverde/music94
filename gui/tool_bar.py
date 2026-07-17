from PySide6.QtCore import Signal

from PySide6.QtGui import QAction

from PySide6.QtWidgets import QToolBar


class Music94ToolBar(QToolBar):

    import_requested = Signal()

    update_requested = Signal()

    sync_requested = Signal()

    analyze_requested = Signal()

    export_requested = Signal()

    settings_requested = Signal()

    def __init__(self):

        super().__init__()

        self.setMovable(False)

        self.setFloatable(False)

        self.setObjectName("MainToolbar")

        # =====================================================
        # BOTONES
        # =====================================================

        self.action_update = QAction("Actualizar", self)

        self.action_import = QAction("Importar", self)

        self.action_sync = QAction("Sincronizar", self)

        self.action_analyze = QAction("Analizar", self)

        self.action_export = QAction("Exportar", self)

        self.action_settings = QAction("Configuración", self)

        # =====================================================
        # TOOLBAR
        # =====================================================

        self.addAction(self.action_update)

        self.addSeparator()

        self.addAction(self.action_import)

        self.addSeparator()

        self.addAction(self.action_sync)

        self.addSeparator()

        self.addAction(self.action_analyze)

        self.addSeparator()

        self.addAction(self.action_export)

        self.addSeparator()

        self.addAction(self.action_settings)

        # =====================================================
        # CONEXIONES
        # =====================================================

        self.action_update.triggered.connect(

            self.update_requested.emit

        )

        self.action_import.triggered.connect(

            self.import_requested.emit

        )

        self.action_sync.triggered.connect(

            self.sync_requested.emit

        )

        self.action_analyze.triggered.connect(

            self.analyze_requested.emit

        )

        self.action_export.triggered.connect(

            self.export_requested.emit

        )

        self.action_settings.triggered.connect(

            self.settings_requested.emit

        )