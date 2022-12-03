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


class ProveedorDialog(QDialog):

    lbl_title: QLabel
    btn_save: QPushButton
    input_razon_social: QLineEdit
    input_ruc: QLineEdit
    input_direccion: QLineEdit
    input_telefono: QLineEdit
    cmb_representante: QComboBox

    def __init__(self, app: App, parent: ProveedorFrame, title=""):
        super(ProveedorDialog, self).__init__(parent=parent)
        uic.loadUi("ui/proveedor_dialog.ui", self)
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
        self.input_razon_social.setText(entity.razon_social)
        self.input_ruc.setText(entity.ruc)
        self.input_direccion.setText(entity.direccion)
        self.input_telefono.setText(entity.telefono)
        text_representante = self.display_representante(entity.representante)
        self.cmb_representante.setCurrentText(text_representante)

    def load_representante(self):
        datos = session.query(Persona).all()
        for item in datos:
            persona: Persona = item
            self.cmb_representante.addItem(persona.display_info(), persona)

    def save(self, evt: QObject):
        persona: Persona = self.cmb_representante.currentData()
        self.entity.razon_social = self.input_razon_social.text()
        self.entity.ruc = self.input_ruc.text()
        self.entity.direccion = self.input_direccion.text()
        self.entity.telefono = self.input_telefono.text()

        if (persona):
            self.entity.representante_id = persona.id

        session.add(self.entity)

        try:
            session.commit()
            SuccessMessageBox(text="Los datos se guardaron").exec()
            self._frm_parent.load()
            self.close()
        except Exception:
            session.rollback()
            CriticalMessageBox(text="No se pudo guardar los datos").exec()
