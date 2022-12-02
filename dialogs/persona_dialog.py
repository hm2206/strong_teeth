from app import App
from PyQt5.QtGui import QShowEvent
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QDialog, QLabel, QPushButton, QLineEdit, QDateEdit, QComboBox
from PyQt5 import uic
from message_boxs.critical_message_box import CriticalMessageBox
from models.persona import genero_to_str, Persona, str_to_genero
from configs.db import session
from message_boxs.success_message_box import SuccessMessageBox
from screens.persona_frame import PersonaFrame


class PersonaDialog(QDialog):

    lbl_title: QLabel
    btn_save: QPushButton
    input_nombres: QLineEdit
    input_apellido_paterno: QLineEdit
    input_apellido_materno: QLineEdit
    input_numero_identidad: QLineEdit
    date_fecha_nacimiento: QDateEdit
    cmb_genero: QComboBox

    def __init__(self, app: App, parent: PersonaFrame, title=""):
        super(PersonaDialog, self).__init__(parent=parent)
        uic.loadUi("ui/persona_dialog.ui", self)
        self._app = app
        self._frm_parent = parent
        self.entity = Persona()
        self.lbl_title.setText(title)
        self.btn_save.clicked.connect(self.save)

    def showEvent(self, evt: QShowEvent):
        return super().showEvent(evt)

    def closeEvent(self, evt: QShowEvent):
        self._app.app_screen.set_enabled_window(True)
        return super().closeEvent(evt)

    def load(self, entity: Persona):
        self.entity = entity
        self.input_nombres.setText(entity.nombres)
        self.input_apellido_paterno.setText(entity.apellido_paterno)
        self.input_apellido_materno.setText(entity.apellido_materno)
        self.input_numero_identidad.setText(entity.numero_identidad)
        self.date_fecha_nacimiento.setDate(entity.fecha_nacimiento)
        self.cmb_genero.setCurrentText(genero_to_str(entity.genero))

    def save(self, evt: QObject):
        self.entity.nombres = self.input_nombres.text()
        self.entity.apellido_paterno = self.input_apellido_paterno.text()
        self.entity.apellido_materno = self.input_apellido_materno.text()
        self.entity.numero_identidad = self.input_numero_identidad.text()
        self.entity.fecha_nacimiento = self.date_fecha_nacimiento.date().toPyDate()
        self.entity.genero = str_to_genero(self.cmb_genero.currentText())

        session.add(self.entity)

        try:
            session.commit()
            SuccessMessageBox(text="Los datos se guardaron").exec()
            self._frm_parent.load()
            self.close()
        except Exception as e:
            session.rollback()
            CriticalMessageBox(text="No se pudo guardar los datos").exec()
