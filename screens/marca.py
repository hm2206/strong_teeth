from app import App
from PyQt5.QtGui import QShowEvent
from PyQt5.QtCore import QEvent, QPoint
from PyQt5.QtWidgets import QPushButton, QFrame, QTableWidget, QTableWidgetItem
from PyQt5 import uic
from models.marca import Marca
from configs.db import session


class MarcaFrame(QFrame):

    table: QTableWidget
    btn_plus: QPushButton

    def __init__(self, app: App, parent=None):
        super(MarcaFrame, self).__init__(parent=parent)
        uic.loadUi("ui/marca_frame.ui", self)
        self._app = app

        self.btn_plus.clicked.connect(self.action_create)
        self.table.doubleClicked.connect(self.action_edit)

    def showEvent(self, evt: QShowEvent):
        self.load()
        return super().showEvent(evt)

    def action_create(self, evt: QEvent):
        from dialogs.marca_dialog import MarcaDialog
        self._app.app_screen.set_enabled_window(False)
        self.msg = MarcaDialog(self._app, self, title="Crear Marca")
        self.msg.show()

    def action_edit(self, evt: QEvent):
        from dialogs.marca_dialog import MarcaDialog
        self._app.app_screen.set_enabled_window(False)
        row = self.table.selectionModel().currentIndex().row()
        id = self.table.item(row, 0).text()
        marca = session.query(Marca).get(id)
        self.msg = MarcaDialog(self._app, self, title="Editar Marca")
        self.msg.load(marca)
        self.msg.show()

    def load(self):
        self.data = session.query(Marca).all()
        self.table.setRowCount(self.data.__len__())
        for index, item in enumerate(self.data):
            marca: Marca = item
            self.table.setItem(index, 0, QTableWidgetItem(str(marca.id)))
            self.table.setItem(index, 1, QTableWidgetItem(str(marca.nombre)))
            self.table.setItem(
                index, 2, QTableWidgetItem(str(marca.descripcion)))
