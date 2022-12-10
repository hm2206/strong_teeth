from app import App
from PyQt5.QtGui import QShowEvent
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QDialog, QLabel, QPushButton, QLineEdit, QComboBox
from PyQt5 import uic
from message_boxs.critical_message_box import CriticalMessageBox
from configs.db import session
from message_boxs.success_message_box import SuccessMessageBox
from screens.proveedor_frame import ProveedorFrame
from models.proveedor import Proveedor
from models.persona import Persona


class PacienteCitaDialog(QDialog):

    lbl_title: QLabel
    btn_save: QPushButton

    def __init__(self, app: App, parent: ProveedorFrame, title=""):
        super(PacienteCitaDialog, self).__init__(parent=parent)
        uic.loadUi("ui/paciente_cita_dialog.ui", self)
        self._app = app
        self._frm_parent = parent
        self.entity = Proveedor()
        self.lbl_title.setText(title)
        self.btn_save.clicked.connect(self.save)

    def showEvent(self, evt: QShowEvent):
        self.load_representante()
        return super().showEvent(evt)

    def closeEvent(self, evt: QShowEvent):
        self._app.app_screen.set_enabled_window(True)
        return super().closeEvent(evt)

    def load(self, entity: Proveedor):
        self.entity = entity

    def load_representante(self):
        datos = session.query(Persona).all()
        for item in datos:
            persona: Persona = item

    def save(self, evt: QObject):

        session.add(self.entity)

        try:
            session.commit()
            SuccessMessageBox(text="Los datos se guardaron").exec()
            self._frm_parent.load()
            self.close()
        except Exception:
            session.rollback()
            CriticalMessageBox(text="No se pudo guardar los datos").exec()
