from app import App
from PyQt5.QtGui import QShowEvent
from PyQt5.QtCore import QEvent
from PyQt5.QtWidgets import QPushButton, QFrame, QTableWidget, QTableWidgetItem
from PyQt5 import uic
from configs.db import session
from models.proveedor import Proveedor
from models.persona import Persona


class ProveedorFrame(QFrame):

    table: QTableWidget
    btn_plus: QPushButton

    def __init__(self, app: App, parent=None):
        super(ProveedorFrame, self).__init__(parent=parent)
        uic.loadUi("ui/proveedor_frame.ui", self)
        self._app = app

        self.btn_plus.clicked.connect(self.action_create)
        self.table.doubleClicked.connect(self.action_edit)

    def showEvent(self, evt: QShowEvent):
        self.load()
        return super().showEvent(evt)

    def action_create(self, evt: QEvent):
        from dialogs.proveedor_dialog import ProveedorDialog
        self._app.app_screen.set_enabled_window(False)
        self.msg = ProveedorDialog(self._app, self, title="Crear Proveedor")
        self.msg.show()

    def action_edit(self, evt: QEvent):
        from dialogs.proveedor_dialog import ProveedorDialog
        self._app.app_screen.set_enabled_window(False)
        row = self.table.selectionModel().currentIndex().row()
        id = self.table.item(row, 0).text()
        proveedor = session.query(Proveedor).get(id)
        self.msg = ProveedorDialog(self._app, self, title="Editar Proveedor")
        self.msg.show()
        self.msg.load(proveedor)

    def load(self):
        self.data = session.query(Proveedor).all()
        self.table.setRowCount(self.data.__len__())
        for index, item in enumerate(self.data):
            proveedor: Proveedor = item
            self.table.setItem(index, 0, QTableWidgetItem(str(proveedor.id)))
            self.table.setItem(
                index, 1, QTableWidgetItem(str(proveedor.razon_social)))
            self.table.setItem(
                index, 2, QTableWidgetItem(str(proveedor.ruc)))
            self.table.setItem(
                index, 3, QTableWidgetItem(str(proveedor.direccion)))
            self.table.setItem(
                index, 4, QTableWidgetItem(str(proveedor.telefono)))
            persona = proveedor.representante
            txt_representante = self.display_representante(persona)
            self.table.setItem(index, 5, QTableWidgetItem(txt_representante))

    def display_representante(self, persona: Persona):
        return f"{persona.nombres} {persona.apellido_paterno} {persona.apellido_materno}"
