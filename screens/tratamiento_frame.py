from app import App
from PyQt5.QtGui import QShowEvent
from PyQt5.QtCore import QEvent
from PyQt5.QtWidgets import QPushButton, QFrame, QTableWidget, QTableWidgetItem
from PyQt5 import uic
from configs.db import session
from models.turno import Turno
from models.tratamiento import Tratamiento


class TratamientoFrame(QFrame):

    table: QTableWidget
    btn_plus: QPushButton

    def __init__(self, app: App, parent=None):
        super(TratamientoFrame, self).__init__(parent=parent)
        uic.loadUi("ui/tratamiento_frame.ui", self)
        self._app = app

        self.btn_plus.clicked.connect(self.action_create)
        self.table.doubleClicked.connect(self.action_edit)

    def showEvent(self, evt: QShowEvent):
        self.load()
        return super().showEvent(evt)

    def action_create(self, evt: QEvent):
        from dialogs.tratamiento_dialog import TratamientoDialog
        self._app.app_screen.set_enabled_window(False)
        self.msg = TratamientoDialog(
            self._app, self, title="Crear Tratamiento")
        self.msg.show()

    def action_edit(self, evt: QEvent):
        from dialogs.tratamiento_dialog import TratamientoDialog
        self._app.app_screen.set_enabled_window(False)
        row = self.table.selectionModel().currentIndex().row()
        id = self.table.item(row, 0).text()
        entity = session.query(Tratamiento).get(id)
        self.msg = TratamientoDialog(
            self._app, self, title="Editar Tratamiento")
        self.msg.show()
        self.msg.load(entity)

    def load(self):
        self.data = session.query(Tratamiento).all()
        self.table.setRowCount(self.data.__len__())
        for index, item in enumerate(self.data):
            entity: Tratamiento = item

            self.table.setItem(index, 0, QTableWidgetItem(str(entity.id)))
            self.table.setItem(index, 1, QTableWidgetItem(entity.nombre))
            self.table.setItem(index, 2, QTableWidgetItem(entity.descripcion))
            self.table.setItem(index, 3, QTableWidgetItem(str(entity.precio)))
            self.table.resizeColumnsToContents()
