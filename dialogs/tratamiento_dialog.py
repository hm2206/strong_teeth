from app import App
from PyQt5.QtGui import QShowEvent
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QDialog, QLabel, QPushButton, QLineEdit, QPlainTextEdit, QDoubleSpinBox
from PyQt5 import uic
from message_boxs.critical_message_box import CriticalMessageBox
from screens.tratamiento_frame import TratamientoFrame
from configs.db import session
from message_boxs.success_message_box import SuccessMessageBox
from models.tratamiento import Tratamiento


class TratamientoDialog(QDialog):

    lbl_title: QLabel
    btn_save: QPushButton
    input_nombre: QLineEdit
    txt_descripcion: QPlainTextEdit
    dbl_precio: QDoubleSpinBox

    def __init__(self, app: App, parent: TratamientoFrame, title=""):
        super(TratamientoDialog, self).__init__(parent=parent)
        uic.loadUi("ui/tratamiento_dialog.ui", self)
        self._app = app
        self._frm_parent = parent
        self.entity = Tratamiento()
        self.lbl_title.setText(title)
        self.btn_save.clicked.connect(self.save)

    def showEvent(self, evt: QShowEvent):
        return super().showEvent(evt)

    def closeEvent(self, evt: QShowEvent):
        self._app.app_screen.set_enabled_window(True)
        return super().closeEvent(evt)

    def load(self, entity: Tratamiento):
        self.entity = entity
        self.input_nombre.setText(entity.nombre)
        self.txt_descripcion.setPlainText(entity.descripcion)
        self.dbl_precio.setValue(entity.precio)

    def save(self, evt: QObject):
        self.entity.nombre = self.input_nombre.text()
        self.entity.descripcion = self.txt_descripcion.toPlainText()
        self.entity.precio = self.dbl_precio.value()
        session.add(self.entity)

        try:
            session.commit()
            SuccessMessageBox(text="Los datos se guardaron").exec()
            self._frm_parent.load()
            self.close()
        except Exception:
            session.rollback()
            CriticalMessageBox(text="No se pudo guardar los datos").exec()
