from app import App
from PyQt5.QtGui import QShowEvent
from PyQt5.QtCore import QEvent
from PyQt5.QtWidgets import QPushButton, QFrame, QTableWidget, QTableWidgetItem
from PyQt5 import uic
from configs.db import session
from models.persona import Persona
from models.trabajador import Trabajador
from models.turno import Turno


class TrabajadorFrame(QFrame):

    table: QTableWidget
    btn_plus: QPushButton

    def __init__(self, app: App, parent=None):
        super(TrabajadorFrame, self).__init__(parent=parent)
        uic.loadUi("ui/trabajador_frame.ui", self)
        self._app = app

        self.btn_plus.clicked.connect(self.action_create)
        self.table.doubleClicked.connect(self.action_edit)

    def showEvent(self, evt: QShowEvent):
        self.load()
        return super().showEvent(evt)

    def action_create(self, evt: QEvent):
        from dialogs.trabajo_dialog import TrabajoDialog
        self._app.app_screen.set_enabled_window(False)
        self.msg = TrabajoDialog(self._app, self, title="Crear Trabajador")
        self.msg.show()

    def action_edit(self, evt: QEvent):
        from dialogs.trabajo_dialog import TrabajoDialog
        self._app.app_screen.set_enabled_window(False)
        row = self.table.selectionModel().currentIndex().row()
        id = self.table.item(row, 0).text()
        entity = session.query(Trabajador).get(id)
        self.msg = TrabajoDialog(self._app, self, title="Editar Trabajador")
        self.msg.show()
        self.msg.load(entity)

    def load(self):
        self.data = session.query(Trabajador).all()
        self.table.setRowCount(self.data.__len__())
        for index, item in enumerate(self.data):
            entity: Trabajador = item
            persona: Persona = entity.persona
            turno: Turno = entity.turno

            self.table.setItem(index, 0, QTableWidgetItem(str(entity.id)))
            self.table.setItem(index, 1, QTableWidgetItem(
                persona.display_nombre()))
            self.table.setItem(index, 2, QTableWidgetItem(turno.nombre))
            self.table.setItem(
                index, 3, QTableWidgetItem(entity.numero_essalud))
            self.table.resizeColumnsToContents()