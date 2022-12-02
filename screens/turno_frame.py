from app import App
from PyQt5.QtGui import QShowEvent
from PyQt5.QtCore import QEvent
from PyQt5.QtWidgets import QPushButton, QFrame, QTableWidget, QTableWidgetItem
from PyQt5 import uic
from configs.db import session
from models.turno import Turno


class TurnoFrame(QFrame):

    table: QTableWidget
    btn_plus: QPushButton

    def __init__(self, app: App, parent=None):
        super(TurnoFrame, self).__init__(parent=parent)
        uic.loadUi("ui/turno_frame.ui", self)
        self._app = app

        self.btn_plus.clicked.connect(self.action_create)
        self.table.doubleClicked.connect(self.action_edit)

    def showEvent(self, evt: QShowEvent):
        self.load()
        return super().showEvent(evt)

    def action_create(self, evt: QEvent):
        from dialogs.turno_dialog import TurnoDialog
        self._app.app_screen.set_enabled_window(False)
        self.msg = TurnoDialog(self._app, self, title="Crear Turno")
        self.msg.show()

    def action_edit(self, evt: QEvent):
        from dialogs.turno_dialog import TurnoDialog
        self._app.app_screen.set_enabled_window(False)
        row = self.table.selectionModel().currentIndex().row()
        id = self.table.item(row, 0).text()
        entity = session.query(Turno).get(id)
        self.msg = TurnoDialog(self._app, self, title="Editar Turno")
        self.msg.load(entity)
        self.msg.show()

    def load(self):
        self.data = session.query(Turno).all()
        self.table.setRowCount(self.data.__len__())
        for index, item in enumerate(self.data):
            entity: Turno = item
            self.table.setItem(index, 0, QTableWidgetItem(str(entity.id)))
            self.table.setItem(index, 1, QTableWidgetItem(str(entity.nombre)))
            self.table.setItem(
                index, 2, QTableWidgetItem(str(entity.descripcion)))
