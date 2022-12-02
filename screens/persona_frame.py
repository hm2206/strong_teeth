from app import App
from PyQt5.QtGui import QShowEvent
from PyQt5.QtCore import QEvent
from PyQt5.QtWidgets import QPushButton, QFrame, QTableWidget, QTableWidgetItem
from PyQt5 import uic
from configs.db import session
from models.persona import genero_to_str, Persona, str_to_genero


class PersonaFrame(QFrame):

    table: QTableWidget
    btn_plus: QPushButton

    def __init__(self, app: App, parent=None):
        super(PersonaFrame, self).__init__(parent=parent)
        uic.loadUi("ui/persona_frame.ui", self)
        self._app = app

        self.btn_plus.clicked.connect(self.action_create)
        self.table.doubleClicked.connect(self.action_edit)

    def showEvent(self, evt: QShowEvent):
        self.load()
        return super().showEvent(evt)

    def action_create(self, evt: QEvent):
        from dialogs.persona_dialog import PersonaDialog
        self._app.app_screen.set_enabled_window(False)
        self.msg = PersonaDialog(self._app, self, title="Crear Persona")
        self.msg.show()

    def action_edit(self, evt: QEvent):
        from dialogs.persona_dialog import PersonaDialog
        self._app.app_screen.set_enabled_window(False)
        row = self.table.selectionModel().currentIndex().row()
        id = self.table.item(row, 0).text()
        persona = session.query(Persona).get(id)
        self.msg = PersonaDialog(self._app, self, title="Editar Persona")
        self.msg.show()
        self.msg.load(persona)

    def load(self):
        self.data = session.query(Persona).all()
        self.table.setRowCount(self.data.__len__())
        for index, item in enumerate(self.data):
            entity: Persona = item
            self.table.setItem(index, 0, QTableWidgetItem(str(entity.id)))
            self.table.setItem(index, 1, QTableWidgetItem(entity.nombres))
            self.table.setItem(
                index, 2, QTableWidgetItem(entity.apellido_paterno))
            self.table.setItem(
                index, 3, QTableWidgetItem(entity.apellido_materno))
            self.table.setItem(
                index, 4, QTableWidgetItem(entity.numero_identidad))
            self.table.setItem(
                index, 5, QTableWidgetItem(str(entity.fecha_nacimiento)))
            self.table.setItem(
                index, 6, QTableWidgetItem(genero_to_str(entity.genero)))
            self.table.resizeColumnsToContents()
