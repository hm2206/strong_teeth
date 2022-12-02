from app import App
from PyQt5.QtGui import QShowEvent
from PyQt5.QtCore import QEvent
from PyQt5.QtWidgets import QPushButton, QFrame, QTableWidget, QTableWidgetItem
from PyQt5 import uic
from configs.db import session
from models.usuario import Usuario
from utils.usuario_util import role_to_str, estado_to_str
from models.persona import Persona


class UsuarioFrame(QFrame):

    table: QTableWidget
    btn_plus: QPushButton

    def __init__(self, app: App, parent=None):
        super(UsuarioFrame, self).__init__(parent=parent)
        uic.loadUi("ui/usuario_frame.ui", self)
        self._app = app

        self.btn_plus.clicked.connect(self.action_create)
        self.table.doubleClicked.connect(self.action_edit)

    def showEvent(self, evt: QShowEvent):
        self.load()
        return super().showEvent(evt)

    def action_create(self, evt: QEvent):
        from dialogs.usuario_dialog import UsuarioDialog
        self._app.app_screen.set_enabled_window(False)
        self.msg = UsuarioDialog(self._app, self, title="Crear Usuario")
        self.msg.show()

    def action_edit(self, evt: QEvent):
        from dialogs.usuario_dialog import UsuarioDialog
        self._app.app_screen.set_enabled_window(False)
        row = self.table.selectionModel().currentIndex().row()
        id = self.table.item(row, 0).text()
        entity = session.query(Usuario).get(id)
        self.msg = UsuarioDialog(self._app, self, title="Editar Usuario")
        self.msg.show()
        self.msg.load(entity)

    def load(self):
        self.data = session.query(Usuario).all()
        self.table.setRowCount(self.data.__len__())
        for index, item in enumerate(self.data):
            entity: Usuario = item
            persona: Persona = entity.persona
            self.table.setItem(index, 0, QTableWidgetItem(str(entity.id)))
            self.table.setItem(index, 1, QTableWidgetItem(entity.email))
            self.table.setItem(index, 2, QTableWidgetItem(
                persona.display_nombre()))
            self.table.setItem(index, 3, QTableWidgetItem(
                role_to_str(entity.role)))
            self.table.setItem(index, 4, QTableWidgetItem(
                estado_to_str(entity.estado)))
            self.table.resizeColumnsToContents()
