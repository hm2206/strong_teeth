from app import App
from PyQt5.QtGui import QShowEvent
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QDialog, QLabel, QPushButton, QComboBox, QRadioButton
from PyQt5 import uic
from message_boxs.critical_message_box import CriticalMessageBox
from configs.db import session
from message_boxs.success_message_box import SuccessMessageBox
from models.paciente import Paciente, PacienteCondicionEnum
from models.persona import Persona
from screens.paciente_frame import PacienteFrame


class PacienteDialog(QDialog):

    lbl_title: QLabel
    btn_save: QPushButton
    cmb_persona: QComboBox
    radio_null: QRadioButton
    radio_embarazo: QRadioButton
    radio_lactancia: QRadioButton

    def __init__(self, app: App, parent: PacienteFrame, title=""):
        super(PacienteDialog, self).__init__(parent=parent)
        uic.loadUi("ui/paciente_dialog.ui", self)
        self._app = app
        self._frm_parent = parent
        self.entity = Paciente()
        self.lbl_title.setText(title)
        self.btn_save.clicked.connect(self.save)
        self.radio_null.toggled.connect(self.toggle_radio)
        self.radio_embarazo.toggled.connect(self.toggle_radio)
        self.radio_lactancia.toggled.connect(self.toggle_radio)

    def showEvent(self, evt: QShowEvent):
        self.load_personas()
        return super().showEvent(evt)

    def closeEvent(self, evt: QShowEvent):
        self._app.app_screen.set_enabled_window(True)
        return super().closeEvent(evt)

    def load(self, entity: Paciente):
        self.entity = entity
        persona = entity.persona
        self.cmb_persona.setCurrentText(persona.display_info())
        self.check_condicion()

    def load_personas(self):
        datos = session.query(Persona).all()
        for item in datos:
            persona: Persona = item
            self.cmb_persona.addItem(persona.display_info(), persona)

    def save(self, evt: QObject):
        persona: Persona = self.cmb_persona.currentData()
        self.entity.persona_id = persona.id
        session.add(self.entity)

        try:
            session.commit()
            SuccessMessageBox(text="Los datos se guardaron").exec()
            self._frm_parent.load()
            self.close()
        except Exception:
            session.rollback()
            CriticalMessageBox(text="No se pudo guardar los datos").exec()

    def toggle_radio(self):
        radio: QRadioButton = self.sender()
        name = radio.objectName()

        if (radio.isChecked()):
            if (name == self.radio_null.objectName()):
                self.entity.condicion = None
            elif (name == self.radio_embarazo.objectName()):
                self.entity.condicion = PacienteCondicionEnum.Embarazo
            elif (name == self.radio_lactancia.objectName()):
                self.entity.condicion = PacienteCondicionEnum.Lactancia

    def check_condicion(self):
        match self.entity.condicion:
            case PacienteCondicionEnum.Embarazo:
                self.radio_embarazo.setChecked(True)
            case PacienteCondicionEnum.Lactancia:
                self.radio_lactancia.setChecked(True)
            case _:
                self.radio_null.setChecked(True)
