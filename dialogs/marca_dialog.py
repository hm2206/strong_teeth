from app import App
from PyQt5.QtGui import QShowEvent
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QDialog, QLabel, QPushButton, QLineEdit
from PyQt5 import uic
from message_boxs.critical_message_box import CriticalMessageBox
from screens.marca import MarcaFrame
from models.marca import Marca
from configs.db import session
from message_boxs.success_message_box import SuccessMessageBox
import sqlalchemy


class MarcaDialog(QDialog):

    lbl_title: QLabel
    btn_save: QPushButton
    input_nombre: QLineEdit
    input_descripcion: QLineEdit

    def __init__(self, app: App, parent: MarcaFrame, title=""):
        super(MarcaDialog, self).__init__(parent=parent)
        uic.loadUi("ui/marca_dialog.ui", self)
        self._app = app
        self._frm_parent = parent
        self.marca = Marca()
        self.lbl_title.setText(title)
        self.btn_save.clicked.connect(self.save)

    def showEvent(self, evt: QShowEvent):
        return super().showEvent(evt)

    def closeEvent(self, evt: QShowEvent):
        self._app.app_screen.set_enabled_window(True)
        return super().closeEvent(evt)

    def load(self, marca: Marca):
        self.marca = marca
        self.input_nombre.setText(marca.nombre)
        self.input_descripcion.setText(marca.descripcion)

    def save(self, evt: QObject):
        self.marca.nombre = self.input_nombre.text()
        self.marca.descripcion = self.input_descripcion.text()
        session.add(self.marca)

        try:
            session.commit()
            SuccessMessageBox(text="Los datos se guardaron").exec()
            self._frm_parent.load()
            self.close()
        except Exception:
            session.rollback()
            CriticalMessageBox(text="No se pudo guardar los datos").exec()
