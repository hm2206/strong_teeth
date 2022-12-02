from app import App
from PyQt5.QtGui import QShowEvent
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QDialog, QLabel, QPushButton, QLineEdit, QComboBox
from PyQt5 import uic
import bcrypt
from message_boxs.critical_message_box import CriticalMessageBox
from models.persona import Persona
from configs.db import session
from message_boxs.success_message_box import SuccessMessageBox
from screens.persona_frame import PersonaFrame
from models.usuario import Usuario
from utils.usuario_util import estado_to_str, role_to_str, str_to_estado, str_to_role


class UsuarioDialog(QDialog):

    lbl_title: QLabel
    btn_save: QPushButton
    input_email: QLineEdit
    input_password: QLineEdit
    cmb_estado: QComboBox
    cmb_role: QComboBox
    cmb_persona: QComboBox

    def __init__(self, app: App, parent: PersonaFrame, title=""):
        super(UsuarioDialog, self).__init__(parent=parent)
        uic.loadUi("ui/usuario_dialog.ui", self)
        self._app = app
        self._frm_parent = parent
        self.entity = Usuario()
        self.lbl_title.setText(title)
        self.btn_save.clicked.connect(self.save)

    def showEvent(self, evt: QShowEvent):
        self.laod_personas()
        return super().showEvent(evt)

    def closeEvent(self, evt: QShowEvent):
        self._app.app_screen.set_enabled_window(True)
        return super().closeEvent(evt)

    def load(self, entity: Usuario):
        self.entity = entity
        persona: Persona = entity.persona
        self.input_email.setText(entity.email)
        self.input_password.setText(entity.password)
        self.cmb_persona.setCurrentText(persona.display_info())
        self.cmb_role.setCurrentText(role_to_str(entity.role))
        self.cmb_estado.setCurrentText(estado_to_str(entity.estado))

    def laod_personas(self):
        datos = session.query(Persona).all()
        for item in datos:
            persona: Persona = item
            self.cmb_persona.addItem(persona.display_info(), persona)

    def save(self, evt: QObject):
        persona: Persona = self.cmb_persona.currentData()
        self.entity.email = self.input_email.text()

        password_tmp = self.input_password.text()
        if (password_tmp != self.entity.password):
            self.entity.set_password(password_tmp)

        self.entity.persona_id = persona.id
        self.entity.role = str_to_role(self.cmb_role.currentText())
        self.entity.estado = str_to_estado(self.cmb_estado.currentText())
        session.add(self.entity)

        try:
            session.commit()
            SuccessMessageBox(text="Los datos se guardaron").exec()
            self._frm_parent.load()
            self.close()
        except Exception:
            session.rollback()
            CriticalMessageBox(text="No se pudo guardar los datos").exec()
